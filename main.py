import cv2

cap = cv2.VideoCapture(0)

tracker = cv2.TrackerMOSSE_create()
# tracker = cv2.TrackerCRST_create()
ret, frame = cap.read()
bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame,bbox)

def drawBox(frame,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(frame,(x,y), ((x+w),(y+h)), (255,0,0), 3, 1)
    cv2.putText(frame, "Tracking", (70, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 50, 12), 2)


while True:
    timer = cv2.getTickCount()
    ret, frame = cap.read()

    ret,bbox = tracker.update(frame)   #bbox is a tuple
    if ret:
        drawBox(frame,bbox)
    else:
        cv2.putText(frame, "Object Lost", (75, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(frame, str(int(fps)), (75,50), cv2.FONT_HERSHEY_PLAIN, 1, (120,180,70), 2)
    cv2.imshow("Tracking",frame)

    if(cv2.waitKey(1) & 0xff==ord('q')):
        break