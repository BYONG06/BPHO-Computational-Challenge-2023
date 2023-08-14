def c3IP(speed):
    import pandas
    import turtle
    import numpy
    planet = turtle.Turtle()
    planet.speed(10)
    planet.penup()
    planet.goto(-100, 200)
    planet.write("Inner Planets", font=("Courier", 15, "bold"), align = "center")

    #obtaining data from excel
    mercuryxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="L,M").to_numpy()
    venusxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="P,Q").to_numpy()
    earthyxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="T,U").to_numpy()
    marsxy = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 2 (FINAL)", usecols ="X,Y").to_numpy()

    #scale is x100

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
    planet._tracer(False)

    #labelling axes
    for i in range(-200, 250, 50):
        planet.goto(i, 0)
        planet.write((i/100), align="center")

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

    #drawing the orbits of the planets

    planet.hideturtle()

    TYPE(mercuryxy, "red")

    TYPE(venusxy, "orange")

    TYPE(earthyxy, "purple")

    TYPE(marsxy, "green")

    planet._update()
    planet._tracer(True)

    #programming the planets
    mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="M,N").to_numpy()
    venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="U,V").to_numpy()
    earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="AC,AD").to_numpy()
    marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="AK, AL").to_numpy()
    t = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 3 test", usecols ="H").to_numpy()

    mercury = turtle.Turtle()
    mercury.shape("circle")

    venus = turtle.Turtle()
    venus.shape("circle")

    earth = turtle.Turtle()
    earth.shape("circle")

    mars = turtle.Turtle()
    mars.shape("circle")

    def ORBIT(PLANETDATA, color, PLANET):
        PLANET.pu()
        PLANET.color(color)
        
        x = PLANETDATA[i][0]
        y = PLANETDATA[i][1]

        PLANET.goto(x*100, y*100)
    for i in range(1,379, speed):

        ORBIT(mercuryP, "red", mercury)
        ORBIT(venusP, "orange", venus)
        ORBIT(earthP, "purple", earth)
        ORBIT(marsP, "green", mars)
