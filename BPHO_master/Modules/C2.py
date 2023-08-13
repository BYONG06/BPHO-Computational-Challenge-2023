class Challenge2():
    import matplotlib.pyplot as graphing
    from openpyxl import load_workbook
    workbook = load_workbook(filename="Challenge 1 initial.xlsx", data_only=True)

    sheet = workbook["Challenge 2 (FINAL)"]
    '''
    for cell in sheet["J"]:
            print(f"{cell.column_letter}{cell.row} = {cell.value}")
    '''
    mercuryx=[]
    mercuryy=[]
    venusx=[]
    venusy=[]
    earthx=[]
    earthy=[]
    marsx=[]
    marsy=[]
    jupiterx=[]
    jupitery=[]
    saturnx=[]
    saturny=[]
    uranusx=[]
    uranusy=[]
    neptunex=[]
    neptuney=[]
    plutox=[]
    plutoy=[]


    for row in sheet:
        mercuryx.append(row[11].value)
        mercuryy.append(row[12].value)
        venusx.append(row[15].value)
        venusy.append(row[16].value)
        earthx.append(row[19].value)
        earthy.append(row[20].value)
        marsx.append(row[23].value)
        marsy.append(row[24].value)
        jupiterx.append(row[27].value)
        jupitery.append(row[28].value)
        saturnx.append(row[31].value)
        saturny.append(row[32].value)
        uranusx.append(row[35].value)
        uranusy.append(row[36].value)
        neptunex.append(row[39].value)
        neptuney.append(row[40].value)
        plutox.append(row[43].value)
        plutoy.append(row[44].value)

    def removechars(x):
        removex=[]
        for i in range (0, len(x)-1, 1):
            if type (x[i]) != float and type (x[i]) != int:
                removex.append(x[i])
        for i in removex:
            x.remove(i)
        return x

    mercuryx=removechars(mercuryx)
    mercuryy=removechars(mercuryy)
    venusx=removechars(venusx)
    venusy=removechars(venusy)
    earthx=removechars(earthx)
    earthy=removechars(earthy)
    marsx=removechars(marsx)
    marsy=removechars(marsy)
    jupiterx=removechars(jupiterx)
    jupitery=removechars(jupitery)
    saturnx=removechars(saturnx)
    saturny=removechars(saturny)
    uranusx=removechars(uranusx)
    uranusy=removechars(uranusy)
    neptunex=removechars(neptunex)
    neptuney=removechars(neptuney)
    plutox=removechars(plutox)
    plutoy=removechars(plutoy)

    fig = graphing.figure("Challenge 2 - Innner Planets")
    graphing.title("Eliptical Orbits")
    graphing.xlabel('x/AU')
    graphing.ylabel('y/AU')

    graphing.plot(mercuryx,mercuryy)
    graphing.plot(earthx,earthy)
    graphing.plot(venusx,venusy)
    graphing.plot(marsx,marsy)
    graphing.legend(["Mercury", "Venus", "Earth", "Mars"], loc = "upper right")

    fig = graphing.figure("Challenge 2 - Outer Planets")
    graphing.title("Eliptical Orbits")
    graphing.xlabel('x/AU')
    graphing.ylabel('y/AU')

    graphing.plot(jupiterx, jupitery)
    graphing.plot(saturnx, saturny)
    graphing.plot(uranusx, uranusy)
    graphing.plot(neptunex, neptuney)
    graphing.plot(plutox, plutoy)
    graphing.legend(["Jupiter", "Saturn", "Neptune", "Pluto"], loc = "upper right")

    fig = graphing.figure("Challenge 2 - Milky Way Planets")
    graphing.title("Eliptical Orbits")
    graphing.xlabel('x/AU')
    graphing.ylabel('y/AU')

    graphing.plot(mercuryx,mercuryy)
    graphing.plot(earthx,earthy)
    graphing.plot(venusx,venusy)
    graphing.plot(marsx,marsy)
    graphing.plot(jupiterx, jupitery)
    graphing.plot(saturnx, saturny)
    graphing.plot(uranusx, uranusy)
    graphing.plot(neptunex, neptuney)
    graphing.plot(plutox, plutoy)
    graphing.legend(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Pluto"], loc = "upper right")



    graphing.show()
