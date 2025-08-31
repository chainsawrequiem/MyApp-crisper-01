<<<<<<< Updated upstream
﻿import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.extract_notes import extract_notes

def test_extract_notes():
    notes = extract_notes("examples/example.xml")
    if notes:
        print("Extract OK:", notes)
=======
﻿from modules.extract_notes import extract_notes

def test_extract_notes():
    notes = extract_notes("example.xml")
    if notes:
        print("Extract OK:", notes[:10])
>>>>>>> Stashed changes
    else:
        print("Extract FAILED")

if __name__ == "__main__":
    test_extract_notes()
