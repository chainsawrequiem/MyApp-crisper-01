from modules.extract_notes import extract_notes

def test_extract_notes():
    notes = extract_notes("example.xml")
    if notes:
        print("Extract OK:", notes[:10])
    else:
        print("Extract FAILED")

if __name__ == "__main__":
    test_extract_notes()
