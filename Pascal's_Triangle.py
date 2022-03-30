def generate(self, numRows: int) -> List[List[int]]:
        retVal = [[1]]
        tmpVal = []
        
        for i in range(1, numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    tmpVal.append(1)
                else:
                    value = retVal[i-1][j-1] + retVal[i-1][j]
                    tmpVal.append(value)
            retVal.append(tmpVal.copy())
            tmpVal.clear()
        return retVal
