class Matrix:
    def __init__(self, width, height, *inArray):
        self.width = width
        self.height = height
        StdArr = [[0 for i in range(width)] for j in range(height)]
        if inArray == None:
            self.arr = StdArr
        else:
            for j in range(len(inArray)):
                for i in range(len(inArray[j])):
                    StdArr[j][i] = inArray[j][i]
            self.arr = StdArr.copy()
        self.inArray = inArray

        for j in range(len(inArray)):
            for i in range(len(inArray[j])):
                StdArr[j][i] = inArray[j][i]
        self.arr = StdArr

    def StringArr(self):
        StrArr = ""
        for i in range(len(self.arr)):
            StrArr += "["
            for j in range(len(self.arr[i])):
                StrArr += f"{self.arr[i][j]}"
                if j != len(self.arr[i]) - 1:
                    StrArr += " "
            StrArr += "]\n"
        return StrArr

    def line(self, inLine):
        return self.arr[inLine]

    def column(self, col):
        retList = []
        for i in range(self.height):
            retList.append(self.arr[i][col])
        return retList
