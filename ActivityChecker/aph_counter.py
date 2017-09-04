import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os



def aph(file_name):
    user_dataframe = pd.read_csv('./ActivityData/'+file_name, header=None, names=['ActivityTime', 'x_pos', 'y_pos'])
    user_dataframe_mouse = user_dataframe.copy()
    user_dataframe_mouse.dropna(how='any', inplace=True)
    user_dataframe = user_dataframe[pd.isnull(user_dataframe.x_pos)]

    user_dataframe['ActivityTime'] = pd.to_datetime(user_dataframe['ActivityTime'])
    user_dataframe['Hour'] = user_dataframe['ActivityTime'].dt.hour
    aph_template = pd.Series(0, index=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    user_dataframe_mouse.drop(['x_pos', 'y_pos'], axis=1, inplace=True)
    user_dataframe_mouse['ActivityTime'] = pd.to_datetime(user_dataframe_mouse['ActivityTime'])
    user_dataframe_mouse['Hour'] = user_dataframe_mouse['ActivityTime'].dt.hour

    aph_by_hour_mouse = user_dataframe_mouse['Hour'].value_counts().sort_index()
    aph_by_hour = user_dataframe['Hour'].value_counts().sort_index()
    aph_by_hour = aph_by_hour / 2

    result = aph_template.add(aph_by_hour, fill_value=0).add(aph_by_hour_mouse, fill_value=0)

    timestamp_aph1 = ((result[8]) + (result[9])) / 2
    timestamp_aph2 = ((result[10]) + (result[11])) / 2
    timestamp_aph3 = ((result[12]) + (result[13])) / 2
    timestamp_aph4 = ((result[14]) + (result[15])) / 2
    timestamp_aph5 = ((result[16]) + (result[17])) / 2

    return[timestamp_aph1, timestamp_aph2, timestamp_aph3, timestamp_aph4, timestamp_aph5]

N = 5
colors = ['r', 'b', 'g', 'y', '#2f470d', '#d6b9cf', '#53c99e', '#724c02', '#5c25a0', '#f01943', '#69de06', '#6fdd66', '#a49bf9', '#0b881f', '#683d92', '#0f7f9e', '#db5d2f', '#d2c01b', '#6f9ca3', '#8d1ccd', '#be7aca', '#2cee90', '#799235', '#15b680', '#47698e', '#925cc0', '#c201bb', '#84ffa2',]
data_list = []

for f_name in os.listdir("./ActivityData/"):
    if f_name.endswith(".txt"):
        data_list.append((aph(f_name)))


ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
fig, ax = plt.subplots()

for i in range(len(data_list)):
    rects = ax.bar(ind + i * width, data_list[i], width, color=colors[i])


ax.set_ylabel('Average clicks per hour')
ax.set_title('Performance')
ax.set_xticks(ind + width/10)
ax.set_xticklabels(('8:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00', '16:00-18:00'))

#ax.legend((rects1[0], rects2[0], rects3[0]), ('KK', 'User2', 'User3'))

plt.show()