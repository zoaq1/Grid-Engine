from colorama import Fore, init; init()

def gridInit(xLength = 5, yHeight = 5):
    global xValue
    global yValue
    xValue = xLength
    yValue = yHeight

    global grid
    grid = []

    for x in range(xValue):
        grid.append(list(" - " for i in range(yValue)))
    
# not working atm

# def getCurrentPoint(item):
#     if not grid:
#         print("grid not yet created! use gridInit(x,y) to create one")

#     if not item:
#         print("invalid arguements! use getCurrentPoint(item)")

#     try:
#         for y in range(yValue):
#                 grid[y].index(item)
#                 currentY = y
#                 for x in range(xValue):
#                     try:
#                         grid[currentY][x].index(item)
#                         currentX = x
#                         return currentY, currentX
#                     except:
#                         pass
#     except:
#         print("error using getCurrentPoint()! make sure your arguemnts are correct, if this issue still occurs please open an issue at https://github.com/zoaq1/Grid-Engine/issues")

def printGrid(showCoordinates = False):
    if not grid:
        print("grid not yet created! use gridInit(x,y) to create one")

    for y in range(yValue):
        for x in range(xValue):
            point = grid[y][x]
            if point != " - ":
                point = f" {point} "
            if x == xValue - 1 : e = "\n"
            else : e = ""
            print(point,end=e)
    if showCoordinates:
        print(getCurrentPoint())

def gridAdd(x, y, item):
    if not grid:
        print("grid not yet created! use gridInit(x,y) to create one")

    if not item:
        print("invalid arguements! use gridAdd(x,y,symbol")

    grid[y][x] = item