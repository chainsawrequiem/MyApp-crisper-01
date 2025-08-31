<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
﻿import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.save_notes import save_notes

def test_save_notes():
    notes = ["C4", "E4", "G4"]
    out_file = "examples/test_output.txt"
    ok = save_notes(notes, out_file)
    print("Save OK" if ok else "Save FAILED")
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
﻿from modules.save_notes import save_notes

def test_save_notes():
    notes = ["C4", "E4", "G4"]
    out_file = "test_output.txt"
    save_notes(notes, out_file)
    print("Saved notes to", out_file)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

if __name__ == "__main__":
    test_save_notes()
