Exercise 4

The image used in this exercise is Lenna.png

1.) When threshold_value is set to 0, the Threshold Truncated image is completely black, and the Binary Thresholding image is completely white.
When threshold_value is set to 255, the Threshold Truncated image is a complete grayscale image, and the Binary Thresholding image is completely black.
For Band Thresholding, if both threshold values are the same, the image is completely black, but if both values are completely opposite of each other (0 and 255), the image is completely white.
For Otsu Thresholding, the threshold value is changed to a value that optimizes the image in binary thresholding as much as possible.  Even if the threshold value is 0 or 255, this value is changed to a value in the middle of this range.
The Semi Thresholding image is a bit darker in the light areas than an Otsu thresholding in binary inverse.  Some more details from the original image are visisible in the Semi Thresholding image.
In the first Adaptive Thresholding image, most outlines in the image are visible, while the second Adaptive Thresholding image shows more details in some areas that the first one does not show.

2.) The disadvantages of binary threshold are that an image is completely black if its threshold value is 0 and completely white if the threshold value is 255.  Binary threshold only shows two distinct colors in an image (black and white) instead of an array of many shades of gray that range from black to white.  Since there are only two distinct colors, some of the details in the image used are lost to the human eye.

3.) Adaptive thresholding is useful when a person needs to outline the details in an image or see details that binary thresholding cannot show.
