#!/usr/bin/env python

# Adapted from the Glowing python example.
# http://glowingpython.blogspot.com/2012/02/convolution-with-numpy.html

################################################################################
# Make a histogram and plot it on a figure (TCanvas).
################################################################################

################################################################################
# Import the standard libraries in the accepted fashion.
################################################################################
from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import scipy.stats as stats
import scipy.signal as signal

def smear_with_gaussian_convolution(x,y,mean,sigma):

    npts = len(x)

    convolving_term = stats.norm(mean,sigma)

    convolving_pts = convolving_term.pdf(x)

    convolved_function = signal.convolve(y/y.sum(),convolving_pts)
    print convolved_function

    znpts = len(convolved_function)
    begin = znpts/2 - npts/2
    end = znpts/2 + npts/2

    print "%d %d %d %d" % (npts,znpts,begin,end)

    return convolved_function[begin:end],convolving_pts

################################################################################
# main
################################################################################
def main():
    
    ############################################################################
    # Make a figure on which to plot stuff.
    # This would be the same as making a TCanvas object.
    ############################################################################
    fig1 = plt.figure(figsize=(12,4),dpi=100,facecolor='w',edgecolor='k')

    ############################################################################
    # Now divide of the figure as if we were making a bunch of TPad objects.
    # These are called ``subplots".
    #
    # Usage is XYZ: X=how many rows to divide.
    #               Y=how many columns to divide.
    #               Z=which plot to plot based on the first being '1'.
    # So '111' is just one plot on the main figure.
    ############################################################################
    #subplot = fig1.add_subplot(1,1,1)

    lo = -3
    hi =  3
    npts = 1000

    ############################################################################
    # Generate values drawn from a normal (Gaussian) distribution.
    ############################################################################
    mean = 0.0
    sigma = 0.5
    rv = stats.norm(mean,sigma)
    x = np.linspace(lo,hi,npts)
    #print x
    gpts = rv.pdf(x)
    fig1.add_subplot(1,3,2)
    plt.plot(x,gpts,color='k')

    ############################################################################
    # Generate values drawn from a negative exponential
    ############################################################################
    tau = 1.0
    x_exp = np.linspace(0,5,npts)
    exp_pts = np.exp(x_exp*(-tau))
    fig1.add_subplot(1,3,3)
    plt.plot(x_exp,exp_pts,color='k')

    ############################################################################
    # Try the convolution
    ############################################################################
    conv_means = [0.0,0.0,-1.0]
    conv_sigmas = [0.1,0.5,0.5]
    colors = ['r','g','b']
    for cm,cs,color in zip(conv_means,conv_sigmas,colors):
        z,convpts = smear_with_gaussian_convolution(x,gpts,cm,cs)
        fig1.add_subplot(1,3,1)
        plt.plot(x,convpts)

        fig1.add_subplot(1,3,2)
        plt.plot(x,z,color=color)

        # Exponential
        z,convpts = smear_with_gaussian_convolution(x,exp_pts,cm,cs)

        fig1.add_subplot(1,3,3)
        plt.plot(x_exp,z,color=color)
        #plt.set_xlim(0,5)

    # Need this command to display the figure.
    plt.show()

################################################################################
# Top-level script evironment
################################################################################
if __name__ == "__main__":
    main()
