import re

p = re.compile(r"(\w+)\s\1")
m = p.search("sdf Hello Hello ")

print(m)


p = re.compile(r"(\w+)\s(\w+)\s\1\s\2")
m = p.search("sdf Hello World Hello World dkfjkdsdf")

print(m)