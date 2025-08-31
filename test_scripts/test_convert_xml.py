<<<<<<< Updated upstream
﻿import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.convert_xml import convert_xml

def test_convert_xml():
    # placeholder — needs a real .mscx later
    result = convert_xml("examples/example.mscx")
=======
﻿from modules.convert_xml import convert_xml

def test_convert_xml():
    result = convert_xml("example.mscx")
>>>>>>> Stashed changes
    if result:
        print("Convert OK")
    else:
        print("Convert FAILED")

if __name__ == "__main__":
    test_convert_xml()
