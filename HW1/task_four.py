import random


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """Сложность O(n*log(n)).
    
        Args:
            arr (list): an array of distinct integers.
        Returns:
            list: a list of pairs in ascending order(with respect to pairs).
        """
        min_d = max(arr) - min(arr)
        min_list = []
        swap = True
        for i in range(len(arr)-1):
            if (arr[i] - arr[i-1]) < min_d:
                min_d = arr[i] - arr[i-1]
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == min_d:
                min_list.append([arr[i-1], arr[i]]) 
        return min_list

def quicksort(nums): #метод быстрой сортировки Хоара
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)
