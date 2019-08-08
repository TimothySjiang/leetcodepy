class Solution_7:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=x
        x=abs(x) 
        x=str(x)
        x= ' '.join(x)
        x=x.split()
        x.reverse()
        x = int(''.join(x))
        if ((x>2**31-1)|(x<-2**31)):
            return(0)
        if(sign>=0):
            return(x)
        else:
            return(-x)