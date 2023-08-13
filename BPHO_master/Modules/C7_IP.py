def IP71():
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

    for i in planets:
        print(i)
    centre = int(input("Select the centre planet (0 to 3): "))

    if centre == 0:
        MAIN = mercuryP
    elif centre == 1:
        MAIN = venusP
    elif centre == 2:
        MAIN = earthP
    elif centre == 3:
        MAIN = marsP

    def POSITION(PLANET, PLANETDATA, MAIN):
        PLANET.pu()
        
        x = PLANETDATA[1][0] - MAIN[1][0]
        y = PLANETDATA[1][1] - MAIN[1][1]

        PLANET.goto(x*100, y*100)
        PLANET.pd()

    POSITION(mercury, mercuryP, MAIN)
    POSITION(venus, venusP, MAIN)
    POSITION(earth, earthP, MAIN)
    POSITION(mars, marsP, MAIN)

    def ORBIT(PLANETDATA, color, PLANET, MAIN):
        PLANET.color(color)
        
        x = (PLANETDATA[i][0]) - (MAIN[i][0])
        y = (PLANETDATA[i][1]) - (MAIN[i][1])

        PLANET.goto(x*100, y*100)

    for i in range(1, 10001):

        ORBIT(mercuryP, "red", mercury, MAIN)
        ORBIT(venusP, "orange", venus, MAIN)
        ORBIT(earthP, "purple", earth, MAIN)
        ORBIT(marsP, "green", mars, MAIN)

    mercury.ht()
    venus.ht()
    earth.ht()
    mars.ht()

    planet._update()
    planet._tracer(True)

