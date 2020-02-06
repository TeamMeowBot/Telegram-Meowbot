from importlib import import_module
from meowbot import cat, MODULES


try:
    cat.start()
except Exception as e:
    print(e)
    exit(1)

s = "Successfully loaded\n"
for module in MODULES:
    try:
        imported_module = import_module("meowbot.modules." + module)
        s = s + "- " + module + "\n"
    except ModuleNotFoundError as e:
        print("Module " + e.name + " is not found on modules folder.")

print(s + "modules.")