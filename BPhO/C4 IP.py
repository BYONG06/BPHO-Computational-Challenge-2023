import pandas
import turtle
import numpy as np
from tabulate import tabulate

planet = turtle.Turtle()
planet.speed(10)
planet.ht()
planet.goto(-100, 200)
planet.write("Inner Planets", font=("Courier", 15, "bold"), align = "center")

mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="P,Q").to_numpy()
venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="AA,AB").to_numpy()
earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="AL,AM").to_numpy()
marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="AW, AX").to_numpy()

mercury = turtle.Turtle()
mercury.shape("circle")

venus = turtle.Turtle()
venus.shape("circle")

earth = turtle.Turtle()
earth.shape("circle")

mars = turtle.Turtle()
mars.shape("circle")

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
axes.goto(-200*R1,-200*R2)
axes.pd()
axes.goto(200*R1,200*R2)
axes.pu()
axes.goto(-200*Q1,-200*Q2)
axes.pd()
axes.goto(200*Q1,200*Q2)
axes.pu()
axes.goto(-200*P1,-200*P2)
axes.pd()
axes.goto(200*P1,200*P2)
axes.pu()

def label(var1, var2):
    for i in range (-200,250,50):
        axes.goto(i*var1,i*var2)
        axes.write((i/100), align="center")
label(P1,P2)
label(R1,R2)
label(Q1,Q2)

axes.goto(250*P1, 250*P2)
axes.write("x/AU")
axes.goto(250*Q1, 250*Q2)
axes.write("y/AU")
axes.goto(250*R1, 250*R2)
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

label(250, 210, "black", "-- Key")
label(250, 200, "red", "-- Mercury")
label(250, 190, "orange", "-- Venus")
label(250, 180, "purple", "-- Earth")
label(250, 170, "green", "-- Mars")

def POSITION(PLANET, PLANETDATA):
    PLANET.pu()
    
    x = PLANETDATA[1][0]
    y = PLANETDATA[1][1]

    PLANET.goto(x*100, y*100)
    PLANET.pd()

POSITION(mercury, mercuryP)
POSITION(venus, venusP)
POSITION(earth, earthP)
POSITION(mars, marsP)

def ORBIT(PLANETDATA, color, PLANET):
    PLANET.color(color)
    
    x = PLANETDATA[i][0]
    y = PLANETDATA[i][1]

    PLANET.goto(x*100, y*100)

planet._tracer(False)    

for i in range(1, 379):

    ORBIT(mercuryP, "red", mercury)
    ORBIT(venusP, "orange", venus)
    ORBIT(earthP, "purple", earth)
    ORBIT(marsP, "green", mars)

planet._update()
planet._tracer(True)

mercury.pu()
venus.pu()
earth.pu()
mars.pu()

def PLANET(PLANETDATA, color, PLANET):
    PLANET.color(color)

    x = PLANETDATA[i][0]
    y = PLANETDATA[i][1]

    PLANET.goto(x*100, y*100)

    
FR = int(input("Input the speed of the orbiting planets (1 to 20): "))
while (not 1<=FR) and (not FR<=20):
    FR = int(input("Input the speed of the orbiting planets (1 to 20): "))

for i in range(1, 379, FR):

    PLANET(mercuryP, "red", mercury)
    PLANET(venusP, "orange", venus)
    PLANET(earthP, "purple", earth)
    PLANET(marsP, "green", mars)
