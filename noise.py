import cv2
import copy
import numpy as np

def addGaussianNoise(image,average,stddev):
    cv2.randn(image, average, stddev)
    return image

def addSaltAndPepperNoise(image, noise_percentage):
    image_rows = image.rows
    image_cols = image.cols
    image_channels = image.channels()

def main():
    src = cv2.imread('Lenna.png',0)
    cv2.namedWindow( "Original image")
    cv2.imshow( "Original image", src)
    
    noise_img = src.copy()
    average = double(0.0)
    stddev = double(50)
    noise_img = addGaussianNoise(noise_img,average,stddev)
    cv2.imshow( "Gaussian Noise", noise_img)
    
    noise_dst = noise_img.copy()
    cv2.blur(noise_dst,(5,5))
    cv2.imshow( "Box filter", noise_dst)
    
    noise_dst1 = noise_dst.copy()
    cv2.GaussianBlur(noise_dst1, (5,5), 1.5)
    cv2.imshow( "Gaussian filter", noise_dst1)
    
    noise_dst2 = noise_img.copy()
    cv2.medianBlur(noise_dst2, 5)
    cv2.imshow( "Median filter", noise_dst2)
    
    noise_img2 = src.copy()
    noise_percentage = double(10)
    addSaltAndPepperNoise(noise_img2, noise_percentage)
    cv2.imshow( "Salt and Pepper Noise", noise_img2)

    noise_dst3 = noise_img2.copy()
    cv2.blur(noise_dst3,(5,5))
    cv2.imshow( "Box filter", noise_dst3)

    noise_dst4 = noise_img2.copy()
    cv2.GaussianBlur(noise_dst4,(5,5),1.5)
    cv2.imshow( "Gaussian filter", noise_dst4)
    
    noise_dst5 = noise_img2.copy()
    cv2.medianBlur(noise_dst5,5)
    cv2.imshow( "Median filter", noise_dst5)
    
    cv2.waitKey(0)
if __name__=="__main__":
    main()
