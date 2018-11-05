"""
This program generates a specified number of candidates in Multidimensional space
using LHS given a set of constraints and one initial valid candidate.

The program uses LHS initially. If it is unable to generate valid candidates,
it switches to a Random Walk Sampling methodology initialized from the
example provided.

The program requires pyDOE which can be installed using

pip install --upgrade pyDOE o


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
import seaborn as sns
from pyDOE import *

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

    Candidates = np.array(instance.get_example())
    NSpace = instance.get_ndim()
    nTrials = 0
    nSamples = 0

    # Modify nFreq to specify when to stop performing LHS and switch to Random Walk
    nFreq = 50

    print("Sampling...")
    while (nSamples < n_results):

        #Perform LHS sampling in the N dimensional space and generate 100,000 samples.
        Sample = lhs(instance.get_ndim(), samples=100000)


        # Generate Pair Plots for diagnostics
        '''
        
        Generate Pair plots to check sampling
        
        np.savetxt('StandardUniform.csv', Sample, delimiter=',')
        header = list(range(instance.get_ndim()))
        df = pd.read_csv('StandardUniform.csv', delimiter=',', names=header)
        sns_plot = sns.pairplot(df)
        sns_plot.savefig("hello"+".png")
        '''

        # Apply the constraints to all the samples generated.
        TFList = np.apply_along_axis(instance.apply,1,Sample)

        # Select candidates which satisfy the constraints (Trues in the TFList)
        TrueList = Sample[TFList]

        if (len(TrueList)>0):

            #Check for duplicates
            NewCandidates = np.array([i for i in TrueList if i not in Candidates])

            #Append unique candidates to the Master CandidateList
            Candidates = np.vstack((Candidates, NewCandidates))


            nSamples = nSamples + len(NewCandidates)



        nTrials = nTrials + 1
        print("No. of Trial: ", nTrials)


        # If after a specified number of trials, the number of candidates generated
        # is less than 50% of the specified number then switch to Random Walk
        if (nTrials == nFreq):
            if (nSamples < 0.5 * nFreq):
                print("Difficult to Sample by Lattice Hypercube Sampling. Performing Random Walk")
                Candidates = RandomWalk(instance, Candidates, n_results)
                break




    # Select 1000 valid candidates.
    Candidates = (Candidates[:1000,:])
    print (len(Candidates))


    # Write to the specified filename
    np.savetxt(outputfile, Candidates, delimiter=" ")

def generate(Vector):
    rand = lambda x: x + np.random.uniform(0 ,x)
    new = np.vectorize(rand)
    return new(Vector)


def RandomWalk(instance, Candidates, n_results):
    example = np.array(instance.get_example())
    nSamples = 0
    while (nSamples < n_results):
        # print (example)
        Sample = np.array(generate(example))

        print(instance.apply(Sample))
        if (instance.apply(Sample) == True):
            Candidates = np.vstack((Candidates,Sample))
            nSamples = nSamples + 1
            print(nSamples)

    return (Candidates)


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