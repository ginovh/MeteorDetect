import numpy as np
import cv2 # is much faster than skimage to read/write file
import sys
import multiprocessing

images = sys.argv[1:]

import cv2
def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

images = [cv2.imread(path,0) for path in images]
def proc_one(indx):
#for indx in range(1,len(images)-1):
#	all = np.stack([images[indx-1],images[indx],images[indx+1]])
	all = [images[indx-1],images[indx],images[indx+1]]
	median = np.median(all, axis=0).astype(dtype='uint8')
	
	median_sub = cv2.subtract(images[indx], median) # must use saturation for subtraction!

	gamma_corrected = adjust_gamma(median_sub, gamma=2)
	cv2.imwrite("out_median"+ str(indx) +".png", gamma_corrected)
	
pool_obj = multiprocessing.Pool()
#print(pool_obj)
res = pool_obj.map(proc_one,range(1,len(images)-1))
#print(res)


