import sys

learning_python = sys.argv[1]
learning_python_copied = sys.argv[2]

f= open("learning_python.txt")
python = f.read()
C_repl = python.replace("python", "C")
f.close()
print(C_repl)

f= open("learning_python_copied.txt", 'w')
f.write(C_repl)
f.close()

