import time
from machine import Pin

# 定義readKeypad函數，作為Keypad驅動程式
def readKeypad(R1, R2, R3, R4, C1, C2, C3, C4):
    # 設定行和列引腳
    rows = [Pin(R1, Pin.OUT), Pin(R2, Pin.OUT), Pin(R3, Pin.OUT), Pin(R4, Pin.OUT)]
    cols = [Pin(C1, Pin.IN, Pin.PULL_UP), Pin(C2, Pin.IN, Pin.PULL_UP), Pin(C3, Pin.IN, Pin.PULL_UP), Pin(C4, Pin.IN, Pin.PULL_UP)]

    # 設置按鍵數值
    Keys = [
                ["1", "2", "3", "A"],
                ["4", "5", "6", "B"],
                ["7", "8", "9", "C"],
                ["*", "0", "#", "D"]
            ]

    # 檢測按鍵
    for r in range(4):  # 遍歷row
        rows[r].value(0)  # 將當前row設置為低電平
        for c in range(4):  # 遍歷col
            if cols[c].value() == 0:  # 當col的值為低電平時
                rows[r].value(1)  # 將row設為高電平，恢復行狀態
                return Keys[r][c]  # 返回對應的按鍵
        rows[r].value(1)  # 將當前row設置為高電平，準備下一行檢測
    return None  # 如果沒有按鍵被按下，返回None

while True:
    output = readKeypad(0, 1, 2, 3, 9, 10, 11, 12)
    if output != None:
        print(f"按下的鍵是: {output}")
    time.sleep(0.1)  # 防止太頻繁按壓按鍵