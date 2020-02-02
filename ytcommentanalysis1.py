import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


ac = pd.read_csv(r'C:\Users\sahil\Documents\nlpexercise\allcomments.csv', index_col=0)
print(ac.head(5))