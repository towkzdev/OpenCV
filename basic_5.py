#การเขียนภาพ (Export)

import cv2

img = cv2.imread("image/1234.jpg",0)
imgresize = cv2.resize(img,(400,400))
cv2.imshow("My picture",imgresize)

cv2.imwrite("Output.jpg",imgresize)

cv2.waitKey(0) # delay image close ปิดหน้าต่าง
cv2.destroyAllWindows()