import os



path = os.path.expanduser(r"~\Desktop")
print(path)
ext = input("Enter the extension of the file you want to search for: ")
count = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(ext):
            count += 1
            print(file)
print(f"Number of files with extension {ext} is: {count}")


