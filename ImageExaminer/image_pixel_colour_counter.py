import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt


def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

im = Image.open("tapeta.bmp")  #Can be many different formats.

color_list = []
color_list_numbers = []
number_of_pixels = 0

# x = 0
# y = 0

pix = im.load()

#print(im.size) #Get the width and hight of the image for iterating over


for x in range(im.size[0]):
    for y in range(im.size[1]):
        color_list.append(pix[x, y])
        number_of_pixels += 1

#pd_list_of_colours = pd.DataFrame([color_list], columns=['R', 'G', 'B', 'counter'])
pd_list_of_colours = pd.Series(color_list, name='Color')
Series_value_count = pd_list_of_colours.value_counts(normalize=True)
# df_value_count = pd_list_of_colours.value_counts(normalize=True).plot(kind='bar')
Series_value_count = Series_value_count.head(50)
df_value_count = Series_value_count.to_frame(name='Color percentage')
df_value_count.reset_index(level=0, inplace=True)
df_value_count.rename(columns={'index': 'Colors'}, inplace=True)
#df_value_count[['R', 'G', 'B']] = df_value_count['Colors'].apply(pd.Series)
#df_value_count['Hex_color_value'] = (df_value_count.R, df_value_count.G, df_value_count.B)

my_list = df_value_count.values.tolist()

# print(df_value_count)
# print(my_list)
list_of_bars_colors = []

for i in range(len(my_list)):
    list_of_bars_colors.append(rgb_to_hex(my_list[i][0][0], my_list[i][0][1], my_list[i][0][2]))

# print(list_of_bars_colors)
# print(df_value_count.iloc[:])
# print(pix[x,y]) #Get the RGBA Value of the a pixel of an image
# value = pix[x,y] # Set the RGBA Value of the image (tuple)
# print(value)

# print(number_of_pixels)
# print(len(color_list))
# print(df_value_count)
#print(list(set(color_list)))
#print(pd_list_of_colours.groupby(['R','G','B'])['counter'].mean())


df_value_count.set_index('Colors', inplace=True)
df_value_count.plot(kind='bar', color=list_of_bars_colors)

plt.show()