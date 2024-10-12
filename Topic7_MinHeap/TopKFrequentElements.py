# https://leetcode.com/problems/top-k-frequent-elements

"""
+ Count the frequency of every element in array

+ I am going to use tuple (key is a frequency of one value and value is element)
+ Add it into heap
    + if len of heap is smaller than kth => continue to push
    + if len of heap is larger than kth => pop first, push after


Space complexity: O(N)
Time complexity: O(N log k): N length of array, k is top k frequent elements
"""

import heapq
from typing import Counter, List

class Solution:
    def topKFrequent(self, nums: List[int], kth: int) -> List[int]:
        counter = Counter(nums)

        heap = []

        for k, v in counter.items():
            if len(heap) == kth:
                heapq.heappushpop(heap, (v, k))
            else:
                heapq.heappush(heap, (v, k))

        return [item[1] for item in heap]


"""
+ It makes sure that the frequency of all elements in array must be smaller than length of list
+ To build list from 0 to len(n)
    + Every idx shows how many element appears idx times at idx

+ To count the frequency of all elements based on tuple
    + Key: element
    + Value: its frequency

+ To iterate the list from end to the beginning 
    => Add element into result until result has kth length

Space complexity: O(len(N))
Time complexity: O(N): N length of array
"""

class Solution:
    def topKFrequent(self, nums: List[int], kth: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)

        arr = [0] * (n + 1)

        for num, freq in counter.items():
            if arr[freq] == 0:
                arr[freq] = [num]
            else:
                arr[freq].append(num)

        result = []
        for ele in arr[::-1]:
            if ele != 0:
                result.extend(ele)

            if len(result) == kth:
                break

        return result