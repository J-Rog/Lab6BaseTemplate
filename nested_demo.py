#!/usr/bin/env python3

def print_menu():
    print("1) Print Data")
    print("2) Select Data")
    print("3) Exit")

def display_grid(grid):
    for i in grid:
        print(i)

def select_element(grid):
    
    x = int(input("Please select a x coordinate: "))
    y = int(input("Please select a y coordinate: "))

    #Note that x and y are backwards here
    print(f"The element at x:{x} y:{y} is {grid[y][x]}")

grid = []
r1 = list('abcd')
r2 = list('efgh')
r3 = list('ijkl')
r4 = list('mnop')

grid.append(r1)
grid.append(r2)
grid.append(r3)
grid.append(r4)

print("=====WELCOME TO NESTED DEMO=====")

option = -1

while(option != '3'):
   print_menu()
   option = input("Selection: ")

   if(option == '1'):
       display_grid(grid)
   elif(option == '2'): 
       select_element(grid)
   elif(option == '3'):
       print("Exiting Goodbye and Happy Coding :D")
   else:
       print("INVALID INPUT PLEASE CHOOSE AGAIN")
