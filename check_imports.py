mods = ["music21","pretty_midi","lxml","numpy","matplotlib","mido","tqdm","PIL","simpleaudio","vedo","jsonlines"]

bad = []
for m in mods:
    try:
        __import__("PIL" if m=="PIL" else m)
        print(f"{m}: OK")
    except Exception as e:
        print(f"{m}: ERROR -> {e}")
        bad.append((m, str(e)))

if bad:
    print("\nNEEDS FIX:", bad)
else:
    print("\nAll good.")
