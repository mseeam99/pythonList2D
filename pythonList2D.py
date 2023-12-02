class Matrix2D:
    def __init__(self, row, column):
        #my2DList = [['_'] * column for _ in range(row)]
        self.my2DList = []
        for i in range(row):
            tempList = []
            for j in range(column):
                tempList.append("_")
            self.my2DList.append(tempList)

    def print2DMatrix(self):
        for i in range(len(self.my2DList)):
            for j in range(len(self.my2DList[i])):
                print(self.my2DList[i][j], end=" ")
            print()
    
    def changeElement(self,rowIndex, columnIndex, newChar):
        self.my2DList[rowIndex][columnIndex] = newChar
        

objectOne = Matrix2D(5, 5)
objectOne.changeElement(2,0,"S")
objectOne.changeElement(2,1,"E")
objectOne.changeElement(2,2,"E")
objectOne.changeElement(2,3,"A")
objectOne.changeElement(2,4,"M")
objectOne.print2DMatrix()

