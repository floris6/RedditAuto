# Scrape posts and place data in pandas dataframe --> download to csv of sql query (than db)
# csv file = input for second .py file: download video's upload to buffer (yt, tiktok)

# scrape file when running: scheduled on pa: scrapes 20 top posts from that week and updates table

# exe file: add new scrape session: creates table at pythonanywhere (store data) -> start . update row when finished

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

url = 'https://www.reddit.com/r/Unexpected/top/?t=all&feedViewType=compactView'

options = Options()
driver = webdriver.Chrome(options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))



scroll_pause_time = 5  # seconds to wait after each scroll
num_batches = 20  # * 25 video titles


posts_dict = {}

for _ in range(num_batches):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    shreddit_posts = soup.find_all('shreddit-post')
    for post in shreddit_posts:
        permalink = post.get('permalink')

        if permalink and permalink not in posts_dict:
            duration_span = post.find('span', class_='font-semibold text-10 ml-2xs truncate')
            duration = duration_span.text if duration_span else None

            # SUBREDDIT SPECIFIC!
            content_tag_a = post.find('a',
                                      href='/r/Unexpected/?f=flair_name%3A%22%F0%9F%94%9E%20Warning%3A%20Graphic%20Content%20%F0%9F%94%9E%22')
            if content_tag_a:
                content_tag = 'TRUE'
            else:
                content_tag = 'FALSE'
            data = {
                'title': post.get('post-title'),
                'post_type': post.get('post-type'),
                'author': post.get('author'),
                'permalink': permalink,
                'url': post.get('content-href'),
                'created_timestamp': post.get('created-timestamp'),
                'duration': duration,
                'content_tag': content_tag
            }
            posts_dict[permalink] = data

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))

driver.quit()

posts_data = list(posts_dict.values())
# for i, post in enumerate(posts_data, 1):
#     print(f"{i}. {post['duration']} {post['title']} ({post['content_tag']})")








import pandas as pd
import re

df = pd.DataFrame(posts_data)

def convert_duration_to_seconds(duration):
    if duration:
        match = re.match(r'(\d+):(\d+)', duration)
        if match:
            minutes = int(match.group(1))
            seconds = int(match.group(2))
            total_seconds = minutes * 60 + seconds
            return total_seconds
        else:
            return None
    return None


df['duration_seconds'] = df['duration'].apply(convert_duration_to_seconds)
df_filtered = df[(df['duration_seconds'] >= 1) & (df['duration_seconds'] <= 59)]
df_filtered = df_filtered.drop(columns=['duration_seconds'])

df_filtered = df_filtered[df_filtered['content_tag'] != 'TRUE']

pd.set_option('display.max_rows', None)
print(df_filtered)





# SAVE TO CSV FILE
df_filtered.to_csv('df_shorts.csv', index=False)


# ADD QUERY
# line 1: table_name(vars)
# for loop to add all data
