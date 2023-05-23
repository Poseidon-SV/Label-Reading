#14th - 16th C
# Install Tesseract-ORC Executable file
''''''
'pip install pytesseract'

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'E:\Shubham\Desktop\AI-ML\PantechSolutions_AI_Master_classes\12_Label_Reading\tesseract\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('1.png')
print(info)

file = open("result.txt", "w")
file.write(info)
file.close()
print("Written Successful")