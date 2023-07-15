import turtle
import pandas 
import numpy

mercuryxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="L,M").to_numpy()
venusxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="P,Q").to_numpy()
earthxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="T,U").to_numpy()
marsxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="X,Y").to_numpy()
#CALL VALUES IN THESE ARRAYS FROM 1 TO 1001 --> 0 VALUE IS THE COLUMN HEADER

#draw y axis
axes=turtle.Turtle()
axes.hideturtle()
axes._tracer(False)
for i in range (-200, 250, 50):
    axes.pu()
    axes.goto(i,-200)
    axes.pd()
    axes.goto(i, 200)
    axes.pu()
    axes.goto(10, i)
    axes.write(str(i/100))
    axes.pu()
    axes.goto(-200,i)
    axes.pd()
    axes.goto(200, i)
    axes.pu()
    axes.goto(i, -20)
    axes.write(str(i/100))
axes.goto(225, 0)
axes.write("x/AU")
axes.goto(0, 225)
axes.write("y/AU")
axes._update()
axes._update()

planet=turtle.Turtle()
planet._tracer(False)
planet.hideturtle()

def TYPE(PLANET, color):
    planet.penup()
    planet.color(color)
    for i in range(1,1001):
        x = PLANET[i][0]
        y = PLANET[i][1]
        planet.goto(x*100, y*100)
        planet.pendown()

    planet.goto(PLANET[1][0]*100, PLANET[1][1]*100)
    planet._update()

TYPE(mercuryxy, "blue")
TYPE(venusxy, "orange")
TYPE(earthxy, "red")
TYPE(marsxy, "green")

def label(x, y, color, name):
    planet.penup()
    planet.goto(x, y)
    planet.color(color)
    planet.write(name)

label(250, 210, "black", "Key")
label(250, 200, "blue", "-- Mercury")
label(250, 190, "orange", "-- Venus")
label(250, 180, "red", "-- Earth")
label(250, 170, "green", "-- Mars")
