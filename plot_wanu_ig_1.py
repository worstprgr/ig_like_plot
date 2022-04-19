#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np


# In[7]:


# init
# data = 'data/ig_wanueka/wa_ig1.csv'
data = 'data/ig_wanueka/wa_ig2.csv'

plot_title = 'Wanueka: Likes Over Time (2022-03-31 21:21 - 2022-04-03 04:20)'  # TODO: implement automatic data start & end
hashtags_used = 6

do = pd.read_csv(data)

x_date = pd.read_csv(data, parse_dates=["DATETIME"]).DATETIME
y1 = do.COUNT


# In[8]:


# highest count
yaxis_max = round(y1.max() + ((y1.max() / 100) * 10))


# In[9]:


# count interaction breaks
cib = do.COUNT.values
iACount = 0

unique, counts = np.unique(cib, return_counts=True)
comp_array = np.asarray((unique, counts)).T

for x in range(len(comp_array)):
    if comp_array[x][1] >= 9:
        iACount = iACount + 1


# count plot lifetime
iAlft = len(do.DATETIME)


# formula
# iAScore = round(iACount / iAlft * 100, 1)  # true formula
iAScore = 0  # if data is not complete or biased


# In[10]:


# find hotspots
y2 = []
n_count = []
t_count = 0

# mark coldspots
for x in range(len(y1)):
    try:
        if y1[x] == y1[x+1]:
            t_count = t_count + 1
            n_count.append(t_count)
        else:
            t_count = 0
            n_count.append(t_count)
    except KeyError:
        if y1[x] == y1[x]:
            t_count = t_count + 1
            n_count.append(t_count)
        else:
            t_count = 0
            n_count.append(t_count)


# count coldspots
for n in range(len(n_count)):
    if n_count[n] <= 2:
        y2.append(y1[n])
    else:
        y2.append(np.nan)
        

y2 = pd.DataFrame(y2, columns=['HOTSPOT'])
y2 = y2.HOTSPOT


# In[14]:


# plot section
fig, (ax, ax2) = plt.subplots(1,2, figsize=(22, 10), gridspec_kw={'width_ratios': [15, 1]})

# color config
fontcolor = 'white'
gridcolor = '#43454a'
legendcolor = '#1b1c1f'
figcolor = '#1b1c1f'
plotcolor = '#181a1c'
bordercolor = '#222326'
cblue = '#268fd7'
cred = '#c92a40'
clred = '#ed324c'

# date format
locator = mdates.AutoDateLocator(minticks=10, maxticks=30)
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

# axes
ax.plot(x_date, y1, label='Likes', color=cblue, linewidth=1)
ax.plot(x_date, y2, label='Hotspots', color=clred, linewidth=1)

# axes 2
ax2.bar('IAS', iAScore, color=cred)

# plot config
# ax.set_xlabel('Time')
ax.set_ylabel('Likes', color=fontcolor, fontsize=20)
ax2.set_ylabel('Interaction Score (Lower = Good)', color=fontcolor, fontsize=18)
ax.set_title(plot_title, color=fontcolor, fontsize=25, fontstyle='italic')

# annotate
anno_xy1 = (0.188, 0.19)
ax.annotate('Data loss',
            xy=anno_xy1,
            xycoords='axes fraction',
            xytext=(anno_xy1[0]-0.034, anno_xy1[1]-0.09),
            color='white',
            size='15',
            bbox=dict(boxstyle="square", color=cblue, alpha=0.4),
            arrowprops=dict(arrowstyle="wedge,tail_width=0.5", color=cblue, alpha=0.4)
           )

anno_xy2 = (0.532, 0.68)
ax.annotate('Data loss',
            xy=anno_xy2,
            xycoords='axes fraction',
            xytext=(anno_xy2[0]-0.034, anno_xy2[1]-0.09),
            color='white',
            size='15',
            bbox=dict(boxstyle="square", color=cblue, alpha=0.4),
            arrowprops=dict(arrowstyle="wedge,tail_width=0.5", color=cblue, alpha=0.4)
           )


# info
boxtext = 'Hashtags used: ' + str(hashtags_used)
props = dict(boxstyle='square', facecolor='white', alpha=0.09)

ax.text(0.02, 0.97, boxtext, transform=ax.transAxes, fontsize=15, color='white',
        verticalalignment='top', bbox=props)

ax.text(0.02, 0.91, 'Data incomplete. No IA-Score available', transform=ax.transAxes, fontsize=15, color='white',
        verticalalignment='top', bbox=props)


ax.legend(loc='lower right', fontsize=18, labelcolor=fontcolor, facecolor=legendcolor)
ax.set(facecolor = plotcolor)
ax2.set(facecolor = plotcolor)
ax.spines["top"].set_color(bordercolor)
ax.spines["bottom"].set_color(bordercolor)
ax.spines["left"].set_color(bordercolor)
ax.spines["right"].set_color(bordercolor)
fig.patch.set_facecolor(figcolor)
ax.grid(True, color=gridcolor)  # Show Grid
# ax.grid(False)  # Don't show Grid
ax2.grid(True, color=gridcolor)
# ax2.grid(False)  # Don't show Grid
ax.tick_params(axis='x', labelrotation = 0, color=gridcolor, labelsize=14, labelcolor=fontcolor)
ax.tick_params(axis='y', color=gridcolor, labelsize=14, labelcolor=fontcolor)
ax2.tick_params(axis='x', labelrotation = 0, color=gridcolor, labelsize=14, labelcolor=fontcolor)
ax2.tick_params(axis='y', color=gridcolor, labelsize=14, labelcolor=fontcolor)
ax.set_ylim(0, yaxis_max)
ax2.set_ylim(0, 10)


# In[ ]:




