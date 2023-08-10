import pandas
import turtle
import numpy as np
from tabulate import tabulate

planet = turtle.Turtle()
planet.speed(10)
planet.ht()
planet.pu()
planet.goto(-250, 410)
planet.write("Outer Planets", font=("Courier", 30, "bold"), align = "center")

jupiterP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="BJ,BK").to_numpy()
saturnP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="BU,BV").to_numpy()
uranusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="CF,CG").to_numpy()
neptuneP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="CS,CT").to_numpy()

jupiter = turtle.Turtle()
jupiter.shape("circle")

saturn = turtle.Turtle()
saturn.shape("circle")

uranus = turtle.Turtle()
uranus.shape("circle")

neptune = turtle.Turtle()
neptune.shape("circle")

#creating the view's data table
view = [["Angled left", -0.35, -0.35, 1, 0, 0, 1],
        ["Footprint", -1, 0, 0, -1, 0, 0],
        ["Draft", -1, 0, 0, 0, 0, 1],
        ["Elevation", 0, 0, 1, 0, 0, 1],
        ["Angled right", -1, 0, 0.35, -0.35, 0, 1],
        ["General ax.", -0.7, -0.35, 0.8, -0.2, 0, 0.8]]

col_names = ["View type", "p1", "p2", "q1", "q2", "r1", "r2"]

print("List of view types available:")
print("\n")
print(tabulate(view, headers=col_names, tablefmt="fancy_grid", showindex="always"))
print("\n")

#in import libs section
from openpyxl import load_workbook
#you should already have this if you have pandas installed


workbook = load_workbook(filename="challenge 1 initial.xlsx") #change to book name
workbook.active = workbook["Challenge 4"] #change to sheet name
sheet=workbook.active
print ("Rotation configuration - refer to table for full details of inputs.")
print ("Typical input: P1/P2 = -0.35, Q1/R2=1, Q2/R1=0")

type = int(input("Select a view type using the index numbers on the table: "))

#Go straight to asking for inputs for P1/P2/Q1/Q2/R1/R2
#I can make it so that it prints current settings and asks if you want
#to change it if you would like
#I don't know what constraints on P/Q/R 1/2 need to be added
sheet["C41"] = view[type][1]
sheet["C42"] = view[type][2]
sheet["C43"] = view[type][3]
sheet["C44"] = view[type][4]
sheet["C45"] = view[type][5]
sheet["C46"] = view[type][6]

workbook.save(filename="spreadsheet tasks.xlsx") #change to book name once again (same name as prev)
#With this the new values for P/Q/R 1/2 have been saved
#This should update the values for the orbits accordingly
#because did some tests on a test sheet which shows updating one cell
#updates cells that use a formula with said cell in it

P1= sheet["C41"].value
P2= sheet["C42"].value
Q1= sheet ["C43"].value
Q2= sheet["C44"].value
R1= sheet["C45"].value
R2= sheet ["C46"].value

#and this bit remains unchanged from previous code I sent you
axes=turtle.Turtle()
axes.ht()
axes.pu()
axes.goto(-400*R1,-400*R2)
axes.pd()
axes.goto(400*R1,400*R2)
axes.pu()
axes.goto(-400*Q1,-400*Q2)
axes.pd()
axes.goto(400*Q1,400*Q2)
axes.pu()
axes.goto(-400*P1,-400*P2)
axes.pd()
axes.goto(400*P1,400*P2)
axes.pu()

def label(var1, var2):
    for i in range (-400,450,50):
        axes.goto(i*var1,i*var2)
        axes.write((i/10), align="center")
label(P1,P2)
label(R1,R2)
label(Q1,Q2)

axes.goto(450*P1, 450*P2)
axes.write("x/AU")
axes.goto(450*Q1, 450*Q2)
axes.write("y/AU")
axes.goto(450*R1, 450*R2)
axes.write("z/AU")

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

def POSITION(PLANET, PLANETDATA):
    PLANET.pu()
    
    x = PLANETDATA[1][0]
    y = PLANETDATA[1][1]

    PLANET.goto(x*10, y*10)
    PLANET.pd()

POSITION(jupiter, jupiterP)
POSITION(saturn, saturnP)
POSITION(uranus, uranusP)
POSITION(neptune, neptuneP)

def ORBIT(PLANETDATA, color, PLANET):
    PLANET.color(color)
    
    x = PLANETDATA[i][0]
    y = PLANETDATA[i][1]

    PLANET.goto(x*10, y*10)

planet._tracer(False)    

for i in range(1, 379):

    ORBIT(jupiterP, "red", jupiter)
    ORBIT(saturnP, "orange", saturn)
    ORBIT(uranusP, "purple", uranus)
    ORBIT(neptuneP, "green", neptune)

planet._update()
planet._tracer(True)

jupiter.pu()
saturn.pu()
uranus.pu()
neptune.pu()

def PLANET(PLANETDATA, color, PLANET):
    PLANET.color(color)

    x = PLANETDATA[i][0]
    y = PLANETDATA[i][1]

    PLANET.goto(x*10, y*10)

    
FR = int(input("Input the speed of the orbiting planets (1 to 20): "))
while (not 1<=FR) and (not FR<=20):
    FR = int(input("Input the speed of the orbiting planets (1 to 20): "))

for i in range(1, 379, FR):

    PLANET(jupiterP, "red", jupiter)
    PLANET(saturnP, "orange", saturn)
    PLANET(uranusP, "purple", uranus)
    PLANET(neptuneP, "green", neptune)
