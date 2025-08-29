from pathlib import Path
from music21 import converter

def convert_xml(path: str):
    """
    If input is .xml -> return it unchanged.
    If input is .mscx -> write MusicXML next to it and return the new .xml path.
    Returns None on failure.
    """
    p = Path(path)
    if p.suffix.lower() == ".xml":
        return str(p)

    if p.suffix.lower() == ".mscx":
        try:
            score = converter.parse(str(p))
            out_path = p.with_suffix(".xml")
            score.write('musicxml', fp=str(out_path))
            return str(out_path)
        except Exception as e:
            print("Error converting to MusicXML:", e)
            return None

    print("Unsupported input type:", p.suffix)
    return None
