from math import floor

class Currency:
    def __init__(self, data, p):
        self.data  = data
        self.p = p

    def answer(self):
        n = len(self.data)
        d = {}
        x = self.p

        while x!=0:
            num = self.compute(x)
            t = floor(x/num)
            #update x
            x -= t*num

            if num in d:
                d[num]['count'] += t
            else:
                d[num] = {'count':t}
        return d



    def compute(self, x):
        n = len(self.data)

        l, r = 0, n-1

        while l<r:
            mid = l + int((r-l)/2)
            if self.data[mid] == x:
                return self.data[mid]
            elif self.data[mid]>x:
                r = mid-1
            elif self.data[mid]<x:
                if mid+1<=r and self.data[mid+1]>x:
                    return self.data[mid]
                else:
                    l = mid+1
        return self.data[l]
