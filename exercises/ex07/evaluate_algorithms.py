"""Evaluating the algorithms."""

__author__: str = "730659778"

import matplotlib.pyplot as plt

from runtime_analysis_functions import evaluate_memory_usage
START_SIZE: int = 0
END_SIZE: int = 100


usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - alexcout")
plt.show()
 
usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - alexcout")
plt.show()