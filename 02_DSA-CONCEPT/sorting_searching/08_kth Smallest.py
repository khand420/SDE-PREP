import heapq

# def findKthLargest(nums, k):
#         p = []

#         # for x in nums:
#         #     heapq.heappush(p, x)
#         #     if len(p) > k:
#         #         heapq.heappop(p) #pop and return the smallest item from the heap.
#         # return p[0]

#         # print(heapq.nsmallest(k, nums))
#         return heapq.nlargest(k,nums)[-1]
#         # print

# # nums = [3,2,1,5,6,4]
# # k = 2
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# # Output: 4
# print(findKthLargest(nums, k))


def kthSmallest(arr,  K):

    # Sort the given array
    # arr.sort()
    # # Return k'th element in the
    # # sorted array
    # return arr[K-1]

    # p  = []
    # for x in arr:
    #     heapq.heappush(p, x)
    #     if len(p) < K:
    #         heapq.heappop(p) #pop and return the smallest item from the heap.
    # return p[0]

    # print(heapq.nsmallest(k, nums))
    return heapq.nsmallest(K,arr)[0]
    # print


# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 4

    # Function call
    print("K'th smallest element is",kthSmallest(arr,  K))