import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt


def rgb_to_hex(colors):
    """Return color as #rrggbb for the given color values."""
    red, green, blue = colors
    return '#%02x%02x%02x' % (red, green, blue)

im = Image.open("Untitled.jpg") #Can be many different formats.
pix = im.load()
color_list = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        color_list.append(pix[x, y])


pd_list_of_colours = pd.Series(color_list, name='Color')
Series_value_count = pd_list_of_colours.value_counts(normalize=True)
Series_value_count = Series_value_count.head(50)
df_value_count = Series_value_count.to_frame(name='Color percentage')
df_value_count.reset_index(level=0, inplace=True)
df_value_count.rename(columns={'index': 'Colors'}, inplace=True)

# df_value_count[['R', 'G', 'B']] = df_value_count.Colors.apply(pd.Series)

df_value_count['hex_c'] = df_value_count.Colors.apply(rgb_to_hex)
list_of_bars_colors = df_value_count['hex_c'].tolist()

df_value_count.drop('hex_c', axis=1, inplace=True)

df_value_count.set_index('Colors', inplace=True)

# writer = pd.ExcelWriter('Colors.xlsx')
# df_value_count.to_excel(writer, 'Sheet1')
# writer.save()
# writer.close()

print(df_value_count)

df_value_count.plot(kind='bar', color=list_of_bars_colors)
plt.tight_layout()
plt.show()
