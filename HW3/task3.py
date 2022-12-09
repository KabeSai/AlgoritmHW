from typing import List


class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        "Сложность данной функции log(n)"
        if root is not None:# Если корень не пустой
            output = []
            depth = 0
            def travel(node, depth):
                depth += 1
                if len(output) < depth:#Если глубина больше очереди
                	output.append([])
                output[depth - 1].append(node.val)
                if node.left is not None:#Если есть узел слева запускаем путешествиника по дереву
                	travel(node.left, depth)
                if node.right is not None:#Прошлое для правого узла
                	travel(node.right, depth)
            travel(root, depth)#Запускаем по дереву путешествиника
            return [sum(x)/len(x) for x in output]
        else:
            return []