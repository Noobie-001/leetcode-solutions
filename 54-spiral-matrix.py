class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        startrow=0
        endrow=n-1
        startcol=0
        endcol=m-1
        c=0
        total=m*n
        result=[]
        while c<total:
            for i in range(startcol,endcol+1):
                result.append(matrix[startrow][i])
                c+=1
            if c==total:
                break
            startrow+=1

            for i in range(startrow,endrow+1):
                result.append(matrix[i][endcol])
                
                c+=1
            if c==total:
                break
            endcol-=1

            for i in range(endcol,startcol-1,-1):
                result.append(matrix[endrow][i])
                
                c+=1
            if c==total:
                break
            endrow-=1

            for i in range(endrow,startrow-1,-1):
                result.append(matrix[i][startcol])
                
                c+=1
            if c==total:
                break
            startcol+=1
        return result



