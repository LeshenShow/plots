import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
# import pylab
# import random
# from matplotlib import animation
# import seaborn as sns
df = pd.read_csv("data/daily_temperature_1000_cities_1980_2020.csv", low_memory=False)
date = np.unique(df['Date'].values)

Moscow = df['Moscow'].values
Prague = df['Prague'].values
Amsterdam = df['Amsterdam'].values
Helsinki = df['Helsinki'].values
Tirana = df['Tirana'].values
Athens = df['Athens'].values
Belgrade = df['Belgrade'].values
Berlin = df['Berlin'].values
Paris = df['Paris'].values
Kyiv = df['Kyiv'].values
Lisbon = df['Lisbon'].values
London = df['London'].values
Rome = df['Rome'].values
# print(max(Moscow))
# print(max(Prague))
# print(max(Amsterdam))
# print(max(Helsinki))
# print(max(Tirana))
# print(max(Athens))
# print(max(Belgrade))
# print(max(Berlin))
# print(max(Paris))
# print(max(Kyiv))
# print(max(Lisbon))
# print(max(London))
# print(max(Rome))
#
# print(min(Moscow))
# print(min(Prague))
# print(min(Amsterdam))
# print(min(Helsinki))
# print(min(Tirana))
# print(min(Athens))
# print(min(Belgrade))
# print(min(Berlin))
# print(min(Paris))
# print(min(Kyiv))
# print(min(Lisbon))
# print(min(London))
# print(min(Rome))
text_color = '#C8D2D1'
bg_color = '#145c6d'
# fig = plt.figure()
# axes = fig.add_subplot(1, 1, 1)
fig, ax = plt.subplots(figsize=(16, 8))
fig.set_facecolor(bg_color)
# plt.tight_layout()


# palette = list(reversed(sns.color_palette("Spectral", 9).as_hex()))
# labels = ('Tokyo', 'Moscow','Prague' )

# axes.set_ylim(1,2)
# axes.set_xlabel('Celc')
# plt.style.use("seaborn")
# fig = plt.figure()
# axes = fig.add_subplot(1, 1, 1)
def bar_race(i):
    ax.clear()

    c_1 = (Moscow[i])
    c_2 = (Prague[i])
    c_3 = (Amsterdam[i])
    c_4 = (Helsinki[i])
    c_5 = (Tirana[i])
    c_6 = (Athens[i])
    c_7 = (Belgrade[i])
    c_8 = (Berlin[i])
    c_9 = (Paris[i])
    c_10 = (Kyiv[i])
    c_11 = (Lisbon[i])
    c_12 = (London[i])
    c_13 = (Rome[i])

    list_y_ticks = sorted([c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13])

    color_dic = {c_1: '#DED3A6', c_2: '#759242', c_3: '#BD613C',
                 c_4: '#f266fc', c_5: '#d90044', c_6: '#4599f8',
                 c_7: '#a3991c', c_8: '#46231c', c_9: '#e7d4f0',
                 c_10: '#f5c428', c_11: '#00ec7a', c_12: '#0000ea', c_13: '#ed5c6d'}
    color = []
    for key in list_y_ticks:
        color.append(color_dic[key])

    bar_h = plt.barh(range(13), list_y_ticks, color=color)  # , color=palette)

    dict_tick = {'Москва': c_1, "Прага": c_2, "Амстердам": c_3,
                 "Хельсинки": c_4, "Тирана": c_5, "Афины": c_6,
                 "Белград": c_7, "Берлин": c_8, "Париж": c_9,
                 "Киев": c_10, "Лиссабон": c_11, "Лондон": c_12, "Рим": c_13}
    sorted_dict = sorted(dict_tick.items(), key=lambda x: x[1])
    tick = [i[0] for i in sorted_dict]

    plt.title(label=f'{date[i]}', color=text_color, fontsize=25)
    plt.yticks(np.arange(13), tick)
    for tl, tc in zip(plt.gca().get_yticklabels(), color):
        tl.set_color(tc)


    ax.bar_label(bar_h, labels=list_y_ticks, padding=0, color=text_color, fontsize=20, label_type='center') #label_type='edge'
    # https: // questu.ru / questions / 28931224 /
    # label = "{:.1f}".format(x_value)
    #
    # # Create annotation
    # plt.annotate(
    #     label,  # Use `label` as label
    #     (x_value, y_value),  # Place label at end of the bar
    #     xytext=(space, 0),  # Horizontally shift label by `space`
    #     textcoords="offset points",  # Interpret `xytext` as offset in points
    #     va='center',  # Vertically center label
    #     ha=ha)  # Horizontally align label differently for
    # # positive and negative values.

    # plt.text(x, y, s, ha, Bbox)
    # ax.set_xlim(left=-30, right=30)
    ax.patch.set_facecolor(bg_color)
    ax.spines['left'].set_color(text_color)
    ax.spines['right'].set_color(bg_color)
    ax.spines['bottom'].set_color(text_color)
    ax.spines['top'].set_color(bg_color)
    ax.tick_params(axis='x', colors=text_color, labelsize=20)
    ax.tick_params(axis='y', color=text_color,  labelsize=20) # labelcolor=text_color,
    ax.set_xlabel("Температура", color=text_color)  # plt.xlabel
    ax.set_ylabel("Город", color=text_color)  # plt.ylabel
    ax.grid(axis='x', color=text_color, linewidth=0.5, linestyle='-')

ani = FuncAnimation(fig, bar_race, interval=50, blit=False)  # blit=True)
# df.plot(x='Date', y=['Tokyo', 'Moscow', 'Prague'])
plt.show()
