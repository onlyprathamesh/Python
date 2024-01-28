f = open('file_handling.txt', 'w')
f.write("Welcome to Python")
f.close()


f = open('file_handling.txt', 'r')
text = f.read()
print(text)
f.close()


f = open('file_handling.txt', 'a')
f.write(", new Text appended")
f.close()
f = open('file_handling.txt', 'r')


text = f.read()
print(text)
f.close()