class Node:
    def __init__(self, point, axis):
        self.point = point
        self.left = None
        self.right = None
        self.axis = axis

def build_kdtree(points, axis):
    if not points:
        return None
    
    points.sort(key = lambda x: x[axis])

    median = len(points) // 2

    node = Node(points[median], axis)

    node.left = build_kdtree(points[:median], (axis + 1) % len(points[0]))

    node.right = build_kdtree(points[median+1:], (axis + 1) % len(points[0]))

    return node

def print_tree(node, level=0, side=None):
    if node is not None:
        prefix = ""
        if side is not None:
            prefix = side + "---- "
        print(" " * level + prefix + str(node.point))
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")

points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]

root = build_kdtree(points, 0)
print_tree(root)