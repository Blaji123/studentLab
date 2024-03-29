from enum import Enum, unique
from sorting_algorithms.merge_sort import MergeSort
from sorting_algorithms.bingo_sort import BingoSort
@unique
class Algorithm(Enum):
    MERGE_SORT = MergeSort
    BINGO_SORT = BingoSort