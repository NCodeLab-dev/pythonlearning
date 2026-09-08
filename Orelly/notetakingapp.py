
#note taking app using open(),write()
"""


from datetime import datetime

notes= input("please take note\n>");
with open("note.txt",mode="a") as file:
    content = str(datetime.now().date())+" "+ notes+"\n"
    file.write(content)
"""
"""

#create a file in home directory or in the same folder and write to it (no append)
#file = Path.home()/"narayan.txt"
file = Path("narayan.txt")

file.write_text("hii this is narayan", encoding="utf-8")

print(file.read_text())
"""

from pathlib import Path
print("current path:",Path.cwd()) #current working directory
file_path = Path("narayan.txt")

with file_path.open('a', encoding="utf-8") as file:
    file.write("hii narayan\n")

print(file_path.read_text())