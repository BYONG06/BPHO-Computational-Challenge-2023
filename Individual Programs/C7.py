import pandas
import turtle
import numpy

planet = turtle.Turtle()
planet.speed(10)
planet.penup()
planet.goto(-250, 410)
planet.write("Outer Planets", font=("Courier", 30, "bold"), align = "center")

planets = ["0 Jupiter", "1 Saturn", "2 Uranus", "3 Neptune", "4 Pluto"]

#drawing the axes

planet.color("black")
planet._tracer(False)

#labelling axes
for i in range(-400, 600, 100):
    planet.goto(i, 0)
    planet.write(i/5)

planet.goto(550, 0)
planet.write("x/AU")

planet.lt(90)

for i in range(-400, 500, 100):
    planet.goto(0, i)
    planet.write(i/5)

planet.goto(0, 425)
planet.write("y/AU")


#drawing grid line

for i in range(-400, 550, 50):
    planet.penup()
    planet.goto(i, -400)
    planet.pendown()
    planet.fd(800)

planet.rt(90)

for i in range(-400, 450, 50):
    planet.penup()
    planet.goto(-400, i)
    planet.pendown()
    planet.fd(900)

#key
def label(x, y, color, name):
    planet.penup()
    planet.goto(x, y)
    planet.color(color)
    planet.pendown()
    planet.dot()
    planet.penup()
    planet.fd(20)
    planet.write(name)

label(650, 400, "black", "-- Key")
label(650, 390, "red", "-- Jupiter")
label(650, 380, "orange", "-- Saturn")
label(650, 370, "purple", "-- Uranus")
label(650, 360, "green", "-- Neptune")
label(650, 350, "magenta", "-- Pluto")

#programming the planets
jupiterP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AU,AV").to_numpy()
saturnP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="BC,BD").to_numpy()
uranusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="BK,BL").to_numpy()
neptuneP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="BS,BT").to_numpy()
plutoP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="CA,CB").to_numpy()

jupiter = turtle.Turtle()
jupiter.shape("circle")

saturn = turtle.Turtle()
saturn.shape("circle")

uranus = turtle.Turtle()
uranus.shape("circle")

neptune = turtle.Turtle()
neptune.shape("circle")

pluto = turtle.Turtle()
pluto.shape("circle")

for i in planets:
    print(i)

centre = int(input("Select the centre planet (0 to 4): "))

if centre == 0:
    MAIN = jupiterP
elif centre == 1:
    MAIN = saturnP
elif centre == 2:
    MAIN = uranusP
elif centre == 3:
    MAIN = neptuneP
elif centre == 4:
    MAIN = plutoP

def POSITION(PLANET, PLANETDATA, MAIN):
    PLANET.pu()
    
    x = PLANETDATA[1][0] - MAIN[1][0]
    y = PLANETDATA[1][1] - MAIN[1][1]

    PLANET.goto(x*5, y*5)
    PLANET.pd()

POSITION(jupiter, jupiterP, MAIN)
POSITION(saturn, saturnP, MAIN)
POSITION(uranus, uranusP, MAIN)
POSITION(neptune, neptuneP, MAIN)
POSITION(pluto, plutoP, MAIN)

def ORBIT(PLANETDATA, color, PLANET, MAIN):
    PLANET.color(color)
    
    x = (PLANETDATA[i][0]) - (MAIN[i][0])
    y = (PLANETDATA[i][1]) - (MAIN[i][1])
    
    PLANET.goto(x*5, y*5)

for i in range(1, 15000):

    ORBIT(jupiterP, "red", jupiter, MAIN)
    ORBIT(saturnP, "orange", saturn, MAIN)
    ORBIT(uranusP, "purple", uranus, MAIN)
    ORBIT(neptuneP, "green", neptune, MAIN)
    ORBIT(plutoP, "magenta", pluto, MAIN)

jupiter.ht()
saturn.ht()
uranus.ht()
neptune.ht()
pluto.ht()

planet._update()
planet._tracer(True)
