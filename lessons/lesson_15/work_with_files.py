from pathlib import Path
from faker import Faker
fake = Faker()



temp_dir = Path.cwd() / "temp"
temp_dir.mkdir(parents=True, exist_ok=True)

filename_w = "text_w.txt"
filename_a = "text_a.txt"
filename_writelines = "text_writelines.txt"

file_path_w: Path = temp_dir / filename_w
file_path_a: Path = temp_dir / filename_a
file_path_writelines: Path = temp_dir / filename_writelines


# ------------------------------ mode "w" запис у файл в режимі перезатирання

with file_path_w.open("w") as file:
    file.write(fake.text())
    file.write("\n\\n - symbol for going new line")
    file.write("\nNEW LINE")

# file = open("test.txt", "w")
# file.close()

# ------------------------------- mode "a" запис у режимі доповнення файлу

with file_path_a.open("a") as file:
    file.write("\n" + fake.text())
    file.write("\n\\n - symbol for going new line")
    file.write("\nNEW LINE")

# ---------------------------------- mode "r" зчитування файлу

# with file_path_a.open("r") as file:
#     all_file_text: str = file.read()
#     print(all_file_text)

with file_path_w.open("r") as file:
    all_lines_text: list[str] = file.readlines()
    # print(all_lines_text)

# ------------------------------ mode "w" запис у файл в режимі перезатирання

with file_path_writelines.open("w") as file:
    file.writelines(all_lines_text)
