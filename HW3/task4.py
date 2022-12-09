class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        "Сложность функции O(n)"
        ans = 0
        while head:
            ans = ans*2 + head.val#Значение узла умножаем на два когда увеличивается разряд 
            #и добавляем к прошлому значению
            head = head.next
        return ans

#Я к подобным задачам на егэ готовился :-)