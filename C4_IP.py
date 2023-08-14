def c4IP(speed,viewsetting):
    import numpy as np
    import pandas
    import turtle
    from tabulate import tabulate
    planet = turtle.Turtle()
    planet.speed(10)
    planet.pu()
    planet.ht()
    planet.goto(-100, 200)
    planet.write("Inner Planets", font=("Courier", 15, "bold"), align = "center")

    mercury = turtle.Turtle()
    mercury.shape("circle")

    venus = turtle.Turtle()
    venus.shape("circle")

    earth = turtle.Turtle()
    earth.shape("circle")

    mars = turtle.Turtle()
    mars.shape("circle")

    #in import libs section
    from openpyxl import load_workbook

    workbook = load_workbook(filename="challenge 1 initial.xlsx") #change to book name
    workbook.active = workbook["Challenge 4"] #change to sheet name
    sheet=workbook.active

    view = [["Angled left", -0.35, -0.35, 1, 0, 0, 1],
        ["Footprint", -1, 0, 0, -1, 0, 0],
        ["Draft", -1, 0, 0, 0, 0, 1],
        ["Elevation", 0, 0, 1, 0, 0, 1],
        ["Angled right", -1, 0, 0.35, -0.35, 0, 1],
        ["General ax.", -0.7, -0.35, 0.8, -0.2, 0, 0.8]]

    type = viewsetting

    sheet["C41"] = view[type][1]
    sheet["C42"] = view[type][2]
    sheet["C43"] = view[type][3]
    sheet["C44"] = view[type][4]
    sheet["C45"] = view[type][5]
    sheet["C46"] = view[type][6]

    P1= sheet["C41"].value
    P2= sheet["C42"].value
    Q1= sheet ["C43"].value
    Q2= sheet["C44"].value
    R1= sheet["C45"].value
    R2= sheet ["C46"].value

    mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="P,Q").to_numpy()
    venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="AA,AB").to_numpy()
    earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="AL,AM").to_numpy()
    marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="AW, AX").to_numpy()

    planet._tracer(False) 

    axes=turtle.Turtle()
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
    axes.ht()

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


    for i in range(1, 379, speed):

        PLANET(mercuryP, "red", mercury)
        PLANET(venusP, "orange", venus)
        PLANET(earthP, "purple", earth)
        PLANET(marsP, "green", mars)

