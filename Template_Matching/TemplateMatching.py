import numpy as np
import cv2

def TemplateMatching(src, temp,
                     stepsize):  # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0
    var_t = 0
    location = [0, 0]

    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------
    mean_t = np.mean(temp)
    var_t = np.var(temp)
    # print(mean_t,var_t)
    max_corr = 0
    corr = 0
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, temp.shape[0], stepsize):
        for j in np.arange(0, temp.shape[1], stepsize):
            mean_s = 0
            var_s = 0
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------
            mean_s = np.mean(src)
            var_s = np.var(src)
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------
            # for k in np.arange(0, temp.shape[0], stepsize):
            #     for l in np.arange(0, temp.shape[1], stepsize):
            corr = (src[i][j] - mean_s) * (temp[i][j] - mean_t) / (var_s*var_t)
            if corr > max_corr:
                max_corr = corr
                location = [i, j]

    return location


# load source and template images
source_img = cv2.imread('source_img.jpg', 0)  # read image in grayscale
temp = cv2.imread('template_img.jpg', 0)  # read image in grayscale
location = TemplateMatching(source_img, temp, 20);
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------
red = (0,0,255)
cv2.line(match_img,(location[1],location[0]),(location[1]+temp.shape[1],location[0]),red,thickness=5)
cv2.line(match_img,(location[1],location[0]),(location[1],location[0]+temp.shape[0]),red,thickness=5)
cv2.line(match_img,(location[1],location[0]+temp.shape[0]),(location[1]+temp.shape[1],location[0]+temp.shape[0]),red,thickness=5)
cv2.line(match_img,(location[1]+temp.shape[1],location[0]),(location[1]+temp.shape[1],location[0]+temp.shape[0]),red,thickness=5)

# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------
cv2.imwrite("match_img.jpg",match_img)

# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()