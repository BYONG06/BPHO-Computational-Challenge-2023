import turtle
import pandas 
import numpy

mercuryxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="L,M").to_numpy()
venusxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="P,Q").to_numpy()
earthxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="T,U").to_numpy()
marsxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="X,Y").to_numpy()

jupiterxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AB,AC").to_numpy()
saturnxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AF,AG").to_numpy()
uranusxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AJ,AK").to_numpy()
neptuneyxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AN,AO").to_numpy()
plutoxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AR,AS").to_numpy()

#CALL VALUES IN THESE ARRAYS FROM 1 TO 1001 --> 0 VALUE IS THE COLUMN HEADER

#draw y axis
axes=turtle.Turtle()
#axes._tracer(False)
for i in range (-200, 250, 50):
    axes.pu()
    axes.goto(i,-200)
    axes.pd()
    axes.goto(i, 200)
    axes.pu()
    axes.goto(10, i)
    axes.pd()
    axes.write(str(i/100))
#draw x axis
for i in range (-200, 250, 50):
    axes.pu()
    axes.goto(-200,i)
    axes.pd()
    axes.goto(200, i)
    axes.pu()
    axes.goto(i, -20)
    axes.pd()
    axes.write(str(i/100))
axes.hideturtle()
#axes._update()

planet=turtle.Turtle()
#planet._tracer(False)
planet.speed(10)
def TYPE(PLANET, color):
    planet.penup()
    planet.color(color)

    for i in range(1,1001):

        x = PLANET[i][0]
        y = PLANET[i][1]

        planet.goto(x*100, y*100)
        planet.pendown()

    planet.goto(PLANET[1][0]*100, PLANET[1][1]*100)

    planet.hideturtle()
    #planet._update()

TYPE(mercuryxy, "blue")
TYPE(venusxy, "orange")
TYPE(earthxy, "red")
TYPE(marsxy, "green")
