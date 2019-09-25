import collections


class Stack:
    """

    8.1

    One way to implement a stack with max function

    """

    # namedtuple is a bit like a class item
    ElementWithCachedMax = collections.namedtuple("ElementWithCachedMax",('element','max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self,x):
        # What is happening here? How is max being kept here?
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x,self.max()))
        )

class StackOptimized:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self._element = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._element) == 0

    def max(self):
        if self.empty():
            raise IndexError ("max(): empty stack")
        return self._cached_max_with_count[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max

        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()

        return pop_element

    def push(self,x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x,1))
        else:
            current_max = self._cached_max_with_count[-1].max

            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x,1))




"""
8.6 
Compute binary tree nodes in order of increased depth

"""

def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        # interesting syntax here
        curr_depth_nodes = [
            child for curr in curr_depth_nodes for child in (curr.left,curr.right)
            if child
        ]
    return result