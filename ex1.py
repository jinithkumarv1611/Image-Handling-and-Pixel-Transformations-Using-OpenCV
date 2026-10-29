import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("parrot.jpg", cv2.IMREAD_GRAYSCALE)
print("Height :", img.shape[0])
print("Width :", img.shape[1])
print("Channels : Grayscale (1)")
plt.imshow(img, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()
cv2.imwrite("parrot.png", img)
img_color = cv2.imread("parrot.png")
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
print("Height :", img_color.shape[0])
print("Width :", img_color.shape[1])
print("Channels :", img_color.shape[2])

plt.imshow(img_color)
plt.title("Color Image")
plt.axis("off")
plt.show()
crop = img_color[50:300, 80:300]

plt.imshow(crop)
plt.title("Cropped Image")
plt.axis("off")
plt.show()
resize = cv2.resize(crop, None, fx=2, fy=2)

plt.imshow(resize)
plt.title("Resized Image")
plt.axis("off")
plt.show()
flip = cv2.flip(resize, 1)

plt.imshow(flip)
plt.title("Flipped Image")
plt.axis("off")
plt.show()
img2 = cv2.imread("waterfall.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
text = "Beautiful Waterfall"

cv2.putText(img2,
            text,
            (40, img2.shape[0]-30),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (255,255,255),
            2)
cv2.rectangle(img2,
              (100,50),
              (350,400),
              (255,0,255),
              3)
plt.imshow(img2)
plt.title("Annotated Waterfall")
plt.axis("off")
plt.show()
img = cv2.imread("tiger.jpg")
matrix = np.ones(img.shape, dtype="uint8") * 50
img_brighter = cv2.add(img, matrix)

img_darker = cv2.subtract(img, matrix)
plt.figure(figsize=(12,4))

plt.subplot(131)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(img_darker,cv2.COLOR_BGR2RGB))
plt.title("Darker")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(img_brighter,cv2.COLOR_BGR2RGB))
plt.title("Brighter")
plt.axis("off")

plt.show()
img_lower = cv2.convertScaleAbs(img, alpha=0.8, beta=0)

img_higher1 = cv2.convertScaleAbs(img, alpha=1.1, beta=0)

img_higher2 = cv2.convertScaleAbs(img, alpha=1.2, beta=0)
plt.figure(figsize=(15,4))

plt.subplot(141)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(142)
plt.imshow(cv2.cvtColor(img_lower,cv2.COLOR_BGR2RGB))
plt.title("Lower Contrast")
plt.axis("off")

plt.subplot(143)
plt.imshow(cv2.cvtColor(img_higher1,cv2.COLOR_BGR2RGB))
plt.title("Higher 1.1")
plt.axis("off")

plt.subplot(144)
plt.imshow(cv2.cvtColor(img_higher2,cv2.COLOR_BGR2RGB))
plt.title("Higher 1.2")
plt.axis("off")

plt.show()
b,g,r = cv2.split(img)

plt.figure(figsize=(12,4))

plt.subplot(131)
plt.imshow(b,cmap="gray")
plt.title("Blue")

plt.subplot(132)
plt.imshow(g,cmap="gray")
plt.title("Green")

plt.subplot(133)
plt.imshow(r,cmap="gray")
plt.title("Red")

plt.show()
merged = cv2.merge((b,g,r))

plt.figure(figsize=(8,4))

plt.subplot(121)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(122)
plt.imshow(cv2.cvtColor(merged,cv2.COLOR_BGR2RGB))
plt.title("Merged RGB")

plt.show()
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(hsv)

plt.figure(figsize=(12,4))

plt.subplot(131)
plt.imshow(h,cmap="gray")
plt.title("Hue")

plt.subplot(132)
plt.imshow(s,cmap="gray")
plt.title("Saturation")

plt.subplot(133)
plt.imshow(v,cmap="gray")
plt.title("Value")

plt.show()
merged_hsv = cv2.merge((h,s,v))

rgb = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2RGB)

plt.figure(figsize=(8,4))

plt.subplot(121)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(122)
plt.imshow(rgb)
plt.title("Merged HSV")

plt.show()
img1 = cv2.imread("parrot.jpg")
img2 = cv2.imread("tiger.jpg")

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)

plt.figure(figsize=(15,4))

plt.subplot(141)
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.title("Image 1")

plt.subplot(142)
plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
plt.title("Image 2")

plt.subplot(143)
plt.imshow(cv2.cvtColor(bit_and,cv2.COLOR_BGR2RGB))
plt.title("Bitwise AND")

plt.subplot(144)
plt.imshow(cv2.cvtColor(bit_or,cv2.COLOR_BGR2RGB))
plt.title("Bitwise OR")

plt.show()