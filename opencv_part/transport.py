import socket
import cv2
import io
from PIL import Image
import numpy as np
import threading
import random

from . import CV_Globals







def rec():
    receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    receive.bind(("0.0.0.0", 9090))#绑定接收端口 
    
    
    while True:
        capture=CV_Globals.get_capture_val()
        print(capture)
        data, IP = receive.recvfrom(100000)
        
        bytes_stream = io.BytesIO(data)
        image = Image.open(bytes_stream)
        img = np.asarray(image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # ESP32采集的是RGB格式，要转换为BGR（opencv的格式）
        cv2.imshow("ESP32 Capture Image", img)
        
        if cv2.waitKey(5) == ord("q"):
            break
        #elif cv2.waitKey(1)==ord("w"):
             #imgPath="./trans.jpg"
             #cv2.imwrite(imgPath,img)
         
        elif capture:
                
                print("saved")
                imgPath="./Pictures/cachesPic.jpg"
                
                cv2.imwrite(imgPath,img)
                CV_Globals.set_capture_val(False)
                #cv2.waitKey(1)
                continue
        else :continue
    cv2.destroyAllWindows()   
    receive.close()

def sen():
        send =socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
        try:
            send.sendto(b"start",("192.168.162.196",9091))
            print("sent")

        finally:
            send.close()
          
               
            

       






#rec_thread.start()
#send_thread.start()

#rec_thread.join()
#send_thread.join() 