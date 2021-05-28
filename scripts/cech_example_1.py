from pylab import *
from itertools import *

points = [(0,1),(0,-1),(1,0),(-1,0)]

toplot = lambda x,y: np.array([x,y]).transpose()

def forplot(eps,alpha=0.2,name =None):
    fig = figure()
    ax = fig.add_subplot(1, 1, 1)

    colors = ("black","blue","orange","blue")

    fig.set_figwidth(10)
    fig.set_figheight(10)

    for p in points:
        scatter(*p,color=colors[-1])
        
    if eps>sqrt(2)/2:
        plot(*toplot(points[0],points[2]),color=colors[0])
        plot(*toplot(points[0],points[3]),color=colors[0])
        plot(*toplot(points[1],points[2]),color=colors[0])
        plot(*toplot(points[1],points[3]),color=colors[0])
    

    for p in points:
        ax.add_patch(Circle(p,eps,color=colors[1],alpha=alpha))
        
    if eps>1:
        plot(*toplot(points[0],[0,0]),color=colors[0])
        plot(*toplot(points[1],[0,0]),color=colors[0])
        plot(*toplot(points[2],[0,0]),color=colors[0])
        plot(*toplot(points[3],[0,0]),color=colors[0])
        scatter(0,0,color=colors[0])
        
        fill([0,1,0],[0,0,1],alpha=0.7,color=colors[2])
        fill([0,-1,0],[0,0,1],alpha=0.7,color=colors[2])
        fill([0,1,0],[0,0,-1],alpha=0.7,color=colors[2])
        fill([0,-1,0],[0,0,-1],alpha=0.7,color=colors[2])
        fill([0,1,0,-1],[1,0,-1,0],alpha=0.1,color=colors[2])
    if name:
        savefig(name)


    #show()
forplot(0.6,name="../imgs/cech_example_1_0_6.png")
forplot(0.8,name="../imgs/cech_example_1_0_8.png")
forplot(1.2,name="../imgs/cech_example_1_1_2.png")
