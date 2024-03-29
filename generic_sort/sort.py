from sorting_algorithms.algorithms import Algorithm

class Sorting:
    @staticmethod
    def sort(col, key=None, reverse=False, algorithm=Algorithm.MERGE_SORT):
        sorting_algorithm = algorithm.value(col,key,reverse)
        sorting_algorithm.sort()