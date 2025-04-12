import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pyautogui as qa

import os


# Required data
x = 1440
y = 900
pc_name = 'name'


url_ratio = 'https://www.fileconverto.com/video-aspect-ratio/'
save_path = rf'C:\Users\{pc_name}\PycharmProjects\ShortAutoUploader\posts'
csv_file_path = 'df_shorts.csv'


options = Options()
driver = webdriver.Chrome(options=options)


with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for row in reader:
        title = row[0]  # column 0 (title)
        url_post = row[4]  # column 4 (url)
        file_name = f"{reader.line_num}. {title}"

        search_path = rf'{save_path}\{file_name}'
        video_path = f'{save_path}/{file_name}.mp4'


        driver.get(url_post)
        time.sleep(10)


        # Download from REDDIT
        qa.rightClick(0.2868 * x, 0.5267 * y)
        time.sleep(1)
        qa.moveTo(0.3306 * x, 0.6922 * y, 1)
        time.sleep(1)
        qa.click()
        time.sleep(4)
        qa.click(0.4514 * x, 0.0633 * y)
        time.sleep(1)
        qa.typewrite(save_path)
        time.sleep(1)
        qa.hotkey('ENTER')
        time.sleep(2)
        qa.click(0.5757 * x, 0.3311 * y)
        time.sleep(1)
        qa.typewrite(file_name)
        time.sleep(1)
        qa.hotkey('ENTER')

        time.sleep(10)

        if os.path.exists(video_path):
            print(f"{file_name}-- Succesfull")

        else:
            print(f"{file_name}-- Failed to download")



driver.quit()
