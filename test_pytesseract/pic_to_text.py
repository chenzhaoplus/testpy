# 图片转文字
from PIL import Image
import pytesseract

img = Image.open('test1.png')
# text = pytesseract.image_to_string(img, lang='eng')
text = pytesseract.image_to_string(img, lang='chi_sim')

print(text)
