import cv2
print("hello world")

img = cv2.imread('lena.jpg', 0)

print(img)

cv2.imshow('image',img)
k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()                             #to delete the displaying window 
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img)                    #to save file
    cv2.destroyAllWindows()

