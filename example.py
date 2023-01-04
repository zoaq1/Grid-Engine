import library as ge

ge.gridInit(5,5)
ge.gridAdd(2,4,"i")
ge.printGrid()

# output: 
#  -  -  -  -  - 
#  -  -  -  -  -
#  -  -  -  -  -
#  -  -  -  -  -
#  -  -  i  -  -
#
# the leftmost and topmost side of the grid is 0,
# the "i" is on the 5th row because it started at 0,
# then counted to 4