import pandas as pd
import numpy as np
import random

names = [f'Person_{i+1}' for i in range(100)]
activities = ['Reading', 'Exercise', 'Coding', 'Social Media', 'Group Study', 'Gaming', 'TV', 'Walking', 'Cooking', 'Meditation']
dates = pd.date_range(start='2025-10-01', periods=7)

rows = []
for name in names:
    for date in dates:
        for _ in range(random.randint(3, 7)):
            start_hour = random.randint(6, 22)
            start_minute = random.choice([0, 15, 30, 45])
            duration = random.choice([30, 45, 60, 90])
            start_time = f'{start_hour:02d}:{start_minute:02d}'
            end_hour = start_hour + duration // 60
            end_minute = start_minute + duration % 60
            if end_minute >= 60:
                end_hour += 1
                end_minute -= 60
            if end_hour > 23:
                end_hour = 23
                end_minute = 59
            end_time = f'{end_hour:02d}:{end_minute:02d}'
            activity = random.choice(activities)
            //note = f'Auto-generated {activity.lower()} activity'
            rows.append([name, str(date.date()), start_time, end_time, activity, duration, note])

columns = ['Person', 'Date', 'Start Time', 'End Time', 'Activity', 'Duration (minutes)', 'Notes']
df = pd.DataFrame(rows, columns=columns)
df.head(10).to_csv('free_time_sample.csv', index=False)
df.shape
print(df)