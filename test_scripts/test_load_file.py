<<<<<<< Updated upstream
﻿import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.load_file import load_file

def test_load_file():
    # use the dummy XML we created so this can succeed today
    score = load_file("examples/example.xml")
=======
﻿from modules.load_file import load_file

def test_load_file():
    score = load_file("example.mscx")  # replace with a real file path
>>>>>>> Stashed changes
    if score:
        print("Load OK:", score)
    else:
        print("Load FAILED")

if __name__ == "__main__":
    test_load_file()
