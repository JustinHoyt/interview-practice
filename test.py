def minPoints(intervals):
    intervals.sort(key=lambda x:x[1])
    closingVal = -1
    count = 0
    for openPt, closePt in intervals:
        if openPt > closingVal:
            count += 1
            closingVal = closePt
    return count

intervals = [[5,5],[3,8],[6,10]]
intervals2 = [[0,0],[3,7],[9,10]]

print(minPoints(intervals))
