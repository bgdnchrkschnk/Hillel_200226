import pathlib
import sys


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))
print(sys.path)
import esng
print(esng)