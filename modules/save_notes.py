<<<<<<< Updated upstream
<<<<<<< Updated upstream
﻿from pathlib import Path

def save_notes(notes, out_file):
    """
    Save a list of note names to a text file, one per line.
    Returns True if successful, False otherwise.
    - Creates parent folders if needed.
    """
    try:
        out_path = Path(out_file)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [(str(n)).strip() for n in notes]
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            for line in lines:
                f.write(line + "\n")
        return True
    except Exception as e:
        print(f"Error saving notes to {out_file}: {e}")
        return False
=======
=======
>>>>>>> Stashed changes
﻿def save_notes(notes, out_file):
    """
    Save a list of note names to a text file, one per line.
    Returns True if successful, False otherwise.
    """
    # TODO: implement save logic
    return False
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
