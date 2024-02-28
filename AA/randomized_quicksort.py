import time
import random

class HoareSort:
    def _quicksort(self, array: list, low: int, high: int) -> None:
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot)
            self._quicksort(array, pivot + 1, high)

    def _partition(self, array: list, low: int, high: int) -> int:
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


    def sort(self, array: list) -> list:
        self._quicksort(array, 0, len(array) - 1)
        return array

class HoareSortRandomPivot:
    def _quicksort(self, array: list, low: int, high: int) -> None:
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot)
            self._quicksort(array, pivot + 1, high)


    def _partition(self, array: list, low: int, high: int) -> int:
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


    def sort(self, array: list) -> list:
        self._quicksort(array, 0, len(array) - 1)
        return array

class HoareSortRandom_ij:
    def _quicksort(self, array: list, low: int, high: int) -> None:
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot)
            self._quicksort(array, pivot + 1, high)

    def _partition(self, array: list, low: int, high: int) -> int:
        pivot = array[low]
        i = low
        j = high

        while True:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]


    def sort(self, array: list) -> list:
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

hsrp = HoareSortRandom_ij()
st = time.time()
sor_arr = hsrp.sort(arr)
et = time.time()
print(f"Time taken for Hoare partition with random i and j {et-st}")