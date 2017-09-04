import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import win32api
import os
from matplotlib.cbook import get_sample_data


def pcc(kk_filename):
    user_dataframe = pd.read_csv('./ActivityData/' + kk_filename, header=None, names=['ActivityTime', 'x_pos', 'y_pos'])
    user_dataframe.dropna(how='any', inplace=True)

    user_dataframe.x_pos = pd.to_numeric(user_dataframe.x_pos.str.replace('(', ''))
    user_dataframe.y_pos = pd.to_numeric(user_dataframe.y_pos.str.replace(')', ''))

    # print(user_dataframe.shape)

    MonitorPart = []
    monitors = win32api.EnumDisplayMonitors()

    main_monitor = 0

    for i in range(len(monitors)):
        if (monitors[i][2][0] == 0) and (monitors[i][2][1] == 0):
            main_monitor = i

    # print(main_monitor)

    Q1 = []
    Q2 = []
    Q3 = []
    Q4 = []
    Q5 = []
    Q6 = []
    Q7 = []
    Q8 = []
    Q9 = []
    Q10 = []
    Q11 = []
    Q12 = []
    Q13 = []
    Q14 = []
    Q15 = []
    Q16 = []

    # for i in range(len(monitors)):
    monitor_corner = monitors[main_monitor][2]
    a = monitor_corner[0]
    b = monitor_corner[1]
    c = monitor_corner[2]
    d = monitor_corner[3]
    Q1.append((a, b, 0.25 * c + a, 0.25 * (d - b) + b))
    Q2.append(((c - a) * 0.25 + a + 0.1, b, (c - a) * 0.5 + a, 0.25 * (d - b) + b))
    Q3.append(((c - a) * 0.5 + a + 0.1, b, (c - a) * 0.75 + a, 0.25 * (d - b) + b))
    Q4.append(((c - a) * 0.75 + a + 0.1, b, c, 0.25 * (d - b) + b))
    Q5.append((a, (d - b) * 0.25 + b + 0.1, (c - a) * 0.25 + a, 0.5 * (d - b) + b))
    Q6.append(((c - a) * 0.25 + a + 0.1, (d - b) * 0.25 + b + 0.1, (c - a) * 0.5 + a, 0.5 * (d - b) + b))
    Q7.append(((c - a) * 0.5 + a + 0.1, (d - b) * 0.25 + b + 0.1, (c - a) * 0.75 + a, 0.5 * (d - b) + b))
    Q8.append(((c - a) * 0.75 + a + 0.1, (d - b) * 0.25 + b + 0.1, c, 0.5 * (d - b) + b))
    Q9.append((a, (d - b) * 0.5 + b + 0.1, (c - a) * 0.25 + a, 0.75 * (d - b) + b))
    Q10.append(((c - a) * 0.25 + a + 0.1, (d - b) * 0.5 + b + 0.1, (c - a) * 0.5 + a, 0.75 * (d - b) + b))
    Q11.append(((c - a) * 0.5 + a + 0.1, (d - b) * 0.5 + b + 0.1, (c - a) * 0.75 + a, 0.75 * (d - b) + b))
    Q12.append(((c - a) * 0.75 + a + 0.1, (d - b) * 0.5 + b + 0.1, c, 0.75 * (d - b) + b))
    Q13.append((a, (d - b) * 0.75 + b + 0.1, (c - a) * 0.25 + a, d))
    Q14.append(((c - a) * 0.25 + a + 0.1, (d - b) * 0.75 + b + 0.1, (c - a) * 0.5 + a, d))
    Q15.append(((c - a) * 0.5 + a + 0.1, (d - b) * 0.75 + b + 0.1, (c - a) * 0.75 + a, d))
    Q16.append(((c - a) * 0.75 + a + 0.1, (d - b) * 0.75 + b + 0.1, c, d))

    # MonitorPart.append([monitors[i][2][0], monitors[i][2][1], monitors[i][2][2], monitors[i][2][3]])

    MonitorPart.append(Q1)
    MonitorPart.append(Q2)
    MonitorPart.append(Q3)
    MonitorPart.append(Q4)
    MonitorPart.append(Q5)
    MonitorPart.append(Q6)
    MonitorPart.append(Q7)
    MonitorPart.append(Q8)
    MonitorPart.append(Q9)
    MonitorPart.append(Q10)
    MonitorPart.append(Q11)
    MonitorPart.append(Q12)
    MonitorPart.append(Q13)
    MonitorPart.append(Q14)
    MonitorPart.append(Q15)
    MonitorPart.append(Q16)

    Q = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # print(MonitorPart)
    for q in range(16):
        for i in range(len(MonitorPart[0])):
            Q[q] += len(user_dataframe.loc[
                        (user_dataframe['x_pos'] >= MonitorPart[q][i][0]) & (user_dataframe['x_pos'] < MonitorPart[q][i][2]) & (
                        user_dataframe['y_pos'] >= MonitorPart[q][i][1]) & (user_dataframe['y_pos'] < MonitorPart[q][i][3]), :].index)
    # print(Q)
    return Q


data_list = []

for f_name in os.listdir("./ActivityData/"):
    if f_name.endswith(".txt"):
        data_list.append((pcc(f_name)))

# filename2 = 'kk.txt'
#
N = 16
colors = ['r', 'b', 'g', 'y', '#2f470d', '#d6b9cf', '#53c99e', '#724c02', '#5c25a0', '#f01943', '#69de06', '#6fdd66', '#a49bf9', '#0b881f',
          '#683d92', '#0f7f9e', '#db5d2f', '#d2c01b', '#6f9ca3', '#8d1ccd', '#be7aca', '#2cee90', '#799235', '#15b680', '#47698e',
          '#925cc0', '#c201bb', '#84ffa2', ]

ind = np.arange(N)  # the x locations for the groups
width = 0.12  # the width of the bars

fig, ax = plt.subplots()

for i in range(len(data_list)):
    rects = ax.bar(ind + i * width, data_list[i], width, color=colors[i])
#
# user2_aph = (aph(filename2))
# #(500, 600, 700, 150, 250)
# rects2 = ax.bar(ind + width, user2_aph, width, color='g')
#
# user3_aph = (250, 300, 50, 800, 25)
# rects3 = ax.bar(ind + 2 * width, user3_aph, width, color='b')
#
# # add some text for labels, title and axes ticks
ax.set_ylabel('Number of clicks in particular screen part')
ax.set_title('Performance')
ax.set_xticks(ind + width / 10)
ax.set_xticklabels(('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16'))
#
# ax.legend('./Screen.png')
im = plt.imread(get_sample_data('c:/Users/A660197/PycharmProjects/MyProjects/ActivityChecker/Screen - Copy.bmp'))

newax = fig.add_axes([0.8, 0.8, 0.2, 0.2], anchor='NE', zorder=1)
newax.imshow(im)
newax.axis('off')
#
plt.show()
