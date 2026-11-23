class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def check(node, minimum, maximum):
            if node is None:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            return (check(node.left, minimum, node.val) and
                    check(node.right, node.val, maximum))

        return check(root, float('-inf'), float('inf'))
        