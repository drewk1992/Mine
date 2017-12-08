import cv2
import numpy as np
#im = cv2.imread('Trimmed/r_re_nir.png',0)
 
def get_gradient(im) :
    # Calculate the x and y gradients using Sobel operator
    grad_x = cv2.Sobel(im,cv2.CV_32F,1,0,ksize=3)
    grad_y = cv2.Sobel(im,cv2.CV_32F,0,1,ksize=3)
 
    # Combine the two gradients
    grad = cv2.addWeighted(np.absolute(grad_x), 0.5, np.absolute(grad_y), 0.5, 0)
#    cv2.imwrite('Trimmed/grad.png',grad)
    return grad
#get_gradient(im)
