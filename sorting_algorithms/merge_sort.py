from generic_sort.generic_sort import GenericSort
class MergeSort(GenericSort):
    def __init__(self,col,key,reverse):
        super().__init__(col,key,reverse)

    def sort(self):
        self.sort_rec(self.col)

    def sort_rec(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]

            self.sort_rec(sub_array1)
            self.sort_rec(sub_array2)

            i = j = k = 0

            while i < len(sub_array1) and j < len(sub_array2):
                if self._in_order(sub_array1[i],sub_array2[j]):
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k +=1

            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1

            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1