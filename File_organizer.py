import shutil
import os

# Get the current working directory
cwd=os.getcwd("file_name")
print(f"Current directory:{cwd}")
 
# Create a new folder
if not os.path.exists("Created_folder"):
    os.mkdir("Created_folder")
    print(f"New file name:{"Created_folder"} created")

# Create a file inside the folder
file_path=os.path.join("Created_folder","file_name")
with open(file_path,"w") as f:
    f.write("This is written inside the file\n")
print("File created inside the folder 'Created_folder'")

# To copy a file to a new file
Copied_file=os.path.join("Created_folder","Copied_file") 
shutil.copy("file_name","Copied_file")
print("File copied")

# Move the copied file to another folder
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
shutil.move("Copied_file","new_folder")
print("File moved")

# Delete a file or a folder(permanently)
shutil.rmtree("Name_Of_File")
shutil.rmtree("Name_Of_Folder")

