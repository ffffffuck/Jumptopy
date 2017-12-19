import os

for path, dir, files in os.walk("c:/"):
    for file in files:
        if file[-3:] == '.py':
            f=open(os.path.join(path, file),'r')
        try:
            ff=f.read()
            if "def"in ff:
                f=open("C:\A\list.txt", 'a')
                f.write(os.path.join(path, file)+'\n')
                print(os.path.join(path, file))
        except: pass