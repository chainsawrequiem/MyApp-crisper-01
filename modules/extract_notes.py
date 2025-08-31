<<<<<<< Updated upstream
﻿from music21 import converter, note, chord

def extract_notes(xml_path):
    """
    Extract note names from a MusicXML file.
    Returns a list of note names (e.g., ['C4','E4','G4']) in score order.
    - Rests are skipped.
    - Chords are expanded low->high.
    """
    try:
        score = converter.parse(xml_path, format='musicxml')
    except Exception as e:
        print(f"Error loading XML: {e}")
        return []

    names = []
    for n in score.recurse().notes:
        if isinstance(n, note.Note):
            if n.pitch is not None:
                names.append(n.pitch.nameWithOctave)
        elif isinstance(n, chord.Chord):
            for p in sorted(n.pitches, key=lambda p: p.midi):
                names.append(p.nameWithOctave)
    return names
=======
﻿def extract_notes(xml_path):
    """
    Extract note names from a MusicXML file.
    Returns a list of notes in order, or an empty list if extraction fails.
    """
    # TODO: implement note extraction logic
    return []
>>>>>>> Stashed changes
