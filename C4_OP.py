def c4OP(speed,viewtype):
    import numpy as np
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

    jupiter = turtle.Turtle()
    jupiter.shape("circle")

    saturn = turtle.Turtle()
    saturn.shape("circle")

    uranus = turtle.Turtle()
    uranus.shape("circle")

    neptune = turtle.Turtle()
    neptune.shape("circle")

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

    type = viewtype

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

    jupiterP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="BJ,BK").to_numpy()
    saturnP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="BU,BV").to_numpy()
    uranusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="CS,CT").to_numpy()
    neptuneP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 4", usecols ="CF,CG").to_numpy()

    planet._tracer(False) 

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


    for i in range(1, 379, speed):

        PLANET(jupiterP, "red", jupiter)
        PLANET(saturnP, "orange", saturn)
        PLANET(uranusP, "purple", uranus)
        PLANET(neptuneP, "green", neptune)

