"""
You are given an array coordinates, coordinates[i] = [x, y], 
where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        y  =(coordinates[1][1]-coordinates[0][1])
        x  = (coordinates[1][0]-coordinates[0][0])
        if(x == 0):
            return False
        slope = y/x
        
        for i in range(len(coordinates)-1):
            y = (coordinates[i+1][1]-coordinates[i][1])
            x = (coordinates[i+1][0]-coordinates[i][0])
            if(x == 0):
                return False
            s = y/x
            if(s != slope):
                return False
            
        return True
            
        
