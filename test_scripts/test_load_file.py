from modules.load_file import load_file

def test_load_file():
    score = load_file("example.mscx")  # replace with a real file path
    if score:
        print("Load OK:", score)
    else:
        print("Load FAILED")

if __name__ == "__main__":
    test_load_file()
