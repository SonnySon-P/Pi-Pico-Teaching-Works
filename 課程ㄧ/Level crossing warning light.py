from machine import Pin
import time

# 設定兩個燈泡的GPIO引腳，使用GPIO 14和GPIO 15
bulb1 = Pin(5, Pin.OUT)
bulb2 = Pin(9, Pin.OUT)

while True:
    # 讓燈泡1開啟，燈泡2關閉
    bulb1.on()
    bulb2.off()
    time.sleep(1)  # 延遲1秒

    # 讓燈泡1關閉，燈泡2開啟
    bulb1.off()
    bulb2.on()
    time.sleep(1)  # 延遲1秒