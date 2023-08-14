from openpyxl import load_workbook
import pandas
import turtle
import numpy
from tabulate import tabulate

def ME():
    planet = turtle.Turtle()
    planet.speed(10)
    planet.penup()
    planet.goto(-300, 300)
    planet.write("Inner Planets", font=("Courier", 15, "bold"), align = "center")

    planets = ["0 Mercury", "1 Venus", "2 Earth", "3 Mars"]
        
    #drawing the axes

    planet.color("black")
    planet._tracer(False)

    #labelling axes
    for i in range(-300, 350, 50):
        planet.goto(i, 0)
        planet.write((i/100), align="center")

    planet.goto(325, 0)
    planet.write("x/AU")

    planet.lt(90)

    for i in range(-300, 350, 50):
        planet.goto(0, i)
        planet.write(i/100)

    planet.goto(0, 325)
    planet.write("y/AU")


    #drawing grid line

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(i, -300)
        planet.pendown()
        planet.fd(600)

    planet.rt(90)

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(-300, i)
        planet.pendown()
        planet.fd(600)

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

    label(350, 210, "black", "-- Key")
    label(350, 200, "red", "-- Mercury")
    label(350, 190, "orange", "-- Venus")
    label(350, 180, "purple", "-- Earth")
    label(350, 170, "green", "-- Mars")

    #drawing the orbits of the planets

    planet.hideturtle()

    #programming the planets
    mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="M,N").to_numpy()
    venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="U,V").to_numpy()
    earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AC,AD").to_numpy()
    marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AK, AL").to_numpy()

    mercury = turtle.Turtle()
    mercury.shape("circle")

    venus = turtle.Turtle()
    venus.shape("circle")

    earth = turtle.Turtle()
    earth.shape("circle")

    mars = turtle.Turtle()
    mars.shape("circle")

    def POSITION(PLANET, PLANETDATA, mercuryP):
        PLANET.pu()
        
        x = PLANETDATA[1][0] - mercuryP[1][0]
        y = PLANETDATA[1][1] - mercuryP[1][1]

        PLANET.goto(x*100, y*100)
        PLANET.pd()

    POSITION(mercury, mercuryP, mercuryP)
    POSITION(venus, venusP, mercuryP)
    POSITION(earth, earthP, mercuryP)
    POSITION(mars, marsP, mercuryP)

    def ORBIT(PLANETDATA, color, PLANET, mercuryP):
        PLANET.color(color)
        
        x = (PLANETDATA[i][0]) - (mercuryP[i][0])
        y = (PLANETDATA[i][1]) - (mercuryP[i][1])

        PLANET.goto(x*100, y*100)

    for i in range(1, 10001):

        ORBIT(mercuryP, "red", mercury, mercuryP)
        ORBIT(venusP, "orange", venus, mercuryP)
        ORBIT(earthP, "purple", earth, mercuryP)
        ORBIT(marsP, "green", mars, mercuryP)

    mercury.ht()
    venus.ht()
    earth.ht()
    mars.ht()

    planet._update()
    planet._tracer(True)

