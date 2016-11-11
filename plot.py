'''
Created on Nov 17, 2011

@author: rupam
'''
import sys
from numpy import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def main():
    x1steps = x2steps = 50.0
    x1range = linspace(0, 6-6/x1steps, x1steps)
    x2range = linspace(0, 6-6/x2steps, x2steps)
    y = loadtxt(sys.argv[1])

    fig = figure()
    ax = Axes3D(fig)
    x1,x2 = meshgrid(x1range,x2range)
    ax.plot_surface(x1, x2, y.T, cstride=1, rstride=1, cmap=cm.jet)
    ax.set_xlabel('$in_1$')
    ax.set_ylabel('$in_2$')
    ax.set_zlabel('$f$')
    savefig("plot.pdf", bbox_inches='tight')
    
if __name__ == '__main__':
    main()
    show()
