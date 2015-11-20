import cv2
import sys
import matplotlib.pyplot as plt

argvs = sys.argv
if (len(argvs) != 2):
	print 'Usage: $ python %s filename' % argvs[0]
quit()
 
imagefilename = argvs[1]
try:
	img = cv2.imread(imagefilename, 1)
except:
	print 'faild to load %s' % imagefilename
	quit()
 
# view image
windowName = 'LoadImage'
cv2.imshow( windowName, img)
print 'press any key to exit.'
 
cv2.waitKey(0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
