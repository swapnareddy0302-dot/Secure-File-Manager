file_name=input("Enter the file name to create: ")
try:
    with open(file_name,"w") as file:
        content=input("Enter the content for the file: ")
        file.write(content)
except Exception as e:
    print(f"An error occurred: {e}")