def VE():
    planet = turtle.Turtle()
    planet.speed(10)
    planet.penup()
    planet.goto(-300, 300)
    planet.write("Inner Planets", font=("Courier", 15, "bold"), align = "center")

    planets = ["0 Mercury", "1 Venus", "2 Earth", "3 Mars"]
        
    #drawing the axes

    planet.color("black")
    planet._tracer(False)

    #labelling axes
    for i in range(-300, 350, 50):
        planet.goto(i, 0)
        planet.write((i/100), align="center")

    planet.goto(325, 0)
    planet.write("x/AU")

    planet.lt(90)

    for i in range(-300, 350, 50):
        planet.goto(0, i)
        planet.write(i/100)

    planet.goto(0, 325)
    planet.write("y/AU")


    #drawing grid line

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(i, -300)
        planet.pendown()
        planet.fd(600)

    planet.rt(90)

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(-300, i)
        planet.pendown()
        planet.fd(600)

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

    label(350, 210, "black", "-- Key")
    label(350, 200, "red", "-- Mercury")
    label(350, 190, "orange", "-- Venus")
    label(350, 180, "purple", "-- Earth")
    label(350, 170, "green", "-- Mars")

    #drawing the orbits of the planets

    planet.hideturtle()

    #programming the planets
    mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="M,N").to_numpy()
    venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="U,V").to_numpy()
    earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AC,AD").to_numpy()
    marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AK, AL").to_numpy()

    mercury = turtle.Turtle()
    mercury.shape("circle")

    venus = turtle.Turtle()
    venus.shape("circle")

    earth = turtle.Turtle()
    earth.shape("circle")

    mars = turtle.Turtle()
    mars.shape("circle")

    def POSITION(PLANET, PLANETDATA, venusP):
        PLANET.pu()
        
        x = PLANETDATA[1][0] - venusP[1][0]
        y = PLANETDATA[1][1] - venusP[1][1]

        PLANET.goto(x*100, y*100)
        PLANET.pd()

    POSITION(mercury, mercuryP, venusP)
    POSITION(venus, venusP, venusP)
    POSITION(earth, earthP, venusP)
    POSITION(mars, marsP, venusP)

    def ORBIT(PLANETDATA, color, PLANET, venusP):
        PLANET.color(color)
        
        x = (PLANETDATA[i][0]) - (venusP[i][0])
        y = (PLANETDATA[i][1]) - (venusP[i][1])

        PLANET.goto(x*100, y*100)

    for i in range(1, 10001):

        ORBIT(mercuryP, "red", mercury, venusP)
        ORBIT(venusP, "orange", venus, venusP)
        ORBIT(earthP, "purple", earth, venusP)
        ORBIT(marsP, "green", mars, venusP)

    mercury.ht()
    venus.ht()
    earth.ht()
    mars.ht()

    planet._update()
    planet._tracer(True)

def EA():
    planet = turtle.Turtle()
    planet.speed(10)
    planet.penup()
    planet.goto(-300, 300)
    planet.write("Inner Planets", font=("Courier", 15, "bold"), align = "center")

    planets = ["0 Mercury", "1 Venus", "2 Earth", "3 Mars"]
        
    #drawing the axes

    planet.color("black")
    planet._tracer(False)

    #labelling axes
    for i in range(-300, 350, 50):
        planet.goto(i, 0)
        planet.write((i/100), align="center")

    planet.goto(325, 0)
    planet.write("x/AU")

    planet.lt(90)

    for i in range(-300, 350, 50):
        planet.goto(0, i)
        planet.write(i/100)

    planet.goto(0, 325)
    planet.write("y/AU")


    #drawing grid line

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(i, -300)
        planet.pendown()
        planet.fd(600)

    planet.rt(90)

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(-300, i)
        planet.pendown()
        planet.fd(600)

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

    label(350, 210, "black", "-- Key")
    label(350, 200, "red", "-- Mercury")
    label(350, 190, "orange", "-- Venus")
    label(350, 180, "purple", "-- Earth")
    label(350, 170, "green", "-- Mars")

    #drawing the orbits of the planets

    planet.hideturtle()

    #programming the planets
    mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="M,N").to_numpy()
    venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="U,V").to_numpy()
    earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AC,AD").to_numpy()
    marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AK, AL").to_numpy()

    mercury = turtle.Turtle()
    mercury.shape("circle")

    venus = turtle.Turtle()
    venus.shape("circle")

    earth = turtle.Turtle()
    earth.shape("circle")

    mars = turtle.Turtle()
    mars.shape("circle")


    def POSITION(PLANET, PLANETDATA, earthP):
        PLANET.pu()
        
        x = PLANETDATA[1][0] - earthP[1][0]
        y = PLANETDATA[1][1] - earthP[1][1]

        PLANET.goto(x*100, y*100)
        PLANET.pd()

    POSITION(mercury, mercuryP, earthP)
    POSITION(venus, venusP, earthP)
    POSITION(earth, earthP, earthP)
    POSITION(mars, marsP, earthP)

    def ORBIT(PLANETDATA, color, PLANET, earthP):
        PLANET.color(color)
        
        x = (PLANETDATA[i][0]) - (earthP[i][0])
        y = (PLANETDATA[i][1]) - (earthP[i][1])

        PLANET.goto(x*100, y*100)

    for i in range(1, 10001):

        ORBIT(mercuryP, "red", mercury, earthP)
        ORBIT(venusP, "orange", venus, earthP)
        ORBIT(earthP, "purple", earth, earthP)
        ORBIT(marsP, "green", mars, earthP)

    mercury.ht()
    venus.ht()
    earth.ht()
    mars.ht()

    planet._update()
    planet._tracer(True)

