file_name = input("Enter the file name to read: ")
file=open(file_name, "r")
try:
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()