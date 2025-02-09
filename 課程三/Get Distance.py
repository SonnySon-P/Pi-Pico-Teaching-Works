from machine import Pin
import time

# 定義getDistance函數，作為HC-SR04驅動程式
def getDistance(trig, echo):
    # 初始化引腳
    trigPin = Pin(trig, Pin.OUT)
    echoPin = Pin(echo, Pin.IN)

    # 發送觸發信號
    trigPin.value(0)  # 設置trigPin為低電壓
    time.sleep_us(5)  # 等待5us
    trigPin.value(1)  # 設置trigPin為高電壓
    time.sleep_us(10)  # 等待10us，送出8個連續的40KHz超音波脈衝
    trigPin.value(0)  # 設置trigPin為低電壓

    # 測量反射波時間。這段代碼會一直持續運行，
    # 直到echoPin的值變為高電壓，即直到接收
    # 到從物體反射回來的超聲波訊號。
    while echoPin.value() == 0:
        pass  # 等待反射波訊號的到來

    pulseStart = time.ticks_us()  # 記錄反射波訊號開始的時間

    # 等待echoPin由高電壓變為低電壓，這表示反射波訊號結束
    while echoPin.value() == 1:
        pass  # 等待反射波訊號的結束

    pulseEnd = time.ticks_us()  # 記錄反射波訊號結束的時間

    # 計算反射波訊號的持續時間
    pulseDuration = time.ticks_diff(pulseEnd, pulseStart)
    
    # 計算距離(單位：cm)
    result = (pulseDuration / 2) / 29.1
    return result

while True:
    distance = getDistance(7, 6)  # trig連接到GPIO7、echo連接到GPIO6
    print("距離: {:.2f} cm".format(distance))
    time.sleep(1)