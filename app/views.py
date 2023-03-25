from django.shortcuts import render
from django.views import View
from .forms import AttendenceForm
import cv2
import time
import winsound
from .models import Attendenc
from datetime import date, datetime, timedelta
 

frequency = 2500
duration = 1000

# Create your views here.

class Home(View):
    def get(self, request):
        cap = cv2.VideoCapture(0)
        detect = cv2.QRCodeDetector()
        while True:
            _,img = cap.read()
            data, one, _=detect.detectAndDecode(img)
            if one is not None:
                if data:
                    cap.release()
                    data = data.split(', ')
                    name = str(data[0])
                    atten  = Attendenc.objects.filter(date__day = datetime.now().day)
                    if Attendenc.objects.filter(name=name, date__day = datetime.now().day).exists():
                        Attendenc.objects.filter(name=name).update(exit_time = datetime.now().time())
                        print('present', datetime.now().day, datetime.now().time())
                        winsound.Beep(duration,frequency)
                        time.sleep(1)
                        break
                    else:
                        print('adding new entry ++++++++present+++++++++')
                        p = Attendenc(name=name)
                        p.save()
                        winsound.Beep(duration, frequency)
                        time.sleep(1)
                        break
            #cv2.imshow('qrcodescanner app', img)
            if cv2.waitKey(1)==ord('q'):
                break
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return render(request, 'base.html',{'name':atten})
    
    def post(self, request):
        cap = cv2.VideoCapture(0)
        detect = cv2.QRCodeDetector()
        while True:
            _,img = cap.read()
            data, one, _=detect.detectAndDecode(img)
            if one is not None:
                if data:
                    cap.release()
                    data = data.split(', ')
                    name = str(data[0])
                    atten  = Attendenc.objects.filter(date__day = datetime.now().day)
                    if Attendenc.objects.filter(name=name, date__day = datetime.now().day).exists():
                        Attendenc.objects.filter(name=name).update(exit_time = datetime.now().time())
                        print('present', datetime.now().day, datetime.now().time())
                        winsound.Beep(duration,frequency)
                        time.sleep(1)
                        break
                    else:
                        print('adding new entry ++++++++present+++++++++')
                        p = Attendenc(name=name)
                        p.save()
                        winsound.Beep(duration, frequency)
                        time.sleep(1)
                        break
            #cv2.imshow('qrcodescanner app', img)
            if cv2.waitKey(1)==ord('q'):
                break
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return render(request, 'base.html',{'name':atten})