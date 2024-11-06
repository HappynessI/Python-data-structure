class Maze:
    def __init__(self,mazeFileName):
        rowInMaze=0
        columnsInMaze=0
        self.mazelist=[]
        mazeFile=open(mazeFileName,'r')
        rowsInMaze=0
        for line  in mazeFile:
            rowList=[]
            col=0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch=='S':
                    self.startRow=rowsInMaze
                    self.startRow=col
                col=col+1

            rowInMaze=rowInMaze+1
            self.mazelist.append(rowList)
            columnsInMaze=len(rowList)