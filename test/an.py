import matplotlib.pyplot as plt

class Model(object):
    def __init__(self):
        pass
    def plot_data(self):
        plt.plot([1,2,3],[1,2,3])
        plt.title('Data for Model Version: ', fontsize=20)
        plt.xlabel('timestamp', fontsize=12)
        plt.ylabel('value', fontsize=12)
        plt.show()