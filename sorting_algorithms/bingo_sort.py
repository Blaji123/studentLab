from generic_sort.generic_sort import GenericSort
class BingoSort(GenericSort):
    def __init__(self,col,key,reverse):
        super().__init__(col,key,reverse)

    def sort(self):
        mini = 10_000_000
        miniStr = "zzzzzzzzzzzzzzz"
        largest = 0
        largestStr = "A"
        for i in range(0,len(self.col)):
            if type(self.key(self.col[i])) is str:
                if self.key(self.col[i]) < miniStr:
                    miniStr = self.key(self.col[i])
            else:
                if self.key(self.col[i]) < mini:
                    mini = self.key(self.col[i])
        for i in range(0,len(self.col)):
            if type(self.key(self.col[i])) is str:
                if self.key(self.col[i]) > largestStr:
                    largestStr = self.key(self.col[i])
            else:
                if self.key(self.col[i]) > largest:
                    largest = self.key(self.col[i])
        if type(self.key(self.col[0])) is str:
            bingo = miniStr
            nextBingo = largestStr
        else:
            bingo = mini
            nextBingo = largest
        nextPos = 0
        while bingo < nextBingo:
            startPos = nextPos
            for i in range(startPos, len(self.col)):
                if self.key(self.col[i]) == bingo:
                    self.col[i], self.col[nextPos] = self.col[nextPos], self.col[i]
                    nextPos += 1
                elif self.key(self.col[i]) < nextBingo:
                    nextBingo = self.key(self.col[i])
            bingo = nextBingo
            if type(self.key(self.col[0])) is str:
                nextBingo = largestStr
            else:
                nextBingo = largest
        if self.reverse == True:
            self.col.reverse()