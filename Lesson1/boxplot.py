import matplotlib.pyplot as plt
import numpy as np

def box_plot(data):
    fig, ax = plt.subplots()
    ax.set_title('Height of Student')
    ax.boxplot(data)
    plt.show()


if __name__ == '__main__':

    data = [87, 143, 149, 163, 180, 186, 186, 212, 222,
            247, 251, 255, 257, 261, 271, 274, 277, 281,
            287, 296, 306, 347, 406, 449, 1300]

box_plot(data)



