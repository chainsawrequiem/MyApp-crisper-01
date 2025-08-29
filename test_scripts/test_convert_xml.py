from modules.convert_xml import convert_xml

def test_convert_xml():
    result = convert_xml("example.mscx")
    if result:
        print("Convert OK")
    else:
        print("Convert FAILED")

if __name__ == "__main__":
    test_convert_xml()
