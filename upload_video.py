# https://www.youtube.com/watch?v=sp3qM2URcig
# OR JUST AN AUTO GUI UPLAODER: TAKE IN ACCOUNT::: PLANNING AND DATE!!

import pyautogui as qa
import time

import os
from datetime import datetime, timedelta


x = 1440
y = 900


url_upload = 'https://studio.youtube.com/channel/UCEj5MOUzOxZzPZdPLhBfnHg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D'
pc_name = ''
save_path = rf'C:\Users\{pc_name}\PycharmProjects\ShortAutoUploader\posts'
start_date = datetime.strptime("20-04-2025", "%d-%m-%Y")


video_files = sorted([f for f in os.listdir(save_path) if f.endswith(('.mp4', '.mov', '.avi'))])


# time.sleep(3)
# qa.click(0.7069 * x, 0.0711 * y)
# time.sleep(1)
# qa.typewrite(url_upload)
# time.sleep(2)
# qa.hotkey('ENTER')
# time.sleep(8)

for i, video_file in enumerate(video_files):
    file_name = os.path.splitext(video_file)[0]
    date_planned = (start_date + timedelta(days=i)).strftime('%d-%m-%Y')

    # start upload
    qa.click(0.9132 * x, 0.1289 * y)
    time.sleep(3)
    qa.click(0.8806* x, 0.1789 * y)
    time.sleep(2)

    qa.click(0.4917 * x, 0.4778 * y)
    time.sleep(5)
    qa.click(0.4414 * x, 0.0633 * y)
    time.sleep(1)
    qa.typewrite(save_path)
    time.sleep(1)
    qa.hotkey('ENTER')
    time.sleep(1)
    qa.click(0.44375 * x, 0.3633 * y)
    time.sleep(1)
    qa.typewrite(file_name)
    time.sleep(1)
    qa.hotkey('ENTER')
    time.sleep(2)
    qa.scroll(-1000)
    time.sleep(2)
    qa.click(0.20625 * x, 0.6055 * y)
    time.sleep(2)
    qa.click(0.7861 * x, 0.8611 * y)
    time.sleep(2)
    qa.click(0.7861 * x, 0.8611 * y)
    time.sleep(2)
    qa.click(0.7861 * x, 0.8611 * y)
    time.sleep(2)
    qa.click(0.2444 * x, 0.7222 * y)
    time.sleep(1)
    qa.click(0.2653 * x, 0.6344 * y)
    time.sleep(2)
    qa.hotkey('crtl', 'a')
    time.sleep(1)
    qa.typewrite(date_planned)
    time.sleep(2)
    qa.click(0.2444 * x, 0.7222 * y)
    time.sleep(12)
    qa.click(0.6361 * x, 0.6922 * y)
    time.sleep(2)
    # Start with new video

