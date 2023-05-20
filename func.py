# 导入基本库

import pyautogui

import time

from datetime import datetime

import threading

from pynput import mouse

prompts = '点击获取基本位置后输入你需要执行的时间，然后点击执行来准备执行操作'

# 文本框内容转换

def PChange(pnum):

    global prompts

    prompt_dict = {

        100: '点击获取基本位置后输入你需要执行的时间，然后点击执行来准备执行操作',

        101: '请点击你的鼠标左键到微信的输入框上',

        102: '请点击你的鼠标左键到微信的发送按钮上'

    }

    prompts = prompt_dict.get(pnum, '点击获取基本位置后输入你需要执行的时间，然后点击执行来准备执行操作')

# 获取基本鼠标位置

sendPx = 0

sendPy = 0

inputPx = 0

inputPy = 0

def gP():

    global sendPx, sendPy, inputPx, inputPy

    def on_click(x, y, button, pressed):

        if pressed:

            if prompts == '请点击你的鼠标左键到微信的输入框上':

                nonlocal inputPx, inputPy

                inputPx, inputPy = x, y

                PChange(102)

            elif prompts == '请点击你的鼠标左键到微信的发送按钮上':

                nonlocal sendPx, sendPy

                sendPx, sendPy = x, y

                PChange(100)

            elif prompts == '点击获取基本位置后输入你需要执行的时间，然后点击执行来准备执行操作':

                pass

    with mouse.Listener(on_click=on_click) as listener:

        listener.join()

    print(inputPx, inputPy, sendPx, sendPy)

# 验证输入的时间是否正确(格式应为: 年/月/日/时/分/秒，年月日可省略，时分秒若早于当前时间则自动转为明天)，输入框变量为date

def validate_time(date):

    now = datetime.now()

    try:

        user_time = datetime.strptime(date, '%Y/%m/%d/%H/%M/%S')

        if user_time < now:

            user_time = user_time.replace(day=user_time.day + 1)

        return user_time

    except ValueError:

        return None

# 按下执行后执行代码

def execute_code():

    # 需要执行的内容：在指定时间复制内容到剪贴板，粘贴到输入框(inputPx, inputPy)中，然后左键单击发送(sendPx, sendPy)

    print("执行代码")

# 主程序

if __name__ == '__main__':

    while True:

        print(prompts)

        user_input = input("请输入操作编号或时间（回车以继续）：")

        

        if user_input.isdigit():

            PChange(int(user_input))

        elif user_input:

            execution_time = validate_time(user_input)

            if execution_time:

                current_time = datetime.now()

                time_difference = (execution_time - current_time).total_seconds()

                if time_difference > 0:

                    print("等待时间到达...")

                    time.sleep(time_difference