def MA():
    planet = turtle.Turtle()
    planet.speed(10)
    planet.penup()
    planet.goto(-300, 300)
    planet.write("Inner Planets", font=("Courier", 15, "bold"), align = "center")

    planets = ["0 Mercury", "1 Venus", "2 Earth", "3 Mars"]
        
    #drawing the axes

    planet.color("black")
    planet._tracer(False)

    #labelling axes
    for i in range(-300, 350, 50):
        planet.goto(i, 0)
        planet.write((i/100), align="center")

    planet.goto(325, 0)
    planet.write("x/AU")

    planet.lt(90)

    for i in range(-300, 350, 50):
        planet.goto(0, i)
        planet.write(i/100)

    planet.goto(0, 325)
    planet.write("y/AU")


    #drawing grid line

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(i, -300)
        planet.pendown()
        planet.fd(600)

    planet.rt(90)

    for i in range(-300, 350, 50):
        planet.penup()
        planet.goto(-300, i)
        planet.pendown()
        planet.fd(600)

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

    label(350, 210, "black", "-- Key")
    label(350, 200, "red", "-- Mercury")
    label(350, 190, "orange", "-- Venus")
    label(350, 180, "purple", "-- Earth")
    label(350, 170, "green", "-- Mars")

    #drawing the orbits of the planets

    planet.hideturtle()

    #programming the planets
    mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="M,N").to_numpy()
    venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="U,V").to_numpy()
    earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AC,AD").to_numpy()
    marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7", usecols ="AK, AL").to_numpy()

    mercury = turtle.Turtle()
    mercury.shape("circle")

    venus = turtle.Turtle()
    venus.shape("circle")

    earth = turtle.Turtle()
    earth.shape("circle")

    mars = turtle.Turtle()
    mars.shape("circle")


    def POSITION(PLANET, PLANETDATA, marsP):
        PLANET.pu()
        
        x = PLANETDATA[1][0] - marsP[1][0]
        y = PLANETDATA[1][1] - marsP[1][1]

        PLANET.goto(x*100, y*100)
        PLANET.pd()

    POSITION(mercury, mercuryP, marsP)
    POSITION(venus, venusP, marsP)
    POSITION(earth, earthP, marsP)
    POSITION(mars, marsP, marsP)

    def ORBIT(PLANETDATA, color, PLANET, marsP):
        PLANET.color(color)
        
        x = (PLANETDATA[i][0]) - (marsP[i][0])
        y = (PLANETDATA[i][1]) - (marsP[i][1])

        PLANET.goto(x*100, y*100)

    for i in range(1, 10001):

        ORBIT(mercuryP, "red", mercury, marsP)
        ORBIT(venusP, "orange", venus, marsP)
        ORBIT(earthP, "purple", earth, marsP)
        ORBIT(marsP, "green", mars, marsP)

    mercury.ht()
    venus.ht()
    earth.ht()
    mars.ht()

    planet._update()
    planet._tracer(True)




