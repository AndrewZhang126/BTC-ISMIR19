import matplotlib.pyplot as plt
import numpy as np
import os, glob

N = 3

root_score = []
majmin_score = []
mirex_score = []

artists = ["Beatles", "Queen", "USPop"]
for artist in artists:
    path = "./BTC-ISMIR19/output_data/" + artist
    curr_root = 0
    curr_majmin = 0
    curr_mirex = 0
    num_entries = 0
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            with open(os.path.join(path, filename), 'r') as f:
                for line in f:
                    key, val = line.split(":")[0], float(line.split(":")[-1])
                    if key == 'root':
                        curr_root += val
                    elif key == 'majmin':
                        curr_majmin += val
                    elif key == 'mirex':
                        curr_mirex += val
            num_entries += 1
    root_score.append(curr_root / num_entries)
    majmin_score.append(curr_majmin / num_entries)
    mirex_score.append(curr_mirex / num_entries)

print(root_score)
print(majmin_score)
print(mirex_score)


indices = np.arange(N)
width = 0.3

plt.bar(indices, root_score, width, label='Root Score', color='tab:blue')
plt.bar(indices + width, majmin_score, width, label='Maj-Min Score', color='tab:orange')
plt.bar(indices + 2 * width, mirex_score, width, label='MIREX Score', color='darkseagreen')

plt.xticks(indices + 3 * width / 3, artists)
plt.legend(loc="best")
plt.savefig("score_plot.png")