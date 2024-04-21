
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

def draw(data, src):
	collection, lines = create_collection(data)

	fig, axs = plt.subplots()
	fig.set_figwidth(10)
	fig.set_figheight(5)

	axs.add_collection(collection)
	[axs.add_line(line) for line in lines]

	plt.axis('auto')
	plt.savefig(src)

def create_collection(data):
    l = len(data)

    grid = []
    height = []
    colors = []

    for i in range(l):
        if data[i]['Close'] > data[i]['Open']:
            grid.append([i+1, data[i]['Open']])
            height.append(data[i]['Close'] - data[i]['Open'])
            colors.append('green')
        elif data[i]['Close'] < data[i]['Open']:
            grid.append([i+1, data[i]['Close']])
            height.append(data[i]['Open'] - data[i]['Close'])
            colors.append('red')
    grid = np.array(grid)

    patches = []
    lines = []
    width = 0.5

    for i in range(l):
        rect = mpatches.Rectangle(grid[i]-[width/2, 0.0], width, height[i])
        patches.append(rect)
        line = mlines.Line2D([i+1, i+1], [data[i]['Low'], data[i]['High']], lw=0.75, color=colors[i])
        lines.append(line)

    collection = PatchCollection(patches, cmap=plt.cm.hsv)
    collection.set_facecolors(colors)
    collection.set_linewidth(1.0)
    collection.set_edgecolors(colors)

    return collection, lines


if __name__ == "__main__":

	data = [
	    {'Open': 100, 'High': 120, 'Low': 100, 'Close': 120},
	    {'Open': 120, 'High': 125, 'Low': 100, 'Close': 110},
	    {'Open': 120, 'High': 150, 'Low': 120, 'Close': 150},
	    {'Open': 150, 'High': 200, 'Low': 140, 'Close': 200},
	    {'Open': 220, 'High': 240, 'Low': 130, 'Close': 130},
	    {'Open': 140, 'High': 170, 'Low': 120, 'Close': 120},
	    {'Open': 110, 'High': 110, 'Low': 90, 'Close': 95},
	]
	draw(data, "example.png")

	
