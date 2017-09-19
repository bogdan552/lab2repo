def stroka():
    s = "Hello, world"
    z = ""
    for i in range(len(s[::-1])):
        z += s[-1-i]
    print(z)


stroka()
stroka()
stroka()