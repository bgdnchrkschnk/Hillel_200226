from pathlib import Path


current_dir = Path.cwd() # шлях до директорії файла
home_dir = Path.home() # домашній шлях юзера в OC

# 1 спосіб створити обʼєкт - передати шлях
repository_dir_1: Path = Path("/Users/milanstar/PycharmProjects/Hillel_200226")

# print(current_dir)
# print(home_dir)
# print(repository_dir_1)

repository_dir: Path = current_dir.parent.parent
# print(repository_dir) # друкуємо повний шлях до директорії
# print(repository_dir.name) # друкуємо назву директорії без повного шляху


# for obj in repository_dir.iterdir():
#     if obj.is_dir(): # Чи є обʼєкт директорією?
#         print(obj)
#
# for obj in repository_dir.iterdir():
#     if obj.is_file(): # Чи є обʼєкт файлом?
#         print(obj)

repository_dirs: list[Path] = [obj for obj in repository_dir.iterdir() if obj.is_dir()]
repository_files: list[Path] = [obj for obj in repository_dir.iterdir() if obj.is_file()]

lesson_12_dir: Path = repository_dir / "lessons" / "lesson_12"
lesson_12_files: list[Path] = [obj for obj in lesson_12_dir.iterdir() if obj.is_file()]

lesson_12_test_logs: Path = lesson_12_dir / "test_logs" / "success_logs"


lesson_12_test_logs.mkdir(parents=True,
                          exist_ok=True) # parents - створити усі необхідні директорії цього шляху

success_log_file: Path = lesson_12_test_logs / "success_log.log"
success_log_file.touch() # створити файл


all_repository_py_files: list[Path] = [obj for obj in repository_dir.iterdir() if obj.is_file() and obj.suffix == ".py"]
# str.endswith(".py")
print(all_repository_py_files)