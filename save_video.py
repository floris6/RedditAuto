import csv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from playsound3 import playsound



options = Options()
# options.add_argument("--disable-images")
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)


csv_file_path = 'df_shorts.csv'
save_path = 'posts'
successful_txt_path = os.path.join(save_path, 'posts_downloaded.txt')


with (open(successful_txt_path, 'w', encoding='utf-8') as success_log):
    success_log.write("Successful Downloads:\n")


    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            title = row[0]  # column 0 (title)
            url_post = row[4]  # column 4 (url)

            file_name = f"{title}"
            url = f'https://viddit.io/download?url={url_post}'

            driver.get(url)

            #
            try:
                download_link = WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//a[@class='btn download__item__info__actions__button']"))
                )
                if download_link:
                    href = download_link.get_attribute("href")
                    driver.get(href)
                    time.sleep(1)
                    success_log.write(f"{file_name}\n")

                else:
                    playsound("alert.mp3")
                    print(f'{file_name} FAILED to download!')
            except:
                pass

            # ERROR FILTER
            try:
                p_error = WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located((By.XPATH, "//img[@src='/images/not__found.svg']")))
                if p_error:
                    playsound("alert.mp3")
                    print(f"{file_name} -- Failed to Save\n\tPossible Error in the reddit VIDEO (not downloadable)")
                    time.sleep(2)
                    driver.get(url)
            except:
                pass



driver.quit()
