import quandl
import pandas as pd

api_key = open('c:/Users/A660197/PycharmProjects/kpiquandl.txt', 'r').read()

#df = quandl.get("FMAC/HPI_AK", authtoken=api_key)

#print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#print(fiddy_states[0][0])

for i in fiddy_states[0][0][1:]:
    print('FMAC/HPI_' + str(i))