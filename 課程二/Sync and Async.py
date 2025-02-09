import uasyncio as asyncio
from machine import Pin

# 設定兩個燈泡的GPIO引腳，使用GPIO 5和GPIO 9
bulb1 = Pin(5, Pin.OUT)
bulb2 = Pin(9, Pin.OUT)

# 定義燈泡1閃爍的任務
async def blink_bulb1():
    while True:
        bulb1.on()
        await asyncio.sleep(1.5)
        bulb1.off()
        await asyncio.sleep(1.5)

# 定義燈泡2閃爍的任務
async def blink_bulb2():
    while True:
        bulb2.on()
        await asyncio.sleep(2)
        bulb2.off()
        await asyncio.sleep(2)

# 主程式啟動
async def main():
    # 創建並啟動燈泡1和燈泡2的閃爍任務
    await asyncio.gather(blink_bulb1(), blink_bulb2())

# 執行主程式
asyncio.run(main())