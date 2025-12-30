import cv2
# script_point3.py
# Applies Grayscale -> GaussianBlur -> Canny and displays each result using cv2.imshow()
image_path = r"D:/BITS/Assignments/ADAS/Assignment2/pythonProject1/IMG_20251101_223026.jpg"
img = cv2.imread(image_path)
if img is None:
    print('Could not load image:', image_path)
    raise SystemExit(1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 100, 200)

# Show windows
cv2.imshow('a) Input Frame', img)
cv2.imshow('b) Grayscale', gray)
cv2.imshow('c) Gaussian Blur', blur)
cv2.imshow('d) Canny Edges', edges)

print('Close any image window or press any key while a window is focused to exit.')
cv2.waitKey(0)
cv2.destroyAllWindows()
