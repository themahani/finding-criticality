from read_files import read_files
import numpy as np
import matplotlib.pyplot as plt

def main():
    file = np.random.choice(read_files())
    data = np.load(file)

    x = np.arange(data[0], data[0] + len(data) - 1)
    y = data[1:]
    z = (y != 0)

    plt.loglog()
    plt.scatter(x[z], y[z] / y.sum(), s=5)
    plt.xlabel("$s$")
    plt.ylabel("$P(s)$")
    plt.show()

if __name__ == "__main__":
    main()
