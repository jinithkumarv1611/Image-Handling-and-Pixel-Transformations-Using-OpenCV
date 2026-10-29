# Image-Handling-and-Pixel-Transformations-Using-OpenCV 

## AIM:
Write a Python program using OpenCV that performs the following tasks:

1) Read and Display an Image.  
2) Adjust the brightness of an image.  
3) Modify the image contrast.  
4) Generate a third image using bitwise operations.

## Software Required:
- Anaconda - Python 3.7
- Jupyter Notebook (for interactive development and execution)

## Algorithm:
### Step 1:
Load an image from your local directory and display it.

### Step 2:
Create a matrix of ones (with data type float64) to adjust brightness.

### Step 3:
Create brighter and darker images by adding and subtracting the matrix from the original image.  
Display the original, brighter, and darker images.

### Step 4:
Modify the image contrast by creating two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix).  
Display the original, lower contrast, and higher contrast images.

### Step 5:
Split the image  into B, G, R components and display the channels

## Program Developed By:
- **Name:** JINITH KUMAR V  
- **Register Number:** 212225040157

  ### Ex. No. 01

#### 1. Read the image ('parrot.jpg') using OpenCV imread() as a grayscale image.
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("parrot.jpg", cv2.IMREAD_GRAYSCALE)
```

#### 2. Print the image width, height & Channel.
```python
print("Height :", img.shape[0])
print("Width :", img.shape[1])
print("Channels : Grayscale (1)")
```

#### 3. Display the image using matplotlib imshow().
```python
plt.imshow(img, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()
```

#### 4. Save the image as a PNG file using OpenCV imwrite().
```python
cv2.imwrite("parrot.png", img)
```

#### 5. Read the saved image above as a color image using cv2.cvtColor().
```python
img_color = cv2.imread("parrot.png")
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
```

#### 6. Display the Colour image using matplotlib imshow() & Print the image width, height & channel.
```python
print("Height :", img_color.shape[0])
print("Width :", img_color.shape[1])
print("Channels :", img_color.shape[2])

plt.imshow(img_color)
plt.title("Color Image")
plt.axis("off")
plt.show()
```

#### 7. Crop the image to extract any specific (parrot alone) object from the image.
```python
crop = img_color[50:300, 80:300]

plt.imshow(crop)
plt.title("Cropped Image")
plt.axis("off")
plt.show()
```

#### 8. Resize the image up by a factor of 2x.
```python
resize = cv2.resize(crop, None, fx=2, fy=2)

plt.imshow(resize)
plt.title("Resized Image")
plt.axis("off")
plt.show()
```

#### 9. Flip the cropped/resized image horizontally.
```python
flip = cv2.flip(resize, 1)

plt.imshow(flip)
plt.title("Flipped Image")
plt.axis("off")
plt.show()
```

#### 10. Read in the image ('waterfall.jpg').
```python
img2 = cv2.imread("waterfall.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
```

#### 11. Add the following text to the dark area at the bottom of the image (centered on the image):
```python
text = "Beautiful Waterfall"

cv2.putText(img2,
            text,
            (40, img2.shape[0]-30),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (255,255,255),
            2)
```

#### 12. Draw a magenta rectangle that encompasses the launch tower and the rocket.
```python
cv2.rectangle(img2,
              (100,50),
              (350,400),
              (255,0,255),
              3)
```

#### 13. Display the final annotated image.
```python
plt.imshow(img2)
plt.title("Annotated Waterfall")
plt.axis("off")
plt.show()
```

#### 14. Read the image ('tiger.jpg').
```python
img = cv2.imread("tiger.jpg")
```

#### 15. Adjust the brightness of the image.
```python
matrix = np.ones(img.shape, dtype="uint8") * 50
```

#### 16. Create brighter and darker images.
```python
img_brighter = cv2.add(img, matrix)

img_darker = cv2.subtract(img, matrix)
```

#### 17. Display the images (Original Image, Darker Image, Brighter Image).
```python
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
```

#### 18. Modify the image contrast.
```python
img_lower = cv2.convertScaleAbs(img, alpha=0.8, beta=0)

img_higher1 = cv2.convertScaleAbs(img, alpha=1.1, beta=0)

img_higher2 = cv2.convertScaleAbs(img, alpha=1.2, beta=0)
```

#### 19. Display the images (Original, Lower Contrast, Higher Contrast).
```python
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
```

#### 20. Split the image (tiger.jpg) into the B,G,R components & Display the channels.
```python
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
```

#### 21. Merged the R, G, B , displays along with the original image
```python
merged = cv2.merge((b,g,r))

plt.figure(figsize=(8,4))

plt.subplot(121)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(122)
plt.imshow(cv2.cvtColor(merged,cv2.COLOR_BGR2RGB))
plt.title("Merged RGB")

plt.show()
```

#### 22. Split the image into the H, S, V components & Display the channels.
```python
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
```
#### 23. Merged the H, S, V, displays along with original image.
```python
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
```

## Output:
- **i)** Read and Display an Image.
<img width="217" height="50" alt="image" src="https://github.com/user-attachments/assets/e965067d-143f-438d-a8a0-9cc0364fcaaf" />
<img width="150" height="222" alt="image" src="https://github.com/user-attachments/assets/99d1116e-506c-4e06-bb82-9a8f00ba9283" />
<img width="181" height="50" alt="image" src="https://github.com/user-attachments/assets/85ed571d-6d26-4db4-8773-74d693c9c205" />
<img width="416" height="737" alt="parrot" src="https://github.com/user-attachments/assets/a5a3d398-d714-4496-9919-c4b17cc0cb05" />
<img width="221" height="217" alt="image" src="https://github.com/user-attachments/assets/6d649116-c306-48af-8963-575f060d3450" />
<img width="226" height="193" alt="image" src="https://github.com/user-attachments/assets/2aea3aa0-fe23-40e4-8abd-b02c1b48dae4" />
<img width="225" height="222" alt="image" src="https://github.com/user-attachments/assets/aea1bc84-b2f8-48cd-88a4-a4569db44f26" />
<img width="336" height="182" alt="image" src="https://github.com/user-attachments/assets/49c69eaa-1a11-46b6-9b8b-ede7a1e7a265" />

- **ii)** Adjust Image Brightness.
<img width="847" height="173" alt="image" src="https://github.com/user-attachments/assets/1b943bfd-cdbf-4042-9b19-d4a0687e5142" />
<img width="835" height="137" alt="image" src="https://github.com/user-attachments/assets/23d5c320-da28-40d2-89ed-e9861be52c99" />
<img width="826" height="186" alt="image" src="https://github.com/user-attachments/assets/6c8c61bc-70dd-4e74-9fe7-471d5f6a5084" />
<img width="602" height="202" alt="image" src="https://github.com/user-attachments/assets/025ad750-ef25-4052-acc5-b6dca543b05d" />

- **iii)** Modify Image Contrast.
<img width="826" height="182" alt="image" src="https://github.com/user-attachments/assets/af62c618-7839-4ffe-81a3-2892e14eefe2" />
<img width="602" height="193" alt="image" src="https://github.com/user-attachments/assets/410e2102-19cb-472c-b368-611d373dd143" />
<img width="698" height="478" alt="image" src="https://github.com/user-attachments/assets/6a2fdb94-9347-44dd-8a03-4dbf6e976770" />

- **iv)** Generate Third Image Using Bitwise Operations.
<img width="702" height="468" alt="image" src="https://github.com/user-attachments/assets/36da07bd-77f4-4906-af68-5c631d08bafb" />

## Result:
Thus, the images were read, displayed, brightness and contrast adjustments were made, and bitwise operations were performed successfully using the Python program.

