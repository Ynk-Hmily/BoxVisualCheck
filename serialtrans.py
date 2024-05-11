import serial
import serial.tools.list_ports
 
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
""" ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备。")
else:
    print("可用的串口设备如下：")
    for comport in ports_list:
        print(list(comport)[0], list(comport)[1]) """
def openRec():
    recCOM=serial.Serial(port="COM2",
                        baudrate=57600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_EVEN,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=0.5
                        )
    while True:
        word_rec=recCOM.read(5)
        if word_rec.decode("utf-8")=="ERR":
            recCOM.write("WRONG".encode("utf-8"))
            break
        else: 
            recCOM.write("TRUE".encode("utf-8"))
            break

    recCOM.close()

def correctSend(sendword):
    senCOM=serial.Serial(port="COM1",
                     baudrate=57600,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_EVEN,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0
                     )

    senCOM.write(sendword.encode('utf-8'))
    print("sent")
    senCOM.close()

def errorSend():
    senCOM=serial.Serial(port="COM1",
                     baudrate=57600,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_EVEN,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0
                     )
    sendword="ERR"
    senCOM.write(sendword.encode('utf-8'))
    senCOM.close()