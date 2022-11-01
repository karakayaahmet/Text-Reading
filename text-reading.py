from PIL import Image
import pytesseract

img = Image.open("text.png")
text_tur = pytesseract.image_to_string(img, lang="tur")
text_eng = pytesseract.image_to_string(img, lang="eng")
print("türkçe: ",text_tur)
print("ingilizce: ",text_eng)

