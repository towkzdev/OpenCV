#การแสดงผลภาพ

import cv2
img = cv2.imread("image/1234.jpg")

#แสดงภาพ
cv2.imshow("Output",img) #.imshow แสดงภาพ
cv2.waitKey(delay = 0) # delay image close ปิดหน้าต่าง
cv2.destroyAllWindows()