import pandas as pd
import matplotlib.pyplot as plt

file = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"
df = pd.read_csv(file)
pd.set_option("display.max.columns", None)
for y, x in enumerate(df['Major_category']):
    df.loc[y, 'Major_category'] = x.replace(' & ', ' &\n')

color = ('#bc5477', '#90bdc0', '#dc9bb3', '#92c1df', '#ca9eca', '#8ecb73')
# text_color = '#a8bed6'
# bg_color = '#182633'
text_color = '#c7cfda'
bg_color = '#506f84'

fig = plt.figure(figsize=(16, 8))
plt.suptitle("Студенты", color=text_color, fontsize=15)
# fig.add_subplot(ROW,COLUMN,POSITION)
#
# ROW=number of rows
# COLUMN=number of columns
# POSITION= position of the graph you are plotting
ax1 = fig.add_subplot(221)  # OR plt.subplot(2,2,1)
df_sex = df.loc[df['Rank'] < 180, ['Major_category', 'Men', 'Women', 'Total']]
df_sex = df_sex.groupby(['Major_category']).sum().reset_index().sort_values(by=['Total'], ascending=False)
df_sex.plot(ax=plt.gca(),
            x='Major_category',
            y=['Men', 'Women'],
            kind='barh',
            color=color,
            fontsize=7,
            )
# ax1.set_yticklabels(df_sex['Major_category'],
#                     # fontsize=15,
#                     color=text_color,
#                     # rotation=0,
#                     # verticalalignment='center',
#                     horizontalalignment='right',
#                     position=(0, 0),
#                     )
ax1.tick_params(axis='x', colors=text_color)
ax1.tick_params(axis='y', color=text_color, labelcolor=text_color)
ax1.patch.set_facecolor(bg_color)
ax1.spines['left'].set_color(text_color)
ax1.spines['right'].set_color(bg_color)
ax1.spines['bottom'].set_color(bg_color)
ax1.spines['top'].set_color(bg_color)

ax1.set_title("Половое соотношение", color=text_color)  # plt.title
ax1.set_xlabel("Количество", color=text_color)  # plt.xlabel
ax1.set_ylabel("Направление", color=text_color)  # plt.ylabel
ax1.grid(axis='x', color=text_color, linewidth=0.75)

ax2 = fig.add_subplot(222)  # OR plt.subplot(1,2,2)
df_salary = df.loc[df['Rank'] < 180, ['Major_category', 'Median', 'P25th', 'P75th']]
df_salary = df_salary.groupby(['Major_category']).mean().reset_index().sort_values(by=['Median'], ascending=True)
df_salary.plot(ax=plt.gca(),
               x='Major_category',
               y=['Median', 'P25th', 'P75th'],
               kind='barh',
               color=color,
               fontsize=7,
               )
ax2.tick_params(axis='both', color=text_color, rotation=0, labelcolor=text_color)
ax2.patch.set_facecolor(bg_color)
ax2.spines['left'].set_color(text_color)
ax2.spines['right'].set_color(bg_color)
ax2.spines['bottom'].set_color(bg_color)
ax2.spines['top'].set_color(bg_color)
ax2.set_title("Зарплатное соотношение", color=text_color)  # plt.title
ax2.set_xlabel("Зарплата, год, $", color=text_color)  # plt.xlabel
ax2.set_ylabel("Направление", color=text_color)  # plt.ylabel

ax3 = fig.add_subplot(223)
df_corr = df.loc[df['Rank'] < 180, ['Unemployment_rate', 'ShareWomen']]
df_corr.plot(ax=plt.gca(),
             x='ShareWomen',
             y='Unemployment_rate',
             kind='scatter',
             color=color[0],
             fontsize=7,
             )
ax3.tick_params(axis='both', color=text_color, rotation=0, labelcolor=text_color)
ax3.set_title("Определение зависимостей", color=text_color)  # plt.title
ax3.set_xlabel("Доля женщин", color=text_color)  # plt.xlabel
ax3.set_ylabel("Доля безработных", color=text_color)
ax3.spines['left'].set_color(text_color)
ax3.spines['right'].set_color(bg_color)
ax3.spines['bottom'].set_color(bg_color)
ax3.spines['top'].set_color(bg_color)
ax3.patch.set_facecolor(bg_color)
ax3.grid(axis='y', linestyle='--', color=text_color, linewidth=0.75)

ax4 = fig.add_subplot(224)
df_employed = [df['Full_time'].sum(), df['Part_time'].sum()]
print(df_employed)
ax4.pie(df_employed,
        labels=['Full time', 'Part time'],
        colors=color[::1],
        autopct='%.2f',
        textprops={'color': 'w'}
        )
ax4.set_title("Доля частичной и полной занятости", color=text_color)  # plt.title

fig.set_facecolor(bg_color)
plt.tight_layout()
plt.show()

# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
# file = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"
# # file_categ = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv'
# df = pd.read_csv(file)
# # df_categ = pd.read_csv(file_categ)
# # df = df.merge(df_categ[['Major_code', 'Major_category']], on='Major_code')
# pd.set_option("display.max.columns", None)
# df_sex = df.loc[df['Rank'] < 180, ['Major_category', 'Men', 'Women', 'Total']]
# df_sex = df_sex.groupby(['Major_category']).sum().reset_index().sort_values(by=['Total'], ascending=False)
# for y, x in enumerate(df_sex['Major_category']):
#     df_sex.loc[y, 'Major_category'] = x.replace(' & ', ' &\n')
# # print(df_sex.loc[2, 'Men'])
# df_sex.plot(ax=axes[0,0], x='Major_category', y=['Men', 'Women'], figsize=(10, 5), kind='bar')
# # plot_plot = df_short.plot(x='Major', y=['Men', 'Women'], kind='bar', rot=0, figsize=(10, 5))
# # plt.tick_params(axis='x', rotation=5)
# df_sex2 = df.loc[df['Rank'] < 180, ['Major_category', 'Men', 'Women', 'Total']]
# df_sex2 = df_sex2.groupby(['Major_category']).sum().reset_index().sort_values(by=['Total'], ascending=False)
# for y, x in enumerate(df_sex2['Major_category']):
#     df_sex2.loc[y, 'Major_category'] = x.replace(' & ', ' &\n')
# # print(df_sex.loc[2, 'Men'])
# df_sex2.plot(ax=axes[0,1], x='Major_category', y=['Men', 'Women'], kind='bar')
# fig.delaxes(axes[1,0])
# fig.delaxes(axes[1,1])
# plt.tight_layout()
# plt.show()
