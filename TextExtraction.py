import easyocr
reader = easyocr.Reader(['en'])

with open("chinese_tra.jpg", "rb") as f:
    img = f.read()
result = reader.readtext(img)