#导入基本库
import pyautogui
import time
from datetime import datetime
import threading
from pynput import mouse

prompts = '点击获取基本位置后输入你需要执行的时间 然后点击执行来准备执行操作'
#文本框内容转换
def PChange(pnum):
    global prompts
    if pnum == 100:
        #初始
        prompts = '点击获取基本位置后输入你需要执行的时间 然后点击执行来准备执行操作'
        #获取输入框位置期间
    elif pnum == 101:
            prompts = '请点击你的鼠标左键到微信的输入框上'
        #获取发送按钮位置期间
    elif pnum == 102:
            prompts = '请点击你的鼠标左键到微信的发送按钮上'
    else:
        prompts = '点击获取基本位置后输入你需要执行的时间 然后点击执行来准备执行操作'

#获取基本鼠标位置
sendPx = 0
sendPy = 0
inputPx = 0
inputPy = 0
def gP():
    global sendPx, sendPy, inputPx, inputPy
    #如果左键按下则获取鼠标位置
    PChange(101)
    if pyautogui.mouseDown():
        inputPx, inputPy = pyautogui.position()
    # 如果左键按下则获取鼠标位置
    PChange(102)
    if pyautogui.mouseDown():
        sendPx, sendPy = pyautogui.position()
    PChange(100)
    print(inputPx, inputPy, sendPx, sendPy)


#验证输入的时间是否正确(格式应为: 年/月/日/时/分/秒(年月日可省略 时分秒若早于当前时间则自动转为明天),输入框变量为date)

#导入基本库
import pyautogui
import time
from datetime import datetime
import threading
from pynput import mouse

prompts = '点击获取基本位置后输入你需要执行的时间 然后点击执行来准备执行操作'
#文本框内容转换
def PChange(pnum):
    global prompts
    prompt_dict = {
        100: '点击获取基本位置后输入你需要执行的时间，然后点击执行来准备执行操作',
        101: '请点击你的鼠标左键到微信的输入框上',
        102: '请点击你的鼠标左键到微信的发送按钮上'
    }
    prompts = prompt_dict.get(pnum, '点击获取基本位置后输入你需要执行的时间，然后点击执行来准备执行操作')

#获取基本鼠标位置
sendPx = 0
sendPy = 0
inputPx = 0
inputPy = 0
def gP():
    global sendPx, sendPy, inputPx, inputPy

    def on_click(x, y, button, pressed):
        if pressed:
            PChange(101)
            if prompts == '请点击你的鼠标左键到微信的输入框上':
                nonlocal inputPx, inputPy
                inputPx, inputPy = x, y
            PChange(102)
            if prompts == '请点击你的鼠标左键到微信的发送按钮上':
                nonlocal sendPx, sendPy
                sendPx, sendPy = x, y
            PChange(100)

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    print(inputPx, inputPy, sendPx, sendPy)



#验证输入的时间是否正确(格式应为: 年/月/日/时/分/秒(年月日可省略 时分秒若早于当前时间则自动转为明天),输入框变量为date)



    #按下执行后执行代码
    def execute_code():
        #需要执行的内容 在指定时间复制内容到剪切板 粘贴到输入框(inputPx, inputPy)中 然后左键单击发送(sendPx, sendPy)
        print("执行代码")



    #按下执行后执行代码
    def execute_code():
        #需要执行的内容 在指定时间复制内容到剪切板 粘贴到输入框(inputPx, inputPy)中 然后左键单击发送(sendPx, sendPy)
        print("执行代码")


