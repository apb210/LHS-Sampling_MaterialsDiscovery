"""
This program generates Uniformly distributed random samples
in the [0,1] space using Lattice Hypercube Sampling.
Each sample is checked to satisfy non-linear constraints.
The candidates which satisfy the constraints are the new candidates
that are put into a specified output file.

  Usage:
            main.py <input_file> <output_file> <n_results>

        Where:
            input_file contains the number of dimensions, and constraints.
            output_file is the name of the file to be generated
            n_results number of samples to be generated.


    This program uses numpy arrays.
    For diagnostic purposes, the user may want to
    plot pairplots.

    Plotting of pair plots require Pandas and Seaborn libraries be installed in the Stack.


"""

import sys
from constraints import *
from LHSSampling import *
import seaborn as sns

import matplotlib.pyplot as plt

import pandas as pd

def main():



    # Read the input parameters
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    n_results = int(sys.argv[3])


    # Create an instance
    instance = Constraint(inputfile)

    # Perform LHS sampling
    uni = sample(instance.get_ndim(), n_results, 1.0)



    # Generate Pair Plots for diagnostics
    '''
    Generate Pair Plots
    
    # np.savetxt('StandardUniform.csv', uni, delimiter=',')
    # header = list(range(instance.get_ndim()))
    # df = pd.read_csv('StandardUniform.csv', delimiter=',', names=header)
    # sns_plot = sns.pairplot(df)
    # sns_plot.savefig(examplefile+".png")
  
    
    '''

    # Check if the candidates satisfy the constraints or not
    TFlist = np.where(np.apply_along_axis(instance.apply,1,uni))

    # Select Candidates that satisfy the constraints
    TrueList = uni[TFlist]

    print("No. of New Candidates Generated from ",str(n_results)," samples: " + str(len(TrueList)))


    # Write to the specified filename
    outputfile = sys.argv[2]
    np.savetxt(outputfile, TrueList, delimiter=" ")




if __name__ == "__main__":

    Usage = """

        Usage:
            main.py <input_file> <output_file> <n_results>

        Where:
            input_file contains the number of dimensions, and constraints.
            output_file is the name of the file to be generated 
            n_results number of samples to be generated.
        """
    if len(sys.argv) < 4:
        print(Usage)
        sys.exit(0)

    main()