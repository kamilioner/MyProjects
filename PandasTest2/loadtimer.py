import time
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

startm = int(round(time.time() * 1000))
nd = pd.read_csv('C:/Users/A660197/Downloads/checkval-history.csv', encoding = "ISO-8859-1")
stopm = int(round(time.time() * 1000))
a = (stopm - startm)



print('Loading time: ' + str(a))

print(nd.head(30))
