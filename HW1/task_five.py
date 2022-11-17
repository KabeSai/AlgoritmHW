import random
class Solution:
    def findKthLargest(self, nums, k):
        if len(nums) <= 1:
            return nums[0]
        else:
            q = random.choice(nums)
        #разбиваем на части меньше, больше или равны рандомному числу
        l_nums = [n for n in nums if n > q]
        e_nums = [n for n in nums if n == q]
        b_nums = [n for n in nums if n < q]
        l, b = len(l_nums), len(e_nums)
        #Если длина списка из меньших значений меньше или равна K то мы ищем в этом списке меньшее
        #Если сумма длин списков средних и больших значений больше K то ищем в большем списке
        #Если не выполняется не одно из этих условий ищем в среднем списке
        #где находятся одинаковые значения, значит сразу возвращем люое значение из этого списка
        if k <= l:
            return self.findKthLargest(l_nums, k)
        elif k > l + b:
            return self.findKthLargest(b_nums, k - l - b)
        else:
            return e_nums[0]
