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

    print(grid)
    
def getCurrentPoint(item):
    if not grid:
        print("grid not yet created! use gridInit(x,y) to create one")

    if not item:
        return

    for y in range(yValue):
        try:
            grid[y].index(item)
            currentY = y
            for x in range(xValue):
                try:
                    grid[currentY][x].index(item)
                    currentX = x
                    return currentY, currentX
                except:
                    pass
        except:
            pass

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
    print("\n")

def gridAdd(x, y, item):
    if not item:
        return

    grid[y][x] = item
