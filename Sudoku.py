



import time
from collections import deque
import numpy as np
import os

    
class Sudoku:     
    def __init__(self, board): 
        self.board = board

    def drawBoard(self): 
        os.system('clear')
        for i in range(0, 9): 
            for x in range(0, 9): 
                print(self.board[i][x], end = "")
            print("\n", end = "")

    def drawBoardEfficiently(self):
        os.system('clear')
        print(np.matrix(self.board))

    def getBox(self, row, col) -> int: 
        if row < 3: 
            if col < 3: 
                return 0
            elif col < 6: 
                return 1
            else: 
                return 2
        elif row < 6: 
            if col < 3: 
                return 3
            elif col < 6: 
                return 4
            else: 
                return 5
        else: 
            if col < 3: 
                return 6
            elif col < 6: 
                return 7
            else: 
                return 8
        
    def getNumbersInRow(self, row) -> list:
        return self.board[row]       
    
    def getNumbersInCol(self, col) -> list:
        arr = []
        for i in range(len(self.board)):
            arr.append(self.board[i][col])
        return arr
    
    def addNumInRow(self, row) -> int: 
        sum = 0
        for num in range(0, 9):
            sum += self.board[row][num]
        return sum
    
    def isRowValid(self, row) -> bool:
        if self.addNumInRow(row) != 45:
            return False
        if len(set(self.getNumbersInRow(row))) != 9: 
            return False
        return True

    def isNumValid(self, row, col, num) -> bool: 
        if num in self.getNumbersInRow(row): 
            return False
        if num in self.getNumbersInCol(col): 
            return False
        return True
    
    def getNumbersInBox(self, row, col) -> list:
        arr = set()
        listOfBoxes = [[[0, 0], [2, 2]], [[0, 3], [2, 5]], [[0, 6], [2, 8]], [[3, 0], [5, 2]], [[3, 3], [5, 5]], [[3, 6], [5, 8]], [[6, 0], [8, 2]], [[6, 3], [8, 5]], [[6, 6], [8, 8]]] 
        box = self.getBox(row, col)
        for row in range(listOfBoxes[box][0][0], listOfBoxes[box][1][0]):
            for col in range(listOfBoxes[box][0][1], listOfBoxes[box][1][1]):
                arr.add(self.board[row][col])
        return list(arr)            
        

    def possibleNumbers(self, row, col) -> list: 
        rowOfNum = set(self.getNumbersInRow(row))
        colOfNum = set(self.getNumbersInCol(col))
        boxOfNum = set(self.getNumbersInBox(row, col))
        arr = []
        for x in range(0, 10): 
            if x not in rowOfNum and x not in colOfNum and x not in boxOfNum:
                arr.append(x)
        return arr
    
    def backTrackBruteForce(self): 
        row = 0
        triedList = dict()
        while row < len(self.board): 
            col = 0
            while col < len(self.board[0]):
                if self.board[row][col] == 0:
                    listOfPossibleNums = self.possibleNumbers(row, col)

                    if (row, col) not in triedList:
                        triedList[(row, col)] = []

                    if len(listOfPossibleNums) != 0:
                        if listOfPossibleNums[0] in triedList[(row, col)]:
                            while len(listOfPossibleNums) != 0 and listOfPossibleNums[0] in triedList[(row, col)]:
                                if len(listOfPossibleNums) != 0:
                                    listOfPossibleNums.remove(listOfPossibleNums[0])

                    if len(listOfPossibleNums) != 0:
                        if listOfPossibleNums[0] not in triedList[(row, col)]:
                            self.board[row][col] = listOfPossibleNums[0]
                            triedList[(row, col)].append(listOfPossibleNums[0])      
                    else: 
                        del triedList[(row, col)]
                        if len(triedList) > 0:
                            row = list(triedList)[len(triedList) - 1][0]
                            col = list(triedList)[len(triedList) - 1][1]
                            self.board[row][col] = 0
                            row = list(triedList)[len(triedList) - 2][0]
                            col = list(triedList)[len(triedList) - 2][1] - 1
                    print("\n")
                    
                col += 1
            row += 1
            

master_arr = [] 
for i in range(0, 9):
    x = input("Enter The Row Of Nums for Sudoku: ")
    arr = [] 
    for num in x: 
        arr.append(int(num))
    master_arr.append(arr)

sudokuSim = Sudoku(master_arr)
sudokuSim.drawBoard()
sudokuSim.backTrackBruteForce()
print("Completed Board: ")
sudokuSim.drawBoard()



