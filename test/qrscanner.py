import cv2
import webbrowser
import time
import winsound
import openpyxl
import pandas as pd

frequency = 2500 
duration = 1000

# wb = openpyxl.Workbook()
# ws = wb.active




cap = cv2.VideoCapture(0)
detect = cv2.QRCodeDetector()
name = 'rudra'
data_set = {'name':name}
while True:
    _,img= cap.read()
    data,one, _=detect.detectAndDecode(img)
    if data:
        a=data
        a = a.split(", ")
        s_name = a[0]
        if s_name == data_set['name']:
            print(a)
            winsound.Beep(frequency, duration)
            time.sleep(3)
        else:
            continue
    cv2.imshow('qrcodescanner app', img)
    if cv2.waitKey(1)==ord('q'):
        break


# b = webbrowser.open(str(a))
# cap.release(a)
#cv2.destroyAllWindows()