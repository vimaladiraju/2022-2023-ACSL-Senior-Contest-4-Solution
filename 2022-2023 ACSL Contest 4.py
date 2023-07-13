import math
import os
import random
import re
import sys



#
# Complete the 'missingArrow' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER size
#  2. STRING targets
#  3. STRING numbers
#  4. STRING arrows
#

def missingArrow(size, targets, numbers, arrows):
    grid = [[" " for i in range(size)] for j in range(size)]
    target_list = targets.split(" ")
    for i in target_list:
        grid[int(i[0])][int(i[1])] = "t"

    arrow_list = arrows.split(" ")
    for i in arrow_list:
        grid[int(i[0])][int(i[1])] = i[2]

    number_list = str(numbers).split(" ")
    arrows_in_rows = [0] * size
    arrows_in_columns = [0] * size
    for i in range(len(number_list)):
        if i == 0:
            for j in grid:
                for k in j:
                    if k in "ABCDEFGH":
                        arrows_in_rows[grid.index(j)] += 1
        else:
            for j in range(size):
                for k in grid:
                    if k[j] in "ABCDEFGH":
                        arrows_in_columns[j] += 1


    required_row_arrows = [int(i) for i in list(number_list[0])]
    required_column_arrows = [int(i) for i in list(number_list[1])]
    output = ""
    xpos = ""
    ypos = ""
    for i in range(len(arrows_in_rows)):
        if required_row_arrows[i] != arrows_in_rows[i]:
            xpos += str(i)
            output += xpos
            break
            
    for i in range(len(arrows_in_columns)):
        if required_column_arrows[i] != arrows_in_columns[i]:
            ypos += str(i)
            output += str(i)
            break
    
    new_target_list = target_list
    for i in arrow_list:
        if i[2] == "A":
            for j in range(int(i[1]), 0, -1):
                if grid[int(i[0])][j] == "t":
                    new_target_list.remove(i[0]+str(j))
                    break
        elif i[2] == "C":
             for j in range(int(i[1]), size):
                if grid[int(i[0])][j] == "t":
                    new_target_list.remove(i[0]+str(j))
                    break
        elif i[2] == "B":
            for j in range(int(i[0]), 0, -1):
                if grid[j][int(i[1])] == "t":
                    new_target_list.remove(str(j)+i[1])
                    break
        elif i[2] == "D":
            for j in range(int(i[0]), size):
                if grid[j][int(i[1])] == "t":
                    new_target_list.remove(str(j)+i[1])
                    break
        elif i[2] == "E":
            ypos = int(i[1])-1
            for j in range(int(i[0]), 0, -1):
                if grid[j-1][ypos] == "t":
                    new_target_list.remove(str(str(j-1)+str(ypos)))
                    break    
                ypos -= 1
        elif i[2] == "F":
            ypos = int(i[1])+1
            for j in range(int(i[0]), 0, -1):
                if grid[j-1][ypos] == "t":
                    new_target_list.remove(str(str(j-1)+str(ypos)))
                    break
                ypos += 1
        elif i[2] == "G":
            ypos = int(i[1])+1
            for j in range(int(i[0]), size):
                if grid[j+1][ypos] == "t":
                    new_target_list.remove(str(str(j+1)+str(ypos)))
                    break
                ypos += 1
        elif i[2] == "H":
            ypos = int(i[1])-1
            for j in range(int(i[0]), size):
                if grid[j+1][ypos] == "t":
                    new_target_list.remove(str(str(j+1)+str(ypos)))
                    break
                ypos -= 1

    start_x = new_target_list[-1][0]
    start_y = new_target_list[-1][1]
    end_x = output[0]
    end_y = output[1]

    print(start_x, end_x)
    print(start_y, end_y)
    
    if start_x == end_x and start_y < end_y:
        output += "A"
    elif start_x < end_x and start_y == end_y: # changed
        output += "B"
    elif start_x == end_x and start_y > end_y: # changed, works
        output += "C"
    elif start_x > end_x and start_y == end_y: # changed, works
        output += "D"
    elif start_x < end_x and start_y < end_y: # works
        output += "E"
    elif start_x < end_x and start_y > end_y: # changed
        output += "F"
    elif start_x > end_x and start_y > end_y:
        output += "G"
    else: # works
        output += "H"  

    print(new_target_list)
    return output
    
print(missingArrow(6, "01 10 23 42 53 12 04 52 00", "200232 111024", "05H 34H 35H 54E 55E 40F 45A 41B"))