from tqdm import tqdm
from time import sleep

text = ""
for i in tqdm(range(100)):
    for char in ["a", "b", "c", "d"]:
        sleep(0.25)
        text = text + char