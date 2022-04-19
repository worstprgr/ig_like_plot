## ig_like_plot
Plots the like-count from a single Instagram post.</br>

_(Experimental)_ iAS (Interaction Score): Lower number = better. </br>
Formula:</br>
Hotspot Occurrence / Lines of Data * 100</br></br>

Hotspots: If the user interaction is high, the line turns red.</br>
```python

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
```
</br></br>

Examples:</br>
![Plot 1](/wa_ig1.png?raw=true "Plot1")</br></br>
![Plot 2](/wa_ig2.png?raw=true "Plot2")</br>
