import pytesseract
from PIL import Image

image_path = "D:\Data Science\Deep Learning Projects\Text Extraction\Barcode number Extractor\runs\detect\predict\crops\barcode"
image = Image.open(image_path)