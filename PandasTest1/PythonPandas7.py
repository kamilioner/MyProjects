import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('c:/Users/A660197/PycharmProjects/kpiquandl.txt', 'r').read()

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df['United States                  not seasonally adjusted'] = (df['United States                  not seasonally adjusted'] - df['United States                  not seasonally adjusted'][0]) / df['United States                  not seasonally adjusted'][0] * 100.0

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for i in states:
        query = ('FMAC/HPI_' + str(i))
        df = quandl.get(query, authtoken=api_key)
        df = df.rename(columns={'Value':i})
        df[i] = (df[i] - df[i][0])/df[i][0]*100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

#grab_initial_state_data()

# pickle_in = open('fiddy_states.pickle','rb')
# HPI_data = pickle.load(pickle_in)
# print(HPI_data)

# HPI_data.to_pickle('pandas_pickle.pickle')


HPI_data = pd.read_pickle('fiddy_states3.pickle')
#print(HPI_data)

# HPI_data['TX2'] = HPI_data['TX'] * 2
# print(HPI_data['TX2'])



HPI_data.plot()
plt.legend().remove()
plt.show()

