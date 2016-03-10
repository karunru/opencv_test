import cv2
import sys
import matplotlib.pyplot as plt

argvs = sys.argv
if (len(argvs) != 2):
	print('Usage: $ python %s filename' % argvs[0])
	exit()
 
imagefilename = argvs[1]
try:
	img = cv2.imread(imagefilename, 1)
except:
	print('faild to load %s' % imagefilename)
	exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# view image
# windowName = 'LoadImage'
# cv2.imshow( windowName, img)
# cv2.waitKey(0)
# print('press any key to exit.')
# cv2.destroyAllWindows()

# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
