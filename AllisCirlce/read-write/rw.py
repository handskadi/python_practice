# open a file for reading
with open('text.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()
