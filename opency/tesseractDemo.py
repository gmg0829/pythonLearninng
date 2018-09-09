from PIL import Image
import pytesseract

path = "code.png"

text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)