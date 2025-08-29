from music21 import converter

def load_file(path):
    """
    Load a MuseScore (.mscx or .xml) file using music21.
    Returns the parsed score object, or None if loading fails.
    """
    try:
        score = converter.parse(path)
        return score
    except Exception as e:
        print("Error loading file:", e)
        return None
