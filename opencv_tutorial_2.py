import cv2


cam = cv2.VideoCapture(0) # 0 is device number: the laptop's webcam, 1 for usb cam

# This is for the camera to stabilize (Take the fiftieth frame)
for _ in range(50):
    ret, firstFrame = cam.read()
    firstFrame = cv2.cvtColor(firstFrame,cv2.COLOR_BGR2GRAY)
 

while(True):
    isReturned, image = cam.read() # captures camera
    rgb = image
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	
    diff = cv2.absdiff(image, firstFrame)
    _, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY) # 50-255 it will convert to zero
	
	# We want to find the contours of the white blobs
    _, cnts,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	# cnts: Array storing the points of a contour
	
    # cv2.drawContours(rgb, cnts, -1, (255, 0, 0), 2) # Blue Color, Line Width = 2
	
	# Doing Dilation: Morphological change
	
    for c in cnts:
        if(cv2.contourArea(c)<100):
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(rgb, (x,y), (x+w, y+h), (0, 0, 255), 2)
        # cv2.drawContours(rgb, c, -1, (255, 0, 0), 2) 
	    
	
    cv2.imshow('Diff VideoFeed', diff)
    cv2.imshow('Thresh VideoFeed', thresh)
    cv2.imshow('Image VideoFeed', rgb)
	
	# Further using Dilation (Morphology techniques), you can reduce the noise.
	
    if(cv2.waitKey(1)==ord('q')): # Why 1, why ord?
        break
		
		
# Applications: Object Tracking: Subtract Image from initial image to get the image part which is moving.
# Non moving part will be zero (black). 		
# So we threshold, since we care only about zero and non-zero.		
		
# Important to release the camera object
cam.release()

# cv2.waitKey(0)
cv2.destroyAllWindows()