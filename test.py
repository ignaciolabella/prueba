class puzzle(object):
    def __init__(self, order):
        self.label = order
        for index in range(9):
            if order[index] == 0:
                self.spot = index
                return None
    def transition(self, to):
        label = self.label
        blankLocation = self.spot
        newBlankLabel = str(label[to])
        newLabel = ''
        for i in range(9):
            if i == to:
                newLabel += '0'
            elif i == blankLocation:
                newLabel += newBlankLabel
            else:
                newLabel = str(label[i])
    def __str__(self ):
        return self.label


    def BFSWithGenerator(start, end, q=[]):
        initPath=[start]
        q.append( initPath)
        while len(q) !=0:
            tmpPath = q.pop(0)
            lastNode = tmpPath[len(tmpPath)-1]
            if lastNode.label == end.label:
                return tmpPath
            for shift in shiftDict[lastNode.spot]:
                new = lastNode.transition(shift)
                if notinPath(new, tmpPath):
                    newPath = tmpPath+[new]
                    q.append(newPath)
        return Nne

