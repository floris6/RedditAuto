import os

from datetime import datetime, timedelta

import pyautogui as qa
import time

time.sleep(2)

csv_path = 'df_shorts.csv'
pc_name = 'osmbo'
save_path = rf'C:\Users\{pc_name}\PycharmProjects\ShortAutoUploader\posts'

yt_title = 'Wait for it...😂'


x = 2048
y = 1152


def refresh():
    yt_url_up = 'https://studio.youtube.com/'

    time.sleep(2)
    qa.hotkey('ctrl' + 't')
    time.sleep(1)
    qa.typewrite(yt_url_up)
    qa.hotkey('ENTER')
    time.sleep(20)

start_date = datetime.strptime("01-07-2025", "%d-%m-%Y")


video_files = sorted([f for f in os.listdir(save_path) if f.endswith(('.mp4'))])

for i, video_file in enumerate(video_files):
    file_name = os.path.splitext(video_file)[0]
    find_video = rf"{save_path}\{file_name}"
    date_planned = (start_date + timedelta(days=i)).strftime('%d-%m-%Y')

    time.sleep(3)
    qa.click(0.9132 * x, 0.1289 * y)
    time.sleep(1)
    qa.click(0.8806* x, 0.1789 * y)
    time.sleep(2)

    qa.click(0.4917 * x, 0.4778 * y)
    time.sleep(4)
    qa.typewrite(find_video)
    time.sleep(1)
    qa.hotkey('ENTER')
    time.sleep(10)


    qa.scroll(-100000)
    time.sleep(1)
    qa.click(0.2437 * x, 0.6137 * y)
    time.sleep(2)
    qa.click(0.7476 * x, 0.8672 * y)
    time.sleep(2)
    qa.click(0.7476 * x, 0.8672 * y)
    time.sleep(10)
    qa.click(0.7476 * x, 0.8672 * y)
    time.sleep(1)

    # PLANNING
    qa.click(0.2593 * x, 0.7118 * y)
    time.sleep(1)
    qa.click(0.2905 * x, 0.6181 * y)
    time.sleep(2)
    qa.hotkey('ctrl', 'a')
    time.sleep(1)
    qa.typewrite(date_planned)
    time.sleep(2)
    qa.hotkey('ENTER')
    time.sleep(2)
    qa.click(0.7476 * x, 0.8672 * y)

    time.sleep(30)
    qa.click(0.6191 * x, 0.6753 * y)

    # Delete uploaded file
    try:
        os.remove(fr'posts\{file_name}.mp4')
        print(f"Deleted: {video_file}")
    except Exception as e:
        print(f"Failed to delete {video_file}: {e}")

    copy_file_name = file_name.replace('viddit_', '')
    print(f'{copy_file_name} -- {i + 1}. {file_name} Uploaded for: {date_planned}')

