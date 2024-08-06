#การอ่านภาพ
import cv2

img = cv2.imread("image/1234.jpg")
print(img) #result 
print(img.ndim) #.ndim Array dimention 
print (type(img.ndim)) #data type of .ndim Array dimention 