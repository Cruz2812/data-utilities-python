"""Check Python/Jupyter environment to troubleshoot missing modules."""
import sys

print("Python executable path:", sys.executable)
print("Python version:", sys.version)

# Try to import common modules used in the original doc
modules_to_test = ["pandas", "html5lib", "bs4", "lxml"]
for mod in modules_to_test:
    try:
        m = __import__(mod)
        print(f"{mod} loaded from: {m.__file__}")
    except Exception as e:
        print(f"FAILED to import {mod}: {e}")

print("\nIf a module above failed, install it in the SAME environment as this interpreter:")
print(f"{sys.executable} -m pip install <module_name>")
