class Solution:
    def calPoints(self, o: List[str]) -> int:
        l=[]
        for i in o:
    
            if i.isdigit():  # Check if all characters are digits
                l.append(int(i))
            elif i.startswith('-') and i[1:].isdigit():  # Check if it's a ne
                l.append(int(i))
            
            elif i=="+":
                l.append(l[-1]+l[-2])
            elif i=="D":
                l.append(2*l[-1])
            elif i=="C":
                l.pop()
            print(l)
        print(l)
        return sum(l)
