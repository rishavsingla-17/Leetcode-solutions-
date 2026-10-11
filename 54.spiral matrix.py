# here is the code of solution of problem in this i use cyclic structure using 4 var top bottom left and right in this we have to 
# matrix in a spiral manner to first ham loop chlayenge from left to right and us row ke sare elements print krwayenge or top ko ek 
# element increase kr denge fir loop top to bottom and right decrease fir right to left  bottom decrease then bottom to top and left
# increase but bottom to top and right to left only runs when top <= bottom and left <= right this is for when matrix has 1 column or
# 1 row
class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        c = len(matrix[0])
        bottom,right = n-1,c-1
        left,top = 0,0
        result = []
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -=1
            if(left <= right):
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left +=1
        return result 
