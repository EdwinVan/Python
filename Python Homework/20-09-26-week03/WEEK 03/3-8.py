# 3.8 tqdm Bar
# fyj

from tqdm import tqdm
from time import sleep

for i in tqdm(range(1,1000)):
    sleep(0.01)

