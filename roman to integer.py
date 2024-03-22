class Solution:
    def romanToInt(self, s: str) -> int:
        r={'I':1,'V':5,'X':10,'L':50 ,'C':100 ,'D':500, 'M':1000}
        p=0
        t=0
        for i in s:
            t+=r[i]
            if r[i]>p:
                t-=2*p
            p=r[i]
        return t


        
