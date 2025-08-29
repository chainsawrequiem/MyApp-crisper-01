import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.extract_notes import extract_notes

def test_extract_notes():
    notes = extract_notes("examples/example.xml")
    if notes:
        print("Extract OK:", notes)
    else:
        print("Extract FAILED")

if __name__ == "__main__":
    test_extract_notes()
