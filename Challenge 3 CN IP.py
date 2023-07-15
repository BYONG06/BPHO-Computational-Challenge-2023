import pandas
import turtle
import numpy

planet = turtle.Turtle()
planet.speed(10)

#obtaining data from excel
mercuryxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="L,M").to_numpy()
venusxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="P,Q").to_numpy()
earthyxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="T,U").to_numpy()
marsxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="X,Y").to_numpy()

jupiterxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AB,AC").to_numpy()
saturnxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AF,AG").to_numpy()
uranusxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AJ,AK").to_numpy()
neptuneyxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AN,AO").to_numpy()
plutoxy = pandas.read_excel("Spreadsheet tasks.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AR,AS").to_numpy()

#scale is x100

planet.penup()

def TYPE(PLANET, color):
    planet.penup()

    for i in range(1,1001):
        planet.color(color)

        x = PLANET[i][0]
        y = PLANET[i][1]

        planet.goto(x*100, y*100)
        planet.pendown()

    planet.goto(PLANET[1][0]*100, PLANET[1][1]*100)

    planet.hideturtle()

#drawing the axes

planet.color("black")
planet.penup()

#labelling axes
for i in range(-200, 250, 50):
    planet.goto(i, 0)
    planet.write(i/100)

planet.goto(225, 0)
planet.write("x/AU")

planet.lt(90)

for i in range(-200, 250, 50):
    planet.goto(0, i)
    planet.write(i/100)

planet.goto(0, 225)
planet.write("y/AU")


#drawing grid line

for i in range(-200, 250, 50):
    planet.penup()
    planet.goto(i, -200)
    planet.pendown()
    planet.fd(400)

planet.rt(90)

for i in range(-200, 250, 50):
    planet.penup()
    planet.goto(-200, i)
    planet.pendown()
    planet.fd(400)

#key
planet.penup()
planet.goto(250, 250)

def label(x, y, color, name):
    planet.penup()
    planet.goto(x, y)
    planet.color(color)
    planet.pendown()
    planet.dot()
    planet.penup()
    planet.fd(20)
    planet.write(name)

label(250, 210, "black", "--Key")
label(250, 200, "red", "--Mercury")
label(250, 190, "orange", "--Venus")
label(250, 180, "purple", "--Earth")
label(250, 170, "green", "--Mars")

#drawing the planets

TYPE(mercuryxy, "red")

TYPE(venusxy, "orange")

TYPE(earthyxy, "purple")

TYPE(marsxy, "green")

