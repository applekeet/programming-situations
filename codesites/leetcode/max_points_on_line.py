#
#
#https://leetcode.com/problems/max-points-on-a-line/
#


from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        listNumberOfPointsOnLine = []
        for point in points:
            pass
        
    def pointsOnSingleLine(self, equation, points):
        pass
    
    
    def lineFromPoints(P,Q):
        a = Q[1] - P[1] 
        b = P[0] - Q[0]  
        c = a*(P[0]) + b*(P[1])  

        if(b<0):  
            print("The line passing through points P and Q is:", 
                  a ,"x ",b ,"y = ",c ,"\n")  
        else: 
            print("The line passing through points P and Q is: ", 
                  a ,"x + " ,b ,"y = ",c ,"\n")  

        


