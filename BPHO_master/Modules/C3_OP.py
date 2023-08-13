def c3OP(speed):
    import pandas
    import turtle
    import numpy
    planet = turtle.Turtle()
    planet.speed(10)
    planet.penup()
    planet.goto(-250, 410)
    planet.write("Outer Planets", font=("Courier", 30, "bold"), align = "center")

    #obtaining data from excel

    jupiterxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AB,AC").to_numpy()
    saturnxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AF,AG").to_numpy()
    uranusxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AJ,AK").to_numpy()
    neptuneyxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AN,AO").to_numpy()
    plutoxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="AR,AS").to_numpy()

    #scale is x100

    def TYPE(PLANET, color):
        planet.penup()

        for i in range(1,1001):
            planet.color(color)

            x = PLANET[i][0]
            y = PLANET[i][1]

            planet.goto(x*10, y*10)
            planet.pendown()

        planet.goto(PLANET[1][0]*10, PLANET[1][1]*10)
        planet.hideturtle()

    #drawing the axes

    planet.color("black")
    planet._tracer(False)

    #labelling axes
    for i in range(-400, 600, 100):
        planet.goto(i, 0)
        planet.write(i/10)

    planet.goto(525, 0)
    planet.write("x/AU")

    planet.lt(90)

    for i in range(-400, 500, 100):
        planet.goto(0, i)
        planet.write(i/10)

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

    label(650, 400, "black", "-- Key")
    label(650, 390, "red", "-- Jupiter")
    label(650, 380, "orange", "-- Saturn")
    label(650, 370, "purple", "-- Uranus")
    label(650, 360, "green", "-- Neptune")
    label(650, 350, "magenta", "-- Pluto")

    #drawing the planets

    TYPE(jupiterxy, "red")

    TYPE(saturnxy, "orange")

    TYPE(uranusxy, "purple")

    TYPE(neptuneyxy, "green")

    TYPE(plutoxy, "magenta")

    planet._update()
    planet._tracer(True)

    #programming the planets
    jupiterP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="AU,AV").to_numpy()
    saturnP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="BC,BD").to_numpy()
    uranusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="BK,BL").to_numpy()
    neptuneP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="BS,BT").to_numpy()
    plutoP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="CA,CB").to_numpy()
    t = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="AO").to_numpy()

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

    def ORBIT(PLANETDATA, color, PLANET):
        PLANET.pu()
        PLANET.color(color)
        
        x = PLANETDATA[i][0]
        y = PLANETDATA[i][1]

        PLANET.goto(x*10, y*10)

    for i in range(2,379, speed):

        ORBIT(jupiterP, "red", jupiter)
        ORBIT(saturnP, "orange", saturn)
        ORBIT(uranusP, "purple", uranus)
        ORBIT(neptuneP, "green", neptune)
        ORBIT(plutoP, "magenta", pluto)
