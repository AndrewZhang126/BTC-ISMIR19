import matplotlib.pyplot as plt
import numpy as np
import os, glob

# number of scores
N = 9

score_map = {'root': [], 'majmin': [], 'majmin_inv': [], 'thirds': [], 'triads': [], 
                 'tetrads': [], 'sevenths': [], 'sevenths_inv': [], 'mirex': []}

artists = ["Beatles"]
for artist in artists:
    path = "./output_data/" + artist
    curr_vals = {'root': 0, 'majmin': 0, 'majmin_inv': 0, 'thirds': 0, 'triads': 0, 
                 'tetrads': 0, 'sevenths': 0, 'sevenths_inv': 0, 'mirex': 0}

    num_entries = 0
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            with open(os.path.join(path, filename), 'r') as f:
                for line in f:
                    key, val = line.split(":")[0], float(line.split(":")[-1])
                    if key in curr_vals:
                        curr_vals[key] += val
            num_entries += 1
    for x in curr_vals:
        score_map[x].append(curr_vals[x] / num_entries)

print(score_map)

indices = np.arange(0, 2 * N, step=2)
width = 0.5
colors = ['tab:blue', 'tab:orange', 'darkseagreen']

tick = 0
for i in range(len(artists)):
    vals = []
    for score in score_map:
        vals.append(score_map[score][i])
    plt.bar(indices + tick * width, vals, width, label=artists[i], color=colors[i])
    tick += 1

plt.xticks(indices + 9 * width / 9, score_map.keys(), fontsize=6)
plt.legend(loc="lower center", ncol = 3, bbox_to_anchor=(0.5, 1))
plt.savefig("score_plot.png")