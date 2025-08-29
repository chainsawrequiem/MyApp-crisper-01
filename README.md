# MyApp — MuseScore/MusicXML → Notes (TXT)

This tool extracts note names from a MuseScore `.mscx` or MusicXML `.xml` file
and saves them to a `.txt` file (one note per line).

It ships with two entry points:

- **CLI**: `main.py` → also built as `dist/NoteExtractor.exe`
- **GUI**: `gui_main.py` → also built as `dist/NoteExtractorGUI.exe`

---

## Quick Start

### 1) Activate environment
**Anaconda Prompt**
```cmd
cd D:\MyApp
conda activate myapp_env
```

### 2) Run GUI (recommended for everyday use)
```cmd
python gui_main.py
```
- Click **Browse & Extract**
- Choose a `.mscx` or `.xml`
- Choose where to save the `.txt` file
- You’ll see a success message when done

### 3) Run CLI (fallback / testing)
```cmd
python main.py examples\example.xml examples\out.txt
```

---

## Packaged executables

After building with PyInstaller you’ll have:

- `dist\NoteExtractorGUI.exe`  ← **double-clickable GUI**
- `dist\NoteExtractor.exe`     ← CLI (use from terminal)

### Build (one time or when code changes)
**Anaconda Prompt**
```cmd
cd D:\MyApp
conda activate myapp_env
pyinstaller --onefile --noconsole --name NoteExtractorGUI gui_main.py
pyinstaller --onefile --name NoteExtractor main.py
```

### Run (PowerShell examples)
```powershell
# GUI (double-click or run)
cd "D:\MyApp\dist"
.\NoteExtractorGUI.exe

# CLI with absolute paths (works from anywhere)
& "D:\MyApp\dist\NoteExtractor.exe" "D:\MyApp\examples\example.xml" "D:\MyApp\examples\from_exe.txt"
Get-Content "D:\MyApp\examples\from_exe.txt"
```

---

## Test Data

A small MusicXML file is included:
```
D:\MyApp\examples\example.xml
```
Expected extraction result:
```
C4
E4
G4
```

---

## Troubleshooting

- **Nothing happens when I double-click the EXE**  
  Use the **GUI exe**: `NoteExtractorGUI.exe`. The CLI exe (`NoteExtractor.exe`) needs arguments.

- **“ModuleNotFoundError: modules …” when running tests**  
  Run tests as modules:  
  `python -m test_scripts.test_extract_notes`  
  (or use the patched tests we include that set `sys.path`)

- **“Can’t parse XML / empty NOTES”**  
  Make sure `lxml` is installed:
  ```cmd
  conda activate myapp_env
  pip install lxml
  ```

- **Path confusion**  
  Prefer **absolute paths** in PowerShell:
  ```powershell
  & "D:\MyApp\dist\NoteExtractor.exe" "D:\MyApp\examples\example.xml" "D:\MyApp\examples\out.txt"
  ```

---

## Git: Standing Rule (check → then commit)

1. Run the step/check.
2. If it **passes** → commit:
   - **Git Bash**
     ```bash
     cd /d/MyApp
     git add .
     git commit -m "Describe the working step"
     ```
3. If it **fails** → do **not** commit. Paste the full output into chat; fix first.

### Roll back to last working state
```bash
cd /d/MyApp
git reset --hard
```

---

## Project Structure
```
MyApp/
  modules/
    load_file.py
    convert_xml.py
    extract_notes.py
    save_notes.py
  test_scripts/
    test_load_file.py
    test_convert_xml.py
    test_extract_notes.py
    test_save_notes.py
  examples/
    example.xml
  main.py          # CLI
  gui_main.py      # GUI
  dist/            # built EXEs (ignored by git)
  build/           # pyinstaller build (ignored by git)
  .gitignore
  README.md
  checkpoint_log.txt
```
