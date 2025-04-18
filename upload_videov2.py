import csv
import os

from datetime import datetime, timedelta

csv_file_path = 'df_shorts.csv'
save_path = 'posts'
start_date = datetime.strptime("20-04-2025", "%d-%m-%Y")

# CSV TO DICTIONARY
csv_data = []
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_data.append(row)

video_files = [f for f in os.listdir(save_path) if f.endswith('.mp4')]

for i, video_file in enumerate(video_files):
    if video_file.startswith("viddit_"):
        post_code = video_file.replace("viddit_", "").replace(".mp4", "")

        matching_row = next((row for row in csv_data if post_code in row['url']), None)

        if matching_row:
            title = matching_row['title']
            date_planned = (start_date + timedelta(days=i)).strftime('%d-%m-%Y')
            print(f"{video_file}  {title} Date: {date_planned}")

        else:
            print(f"{video_file} --> Title not found in CSV.")

