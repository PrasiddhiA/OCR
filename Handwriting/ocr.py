import cv2
import pytesseract
img = cv2.imread("image.jpg")
#img = cv2.resize(img, (100, 100))
cv2.waitKey(0)
cv2.destroyAllWindows()
pytesseract.pytesseract.tesseract_cmd=r'c:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img) 
print(text)     #print the result
