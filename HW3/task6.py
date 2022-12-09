class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:#Проверка на пустоту
            return 0
        def get_diametr(root):#Рекурсивная функция проверяющая все узлы и возвращающая максимальной из левого узла и правого
            if not root:
                return 0,0
            else:
                l,lr = get_diametr(root.left)
                r,rl = get_diametr(root.right)
                return max(l,r), max(l+r,lr,rl)
        a, b = get_diametr(root)
        return max(a, b)#Возвращаем самый длинный диаметр