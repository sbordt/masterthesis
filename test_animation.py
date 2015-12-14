import numpy as np
import cv2
import matplotlib.pyplot as plt

import io
from PIL import Image

def gen_frame(i):
	# create the frame as a matplotlib figure
	fig = plt.figure(figsize=(19.20, 10.80), dpi=100)
	plt.ylim((-1,1+0.002*i))

	x = np.linspace(0, 2 * np.pi, 120)
	plt.plot(x,np.sin(0.002*i+x))

	# figure to png in memory
	buf = io.BytesIO()
	fig.savefig(buf, format="png", dpi=100)
	buf.seek(0)

	# png in memory to PIL image
	pil_image = Image.open(buf).convert('RGB')

	# PIL image to numpy BGR array
	open_cv_image = np.array(pil_image) 

	# Convert RGB to BGR 
	open_cv_image = open_cv_image[:, :, ::-1].copy() 	

	# close buffer and clear the figure
	buf.close()
	plt.clf()	
	plt.close()

	return open_cv_image
	

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'FMP4')
out = cv2.VideoWriter('/home/sbordt/Desktop/output.avi',fourcc, 100.0, (1920,1080))

for i in xrange(200):
    frame = gen_frame(i)
    print i
       
    # write the frame
    out.write(frame)

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()


