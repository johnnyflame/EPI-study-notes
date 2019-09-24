import random



def search_first_of_k(A,k):
    """

    11.1 Search first occurrence of K

    The difference between this and ordinary binary search is that it
    asks us to return the first instance of k. A naive binary search will find k, but
    to find the first instance of it may require a long linear scan backwards.

    Imagine an extreme case where the whole array is filled with k, then this makes the
    naive binary search O(N).

    To avoid this, in the following algorithm we discard half of the array each time.


    :param A: A sorted array of integers
    :param k: the value to find
    :return: The first occurance of k in A
    """

    left,right = 0,len(A) - 1,
    result = -1

    # invariant: A[left:right+1] is the candidate set

    while left <= right:
        mid = left + (right - left) / 2

        if A[mid] > k:
            right = mid-1
        elif A[mid] == k:
            # Ordinary binary search would return here, but instead, we mark it and
            # continue onwards.

            result = mid
            right = mid -1
        else:
            left = mid + 1
    return result


def square_root(k):
    """
    11.4: Compute the integer square root

    Takes a non negative integer and returns the largest integer whose square is less
    than or equal to the given integer.

    For example, if k=16, the output would be 4. If the input is 300, return 17, since
    17**2 = 289 < 300 and 18**2 is 324 > 300

    :param k: The target square number
    :return: the largest int who's square is less than or equal to k
    """

    left, right = 0,k

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared <=k:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1



def find_kth_largest(k,A):
    """
    11.8 Find the Kth largest element.

    Problem:

    Given an unsorted array, A, with distinct items,
    and a value k. Find the kth largest value in A.

    Insights:

    1. We could sort, then the problem is trivial. But this is wasteful, we don't need
    to go O(n log n)

    2. We could use a heap--put all values in a heap, then pop k times. Again, wasteful.

    3. The key insight here---if we randomly select an item as a "pivot", and partition
    the remaining entries around this pivot.

    If there are exactly k-1 items on the right hand side of the pivot (as in, greater
    than the pivot), then the pivot must
    be the kth largest.

    If there are more than k - 1 items greater than the pivot, we can get rid of the
    smaller half of the array, trimming the search space by half

    If there are less than k-1 items, we've overshot, we can discard the right sub array.

    (Fuck me, this is genius!)

    :param k:
    :param A:
    :return:
    """

    def partition_around_pivot(left, right, pivot_idx):
        pivot_value = A[pivot_idx]
        new_pivot_idx = left

        A[pivot_idx], A[right] = A[right],A[pivot_idx]

        # for i in range(left,right):
        #     if A[i] <


    left, right = 0, len(A) - 1

    while left <= right:
        pivot_idx = random.randint(left,right)
        # new_pivot_idx =