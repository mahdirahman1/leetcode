# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Essentially this problem comes down to finding the node which has out degree of 0 
        or in other words no edges coming out of the node
        So for a given node, we can check if they know anyone, if they do then they
        cant be a celebrity
        Brute force:
        for each node from 1 to n, check if they know anyone (n^2)
        """
        
        for i in range(n):
            knows_i = 0
            for j in range(n):
                if i != j:
                    if knows(i,j):
                        break
                    knows_i += knows(j,i)
            else:
                if knows_i == n-1:
                    return i
        
        return -1