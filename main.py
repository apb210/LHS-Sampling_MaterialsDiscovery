

import sys
from constraints import *
from LHSSampling import *

import matplotlib.pyplot as plt

import pandas as pd

def main():
    inputfile = "C:\\Users\\usaaxb85\\Desktop\\citrine-challenge\\mixture.txt" #sys.argv[1]



    instance = Constraint(inputfile)
    print(instance.example)
    print(instance.get_ndim())
    print(instance.exprs[0])

    uni = sample(instance.get_ndim(), 1000, 1.0)
    print(type(uni))
    print(uni)
    np.savetxt('StandardUniform.csv', uni, delimiter=',')
    df = pd.read_csv('StandardUniform.csv', delimiter=',')
    correlations = df.corr()
    # plot correlation matrix
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    # ticks = numpy.arange(0, 9, 1)
    # ax.set_xticks(ticks)
    # ax.set_yticks(ticks)
    # ax.set_xticklabels(names)
    # ax.set_yticklabels(names)
    plt.show()



    TFlist = np.array(np.apply_along_axis(instance.apply,1,uni))
    print(TFlist)
    np.savetxt('TFList.csv',TFlist,delimiter=" ")

if __name__ == "__main__":

    Usage = """

        Usage:
            main.py first_row.csv NRows

        Where:
            first_row.csv contains the first row as initial condition
            NRows specifies the number of steps to evolve

    """
    # if len(sys.argv) < 3:
    #     print(Usage)
    #     sys.exit(0)

    main()