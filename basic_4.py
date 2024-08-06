#กำหนดรูปแบบภาพ

#อ่านภาพ
import cv2
img = cv2.imread("image/1234.jpg",0) #mode image color 0=gray scale 1=full color -1=alpha

#resize
imgresize = cv2.resize(img,(800,800))

#แสดงภาพ
cv2.imshow("Output",imgresize) #.imshow แสดงภาพ
cv2.waitKey(delay = 0) # delay image close ปิดหน้าต่าง
cv2.destroyAllWindows()

