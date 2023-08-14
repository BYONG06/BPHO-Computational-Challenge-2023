import math
import matplotlib.pyplot as graphing
def integrate (theta0, theta, n, function, eccentricity, p):
    h = (theta-theta0)/n
    yvals=[]
    for i in range (0,n+1):
        yvals.append(function(theta0+(i*h), eccentricity, p))
    total=0
    for x in yvals:
        if yvals.index(x)==0 or yvals.index(x)==len(yvals)-1:
            total=total+x
        elif yvals.index(x)%2 == 0:
            total=total+(x*2)
        elif yvals.index(x)%2 ==1:
            total=total+(x*4)
    finaltotal=total*(1/3)*h
    return finaltotal
    

def function(val,eccentricity, p):
    integration = (1/((1-(eccentricity*math.cos(val)))**2))
    t = p*(1-eccentricity**2)**(3/2)*(1/(2*math.pi))*integration
    return t

yCoords=[]
for i in range (0,2001,5):
    yCoords.append(i/100)

def gencoords1(eccentricity, yCoords, p):
    xCoordsE=[]
    for j in yCoords:
        xCoordsE.append(integrate (0, j, 400, function, eccentricity, p))
    return xCoordsE

def gencoords2(yCoords, p):
    xCoordsC=[]
    for j in yCoords:
        xCoordsC.append((j*p)/(2*math.pi))
    return xCoordsC

#Elipse
mercuryxCoords=gencoords1(0.21, yCoords, 0.241)
venusxCoords=gencoords1(0.01, yCoords, 0.651)
earthxCoords=gencoords1(0.02, yCoords, 1)
marsxCoords=gencoords1(0.09, yCoords, 1.881)
jupiterxCoords=gencoords1(0.05, yCoords, 11.861)
saturnxCoords=gencoords1(0.06, yCoords, 29.628)
uranusxCoords=gencoords1(0.05, yCoords, 84.747)
neptunexCoords=gencoords1(0.01, yCoords, 166.344)
plutoxCoords=gencoords1(0.25, yCoords, 248.348)

#Circular
CmercuryxCoords=gencoords2(yCoords, 0.241)
CvenusxCoords=gencoords2(yCoords, 0.651)
CearthxCoords=gencoords2(yCoords, 1)
CmarsxCoords=gencoords2(yCoords, 1.881)
CjupiterxCoords=gencoords2(yCoords, 11.861)
CsaturnxCoords=gencoords2(yCoords, 29.628)
CuranusxCoords=gencoords2(yCoords, 84.747)
CneptunexCoords=gencoords2(yCoords, 166.344)
CplutoxCoords=gencoords2(yCoords, 248.348)

def plot(planetE, planetC, NAME):
    fig = graphing.figure("Challenge 5")
    graphing.xlabel('Time/years')
    graphing.ylabel('Orbit Polar Angle/rad')
    graphing.plot(planetE, yCoords, alpha = 0.4,
             color = "green", linestyle ='solid',
             linewidth = 1, marker ='D',
             markersize = 1, markerfacecolor = "green",
             markeredgecolor = "green")

    graphing.plot(planetC, yCoords, alpha = 0.4,
             color = "blue", linestyle ='solid',
             linewidth = 1, marker ='D',
             markersize = 1, markerfacecolor = "blue",
             markeredgecolor = "blue")
    graphing.title('Orbit angle VS time for ' + NAME)
    graphing.grid(alpha =.6, linestyle ='-')

def ME():
    plot(mercuryxCoords, CmercuryxCoords, "Mercury")
    graphing.legend(["P = 0.241, Σ = 0.21", "Circular Σ = 0"], loc = "upper left")
    graphing.show()
def VE():
    plot(venusxCoords, CvenusxCoords, "Venus")
    graphing.legend(["P = 0.615, Σ = 0.01", "Circular Σ = 0"], loc = "upper left")
    graphing.show()
def EA():
    plot(earthxCoords, CearthxCoords, "Mars")
    graphing.legend(["P = 1.000, Σ = 0.02", "Circular Σ = 0"], loc = "upper left")
    graphing.show()

def MA():
    plot(earthxCoords, CearthxCoords, "Earth")
    graphing.legend(["P = 1.881, Σ = 0.09", "Circular Σ = 0"], loc = "upper left")
    graphing.show()
def JU():
    plot(marsxCoords, CmarsxCoords, "Jupiter")
    graphing.legend(["P = 11.861, Σ = 0.05", "Circular Σ = 0"], loc = "upper left")
    graphing.show()
def SA():
    plot(jupiterxCoords, CjupiterxCoords, "Saturn")
    graphing.legend(["P = 29.628, Σ = 0.06", "Circular Σ = 0"], loc = "upper left")
    graphing.show()
def UR():
    plot(saturnxCoords, CsaturnxCoords, "Uranus")
    graphing.legend(["P = 84.747, Σ = 0.05", "Circular Σ = 0"], loc = "upper left")
    graphing.show()
def NE():
    plot(neptunexCoords, CneptunexCoords, "Neptune")
    graphing.legend(["P = 166.344, Σ = 0.01", "Circular Σ = 0"], loc = "upper left")
    graphing.show()
def PL():
    plot(plutoxCoords, CplutoxCoords, "Pluto")
    graphing.legend(["P = 248.348, Σ = 0.25", "Circular Σ = 0"], loc = "upper left")
    graphing.show()


