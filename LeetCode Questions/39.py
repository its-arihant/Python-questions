# 2469. Convert the Temperature

class Solution():
    def convertTemperature(self, celsius):
        l=[]
        k=celsius+273.15
        f= (celsius * 1.80) +32.00
        l.append(k)
        l.append(f)
        return l
    
a=Solution()
print(a.convertTemperature(36.50))