import itertools, heapq,math

"""
Boot camp question:

Finding the k longest strings out of streaming data


The idea is to use a min-heap. Thought I'm struggling to understand why not use maxheap instead.
It certainly feels more intuitive to bash the whole thing into a heap, then pick k 
elements away from the heap.

"""

def top_k(k,stream):
    min_heap = [(len(s),s) for s in itertools.islice(stream,k)]
    heapq.heapify(min_heap)

    for next_string in stream:
        #push next string and pop the shortest string in min_heap
        heapq.heappushpop(min_heap,(len(next_string),next_string))

    return [p[1] for p in heapq.nsmallest(k,min_heap)]


"""
10.1

Merge k sorted Arrays
"""

def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    # Builds a list of iterators for each array in sorted_array
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterator in min_heap
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it,None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element,i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter,None)
        if next_element is not None:
            heapq.heappush(min_heap,(next_element, smallest_array_i))

    return result


def test_code():

    data = [
        [3,5,7],
        [0,6],
        [0,6,2,8]
    ]

    merge_sorted_arrays(data)





"""
10.4
"""

class Star:
    def __init__(self,x,y,z):
        self.x, self.y, self.z = x,y,z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance


def find_closest_k_stars(stars,k):
    max_heap = []

    for star in stars:
        heapq.heappush(max_heap, (-star.distance,star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    return [s[1] for s in heapq.nlargest(k,max_heap)]





test_code()