import numpy as np
import matplotlib.pyplot as plt

def random_walk_1d(steps):
    random_integers = np.random.randint(2, size=steps)
    steps_taken = 2 * random_integers - 1
    position = np.cumsum(steps_taken)
    return position

num_steps = int(input("Enter the number of steps: "))
walk = random_walk_1d(num_steps)

plt.subplot(2, 1, 1)
plt.plot(range(num_steps), walk)
plt.title("1D Random Walk")
plt.xlabel("Steps")
plt.ylabel("Position")

plt.subplot(2, 1, 2)
plt.hist(walk, bins=max(walk) - min(walk) + 1, color='blue', alpha=0.7, rwidth=0.8)
plt.title("Histogram with X as Position and Y as Frequency")
plt.xlabel("Position")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
