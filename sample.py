from tqdm import tqdm
from time import sleep

text = ""
l = tqdm(iterable=range(100), colour='blue')
for i in l:
    sleep(0.25)
    # l.write('loop ', i)