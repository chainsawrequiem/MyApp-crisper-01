import argparse
from pathlib import Path
from modules.load_file import load_file
from modules.convert_xml import convert_xml
from modules.extract_notes import extract_notes
from modules.save_notes import save_notes

def run(input_path: str, output_path: str):
    input_path = Path(input_path)

    # 1) Load (for basic validation/logging)
    score = load_file(str(input_path))
    if not score:
        print("❌ Failed to load file:", input_path)
        return False

    # 2) Convert (no-op for .xml)
    xml_file = convert_xml(str(input_path))
    if not xml_file:
        print("❌ Conversion failed.")
        return False

    # 3) Extract notes
    notes = extract_notes(xml_file)
    if not notes:
        print("❌ No notes extracted.")
        return False

    # 4) Save notes
    ok = save_notes(notes, output_path)
    if ok:
        print(f"✅ Notes saved to {output_path}")
    else:
        print("❌ Failed to save notes.")
    return ok

def main():
    parser = argparse.ArgumentParser(description="MuseScore/MusicXML → notes list")
    parser.add_argument("input", help="Path to .mscx or .xml")
    parser.add_argument("output", help="Path to output .txt")
    args = parser.parse_args()
    run(args.input, args.output)

if __name__ == "__main__":
    main()
