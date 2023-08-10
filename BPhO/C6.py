import turtle
import math
import pandas

planet = turtle.Turtle()
planet.speed(10)
planet.penup()

mercuryxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="L,M").to_numpy()
venusxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="R,S").to_numpy()
earthxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="X,Y").to_numpy()
marsxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="AD,AE").to_numpy()
jupiterxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="AJ,AK").to_numpy()
saturnxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="AP,AQ").to_numpy()
uranusxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="AV,AW").to_numpy()
neptuneyxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="BB,BC").to_numpy()
plutoxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="BG,BH").to_numpy()

t = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 6", usecols ="G").to_numpy()

P = [0.241, 0.615, 1, 1.881, 11.861, 29.628, 84.747, 166.43, 248.35]

def planet(planet1, planet2, P2, scale):
    planet = turtle.Turtle()
    planet._tracer(False)
    for i in range(2, 999999):
        x1 = planet1[i][0]
        y1 = planet1[i][1]
        x2 = planet2[i][0]
        y2 = planet2[i][1]
        planet.penup()
        planet.goto(x1*scale, y1*scale)
        planet.pendown()
        planet.goto(x2*scale, y2*scale)
        if t[i] > P2*2:
            break
    planet._update()
    planet._tracer(True)


planet(jupiterxy, saturnxy, P[5], 35)

