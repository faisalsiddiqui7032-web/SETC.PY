
import os
import shutil

# 1. Create store_data/logs folder twice
base = "store_data"
logs = os.path.join(base, "logs")

os.makedirs(logs, exist_ok=True)
os.makedirs(logs, exist_ok=True)


# 2. Create three files inside logs
p = os.path.join(logs, "p.txt")
q = os.path.join(logs, "q.txt")
r = os.path.join(logs, "r.csv")

with open(p, "w") as file:
    file.write("red\ngreen\n")

with open(q, "w") as file:
    file.write("blue\n")

with open(r, "w") as file:
    file.write("x,y\n1,2\n")


# 3. Print sorted list of .txt files
txt_files = sorted(
    name for name in os.listdir(logs)
    if name.endswith(".txt")
)

print(txt_files)


# 4. Read p.txt and print number of lines and first line
with open(p, "r") as file:
    lines = file.readlines()

print(len(lines), lines[0].strip())


# 5. Create archive folder and move p.txt
archive = os.path.join(base, "archive")

os.makedirs(archive, exist_ok=True)

shutil.move(p, archive)

logs_list = sorted(os.listdir(logs))
archive_list = sorted(os.listdir(archive))

print(logs_list, archive_list)


# 6. Rename q.txt to old_q.txt
old_q = os.path.join(logs, "old_q.txt")

os.rename(q, old_q)

print(os.path.exists(q), os.path.isfile(old_q))


# 7. Delete complete store_data folder
shutil.rmtree(base)

print(os.path.exists(base))
