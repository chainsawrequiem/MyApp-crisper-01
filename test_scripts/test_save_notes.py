from modules.save_notes import save_notes

def test_save_notes():
    notes = ["C4", "E4", "G4"]
    out_file = "test_output.txt"
    save_notes(notes, out_file)
    print("Saved notes to", out_file)

if __name__ == "__main__":
    test_save_notes()
