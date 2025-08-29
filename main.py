from modules.load_file import load_file
from modules.convert_xml import convert_xml
from modules.extract_notes import extract_notes
from modules.save_notes import save_notes

def main():
    print("=== MuseScore Notes Extractor ===")

    input_file = "example.mscx"  # replace with real file path
    score = load_file(input_file)
    if not score:
        print("❌ Failed to load file.")
        return

    xml_file = convert_xml(input_file)
    if not xml_file:
        print("❌ Conversion failed.")
        return

    notes = extract_notes(xml_file)
    if not notes:
        print("❌ No notes extracted.")
        return

    out_file = "output_notes.txt"
    if save_notes(notes, out_file):
        print(f"✅ Notes saved to {out_file}")
    else:
        print("❌ Failed to save notes.")

if __name__ == "__main__":
    main()
