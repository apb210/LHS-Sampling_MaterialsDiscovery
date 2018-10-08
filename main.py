

import sys
from constraints import *
from LHSSampling import *


def main():
    inputfile = "C:\\Users\\usaaxb85\\Desktop\\citrine-challenge\\mixture.txt" #sys.argv[1]

    instance = Constraint(inputfile)
    print(instance.example)
    print(instance.get_ndim())
    print(instance.exprs[0])


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