def IP72(viewpoint, chosen):
    from openpyxl import load_workbook
    import pandas
    import turtle
    import numpy
    from tabulate import tabulate
    planet = turtle.Turtle()
    planet.speed(10)
    planet.ht()
    planet.pu()
    planet._tracer(False)
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


    workbook = load_workbook(filename="Challenge 1 initial.xlsx") #change to book name
    workbook.active = workbook["Challenge 4"] #change to sheet name
    sheet=workbook.active

    type = viewpoint

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

    P1= sheet["C41"].value
    P2= sheet["C42"].value
    Q1= sheet ["C43"].value
    Q2= sheet["C44"].value
    R1= sheet["C45"].value
    R2= sheet ["C46"].value

    mercuryP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7.2", usecols ="P,Q").to_numpy()
    venusP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7.2", usecols ="AA,AB").to_numpy()
    earthP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7.2", usecols ="AL,AM").to_numpy()
    marsP = pandas.read_excel("Challenge 1 initial.xlsx", sheet_name="Challenge 7.2", usecols ="AW, AX").to_numpy()
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

    centre = chosen
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

    '''
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
    '''

    def PLANET(PLANETDATA, color, PLANET, MAIN):
        PLANET.color(color)

        x = PLANETDATA[i][0] - MAIN[i][0]
        y = PLANETDATA[i][1] - MAIN[i][1]

        PLANET.goto(x*100, y*100)
        

    for i in range(2, 1200):

        PLANET(mercuryP, "red", mercury, MAIN)
        PLANET(venusP, "orange", venus, MAIN)
        PLANET(earthP, "purple", earth, MAIN)
        PLANET(marsP, "green", mars, MAIN)

    mercury.ht()
    venus.ht()
    earth.ht()
    mars.ht()

    planet._update()
    planet._tracer(True)

