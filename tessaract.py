from urllib.request import urlopen
import pytesseract
from PIL import Image

url = "http://risovach.ru/upload/2014/02/mem/muzhik-bleat_43233947_orig_.jpg"

image = Image.open(urlopen(url))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
text =  pytesseract.image_to_string(image, lang='rus')
print(text.strip())
