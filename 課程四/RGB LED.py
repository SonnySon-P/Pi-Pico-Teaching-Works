from machine import Pin, ADC, PWM
import time

# 初始化可變電阻的腳位
adcR = ADC(Pin(26))
adcG = ADC(Pin(27))
adcB = ADC(Pin(28))

# 設置RGB LED的腳位
pwmR = PWM(Pin(2))
pwmG = PWM(Pin(3))
pwmB = PWM(Pin(9))

# 設定PWM頻率
pwmR.freq(1000)
pwmG.freq(1000)
pwmB.freq(1000)

# 設定PWM占空比為0，指LED熄滅
pwmR.duty_u16(0)
pwmG.duty_u16(0)
pwmB.duty_u16(0)

# 主程式
while True:
    # 讀取每個可變電阻的ADC值，範圍介於0-65535
    rValue = adcR.read_u16()
    gValue = adcG.read_u16()
    bValue = adcB.read_u16()
    
    # 將ADC值映射到PWM佔空比，範圍介於0-65535
    pwmR.duty_u16(rValue)
    pwmG.duty_u16(gValue)
    pwmB.duty_u16(bValue)

    # 顯示RGB LED的當前顏色亮度
    print("Red:", rValue, "Green:", gValue, "Blue:", bValue)

    # 每100毫秒更新一次
    time.sleep(0.1)
