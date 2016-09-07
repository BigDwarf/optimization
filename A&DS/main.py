import random
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i],self.heapList[i // 2]
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i],self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

class Sorts:
    def bubblesort(self,list, ascending=True):
        for i in xrange(len(list)):
            for j in xrange(len(list) - i - 1):
                if (list[j] < list[j + 1]):
                    list[j], list[j + 1] = list[j + 1], list[j]
##########QUICK SORT#############
    def quicksort(self,aList):
        self._quicksort(aList, 0, len(aList) - 1)

    def _quicksort(self,aList, first, last):
        if first < last:
            pivot = self.partition(aList, first, last)
            self._quicksort(aList, first, pivot - 1)
            self._quicksort(aList, pivot + 1, last)

    def partition(self, aList, first, last):
        pivot = first + random.randrange(last - first + 1)
        for i in xrange(first, last):
            if aList[i] <= aList[last]:
                self.swap(aList, i, first)
                first += 1

        self.swap(aList, first, last)
        return first

    def swap(self,A, x, y):
        A[x], A[y] = A[y], A[x]

##########COUNTING SORT#############
    def countingsort(self,a):
        scope = max(a) + 1
        c = [0]*scope
        for i in xrange(len(a)):
            c[a[i]] += 1
        for i in xrange (len(c)):
            if not c[i] == 0:
                for j in xrange(c[i]):
                    print i
##########RADIX SORT#############
    def radixsort(self,aList):
        RADIX = 10
        maxLength = False
        tmp, placement = -1, 1

        while not maxLength:
            maxLength = True
            buckets = [list() for _ in range(RADIX)]
            for i in aList:
                tmp = i / placement
                buckets[tmp % RADIX].append(i)
                if maxLength and tmp > 0:
                    maxLength = False
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    aList[a] = i
                    a += 1
            placement *= RADIX
sort = Sorts()
a = [2,3,1,23,3,4,1]
sort.radixsort(a)
print a
