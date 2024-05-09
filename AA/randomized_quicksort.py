import time
import random

class HoareSort:
    def _quicksort(self, array, low, high):
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot)
            self._quicksort(array, pivot + 1, high)

    def _partition(self, array, low, high):
        pivot = array[low]
        i = low-1
        j = high+1

        while True:
            i+=1
            while array[i] < pivot:
                i += 1
            j-=1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]


    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
        return array

class HoareSortRandomPivot:
    def _quicksort(self, array, low, high):
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot)
            self._quicksort(array, pivot + 1, high)


    def _partition(self, array, low, high):
        pivot_index = random.randint(low, high)
        pivot = array[pivot_index]
        array[low], array[pivot_index] = array[pivot_index], array[low]  # Move pivot to start
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]


    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
        return array

class LumotoSort:
    def _quicksort(self, array, low, high):
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot-1)
            self._quicksort(array, pivot + 1, high)

    def _partition(self, array, low, high):
        pivot = array[high]
        i = low-1

        for j in range(low,high):
            if array[j] < pivot:
                i+=1
                array[i], array[j] = array[j], array[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i+1

    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
        return array

class LumotoSortWithRandomPivot:
    def _quicksort(self, array, low, high):
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot-1)
            self._quicksort(array, pivot + 1, high)

    def _partition(self, array, low, high):
        pivot_index = random.randint(low,high)
        array[high], array[pivot_index] = array[pivot_index], array[high]
        pivot = array[high]
        i = low-1

        for j in range(low,high):
            if array[j] < pivot:
                i+=1
                array[i], array[j] = array[j], array[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i+1


    def sort(self, array):
        self._quicksort(array, 0, len(array) - 1)
        return array

def generate():
    arr = []
    for i in range(1000):
        arr.append(random.randint(1,1000))

    with open('getData.txt','w') as f:
        for a in arr:
            f.write(str(a)+'\n')

generate()


with open('getData.txt','r') as f:
    arr = f.read()
    arr = [ int(x) for x in arr.split() ]


hs = HoareSort()
st = time.time()
sor_arr = hs.sort(arr)
et = time.time()
print(f"Time taken for Hoare partition {et-st}")

hsrp = HoareSortRandomPivot()
st = time.time()
sor_arr = hsrp.sort(arr)
et = time.time()
print(f"Time taken for Hoare partition with random pivot {et-st}")

ls = LumotoSort()
st = time.time()
sor_arr = ls.sort(arr)
et = time.time()
print(f"Time taken for Lumoto partition {et-st}")

lsrp = LumotoSortWithRandomPivot()
st = time.time()
sor_arr = lsrp.sort(arr)
et = time.time()
print(f"Time taken for Lumoto partition with random pivot {et-st}")
