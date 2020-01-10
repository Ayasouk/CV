import cv2
import math


def capture():
    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
        ret,frame = cap.read()
        print(frame)
        color = [0,0,255]
        nearest_pix = (0,0)
        min_dist = color_distance(frame[0][0],color)
        for i in range(0,len(frame)):
            for j in range(0,len(frame[i])):
                cur_dist = color_distance(frame[i][j],color)
                if cur_dist < min_dist:
                    nearest_pix = (i,j)
                
        cv2.circle(frame, nearest_pix, 10, color)
        if ret==True:
            cv2.imshow('fr',frame)
            cv2.waitKey()
        else:
            break

    cap.release()

    cv2.destroyAllWindows()

def color_distance(pix1,pix2):
    dist = 0
    for i in range(len(pix1)):
        dist += math.sqrt((pix1[i]-pix2[i])**2)

    return dist
