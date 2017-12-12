def pythontoc():
    f= open("learning_python.txt",'r')
    python = f.read()
    C_repl = python.replace("python", "C")
    print(C_repl)
    f.close()

    f= open("learning_python_copied.txt", 'w')
    f.write(C_repl)
    f.close()

pythontoc()