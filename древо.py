def height(man):
    if man not in p_trees:
        return 0
    else:
        return 1 + height(p_trees[man])


p_trees = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_trees[child] = parent
heights = {}
for man in set(p_trees.keys()).union(set(p_trees.values())):
    heights[man] = height(man)
for key, value in sorted(heights.items()):
    print(key, value)
