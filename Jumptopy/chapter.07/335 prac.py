from xml.etree.ElementTree import Element, SubElement, dump, ElementTree,parse

def indent(elem, level=0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


print("<blog page>")
blog = Element("blog")
blog.attrib["date"] = "20180108"
blog.attrib["editor"] = "Pycharm"
subject = Element("subject")
author = Element("author")
Agenda = Element("Agenda")
blog.append(subject)
blog.append(author)
blog.append(Agenda)
subject.text = "Why Python?"
author.text = "Eric"
Agenda.text = ""


SubElement(author, "age").text = "58"
SubElement(author, "nation").text = "USA"

SubElement(Agenda, "A").text = "Data Type"
SubElement(Agenda, "B").text = "Control Flow"
SubElement(Agenda, 'C').text = "Function"


indent(blog)
dump(blog)
ElementTree(blog).write("blog.xml")

tree = parse("blog.xml")
blog = tree.getroot()


from_tag = blog.find("subject")
print()
print("<Subject>")
print(from_tag.text)


print()
print("<author's Child>")
for parent in blog.findall("author"):
    for child in parent:
        print(child.text)


print()
print("<Agenda's Child>")
for parent in blog.getiterator("Agenda"):
    for child in parent:
        print(child.text)

print()
print("<all of blog>")
print(blog.keys())

