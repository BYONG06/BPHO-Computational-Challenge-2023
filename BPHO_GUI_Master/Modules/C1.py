def Challenge1():
    import matplotlib.pyplot as graphing
    from openpyxl import load_workbook
    workbook = load_workbook(filename="Challenge 1 initial.xlsx", data_only=True)

    sheet = workbook["Challenge 1 (FINAL)"]

    x=[]
    y=[]
    for row in sheet:
        tempx = row[8].value
        tempy= row[6].value
        x.append(tempx)
        y.append(tempy)

    removex=[]
    removey=[]
    for i in range (0, len(x)-1, 1):
        if type (x[i]) != float and type (x[i]) != int:
            removex.append(x[i])
    for i in range (0, len(y)-1, 1):
        if type (y[i]) != float and type (y[i]) != int:
            removey.append(y[i])
    for i in removex:
        x.remove(i)
    for i in removey:
        y.remove(i)

    fig = graphing.figure("Challenge 1")
    graphing.plot(x, y, 'o', color="blue")
    graphing.plot (x, y, color="red")

    graphing.title("Kepler's Third Law")
    graphing.xlabel('(a/AU)^(3/2)')
    graphing.ylabel('T/Yr')
    graphing.text(-5, 120, 'T/Yr = (R/AU)^(3/2)', fontsize = 12, 
             bbox = dict(facecolor = 'red', alpha = 0.5))

    graphing.legend(["Kepler's Third Law", "Linear (Kepler's Third Law)"], loc = "upper right")
    graphing.show()