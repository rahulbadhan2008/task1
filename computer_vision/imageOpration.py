import cv2
img = cv2.imread('images.jpg')
height, width = img.shape[:2]
width_img = cv2.resize(img,(int(width*0.25)+width, height), interpolation = cv2.INTER_CUBIC)
cv2.imwrite('output/x_25%.jpg',width_img)
hight_img = cv2.resize(img,(width, int(height*0.25)+height), interpolation = cv2.INTER_CUBIC)

cv2.imwrite('output/y_25%.jpg',hight_img)

image_90 = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('output/image_90.jpg',image_90)
image_90_ = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('output/image_-90.jpg',image_90_)



cv2.imshow('Image x axis by 25%',width_img)
cv2.imshow('Image y axis by 25%',hight_img)
cv2.imshow('Rotate by 90',image_90)
cv2.imshow('Rotate by - 90',image_90_)


cv2.imshow('Orignal Img%',img)



cv2.waitKey(0)
cv2.destroyAllWindows()