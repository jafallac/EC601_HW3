import cv2
import copy
import numpy as np

def addGaussianNoise(image,mean,sigma):
    gauss = np.random.normal(mean,sigma,image.shape)
    noisy = image + gauss
    return noisy
def addSaltAndPepperNoise(image, noise_percentage):
    s_vs_p = 0.5
    amount = 0.01*noise_percentage
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in image.shape]
    out[coords] = 255

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in image.shape]
    out[coords] = 0
    return out


def main():
    src = cv2.imread('Lenna.png', 0)
    cv2.namedWindow("Original image")
    cv2.imshow("Original image", src)

    noise_img = src
    mean = float(0.0)
    sigma = float(50)
    noise_img = addGaussianNoise(noise_img, mean, sigma)
    cv2.imshow("Gaussian Noise", noise_img)

    noise_dst = cv2.blur(noise_img, (5, 5))
    cv2.imshow("Box filter", noise_dst)

    noise_dst1 = cv2.GaussianBlur(noise_dst, (5, 5), 0)  # 1.5)
    cv2.imshow("Gaussian filter", noise_dst1)

    noise_dst2 = noise_img.astype(np.uint8)
    noise_dst2 = cv2.medianBlur(noise_dst2, 5)
    cv2.imshow("Median filter", noise_dst2)

    noise_img2 = src
    noise_percentage = float(10)
    noise_img2 = addSaltAndPepperNoise(noise_img2, noise_percentage)
    cv2.imshow("Salt and Pepper Noise", noise_img2)

    noise_dst3 = noise_img2
    cv2.blur(noise_dst3, (5, 5))
    cv2.imshow("Box filter_Salt_Pepper", noise_dst3)

    noise_dst4 = noise_img2
    cv2.GaussianBlur(noise_dst4, (7, 7), 0)
    cv2.imshow("Gaussian filter_Salt_Pepper", noise_dst4)

    noise_dst5 = noise_img2
    cv2.medianBlur(noise_dst5, 5)
    cv2.imshow("Median filter_Salt_Pepper", noise_dst5)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()