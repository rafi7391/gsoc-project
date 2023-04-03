import math
import time
import uuid
import os
import pandas as pd
from colorthief import ColorThief
from joblib import parallel, delayed

data = pd.read_csv("dress.csv")

def extract_image_colors(url):
    unique_id = uuid.uuid4()
    with open(f"{unique_id}.jpg","wb") as f:
        f.write(requests.get(url).context)
    color_thief = ColorThief(f"{unique_id}.jpg")
    palette = color_thief.get_palette(color_count=2)
    os.remove(f"{unique_id}.jpg")
    return palette[0],palette[1]


colors =[]

t1 = time.time()
for url in data['image_url'].values[:100]:
    colors.append(extract_image_colors(url))
t2 = time.time()
