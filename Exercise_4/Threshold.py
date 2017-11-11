import cv2
src = cv2.imread('Lenna.png',1)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Input Image",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Input Image", src)

# 0: Binary,      1: Binary Inverted,      2: Threshold Truncated,      3: Threshold to Zero,      4: Threshold to Zero Inverted    */
# cv2.THRESH_BINARY, cv2.THRESH_BINARYINV, cv2.THRESH_TRUNC, cv2.THRESH_ZERO, cv2.THRESH_ZERO_INV
threshold_value = 128
max_threshold_value = 255

# Threshold Truncating
filler,dst = cv2.threshold(gray, threshold_value, max_threshold_value, cv2.THRESH_TRUNC)
cv2.namedWindow("Threshold Truncated",cv2.WINDOW_AUTOSIZE)
cv2.imshow('Threshold Truncated', dst)

# Binary Thresholding
filler, thresholded = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Thresholding', thresholded)

# Band Thresholding
threshold1 = 55
threshold2 = 73
filler,binary_image1 = cv2.threshold(gray, threshold1, max_threshold_value, cv2.THRESH_BINARY)
filler,binary_image2 = cv2.threshold(gray, threshold2, max_threshold_value, cv2.THRESH_BINARY_INV)
band_thresholded_image = cv2.bitwise_and(binary_image1, binary_image2)
cv2.imshow('Band Thresholding', band_thresholded_image)

# Otsu Thresholding
filler,otsu_binary_image = cv2.threshold(gray, 0, max_threshold_value, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Otsu Thresholding", otsu_binary_image)

# Semi Thresholding

filler,otsu_inv_bin = cv2.threshold(gray, threshold_value, max_threshold_value, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
semi_thresholded_image = cv2.bitwise_and(gray, otsu_inv_bin)
# cv2.imshow("otsu_inv_bin",otsu_inv_bin)
cv2.imshow("Semi Thresholding", semi_thresholded_image)

# Adaptive Thresholding

otsu_bin_2 = cv2.threshold(gray, threshold_value, max_threshold_value, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
adaptive_thresholded_binary_image1 = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 20)
adaptive_thresholded_binary_image2 = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 20)
cv2.imshow("Adaptive_Thresholding_1", adaptive_thresholded_binary_image1)
cv2.imshow("Adaptive_Thresholding_2", adaptive_thresholded_binary_image2)

cv2.waitKey(0)
