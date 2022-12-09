class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        "Сложность данной функции log(n)"
        if not root:#Если зкорень пуст
            return []
        if not root.left and not root.right: #Если глубина 0
            return [str(root.val)]
        #Проверяем сначало глубину 
        left_path = self.binaryTreePaths(root.left) 
        right_path = self.binaryTreePaths(root.right)
        #добавляем результат
        left = [] 
        for l in left_path:
            left.append(str(root.val)+ ("->"+l))
        right = [] 
        for r in right_path:
            right.append(str(root.val)+ ("->"+r))
        return left+right