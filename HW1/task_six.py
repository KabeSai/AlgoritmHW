class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(num, count=0): #функция для вычисления шагов нужных чтобы из числа получить 1
            if num == 1:
                return count
            if num % 2 == 0:
                return power(num / 2, count+1)
            return power(num * 3 + 1, count+1)
        power_l = []#список из кортежей в (x,y) где х шаги а y число 
        for i in range(lo, hi+1):
            power_l.append((power(i),i))
        return sorted(power_l)[k-1][1]# функция sorted сортирует кортежи по первому значению, если значения равны по следующему и тд
