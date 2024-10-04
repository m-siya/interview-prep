# ### K CLOSEST POINTS TO ORIGIN

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# https://leetcode.com/problems/k-closest-points-to-origin/description/

# TC - O(nlogn), SC - O(n)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # find distance from origin of every point ? and take top k points?

        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
    
# TC - O(nlogn), SC - (O(k))

from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # find distance from origin of every point ? and take top k points?

        #return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]

        heap = []
        for x, y in points:            
            heappush(heap, (-(x**2 + y**2), [x, y]))

            if len(heap) > k:
                heappop(heap)
        
        ans = [point for dist, point in heap]
        return ans

# TC - O(n) (best and average case); O(n^2) (worst case), SC - O(n^2) [due to recursion]
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # find distance from origin of every point ? and take top k points?

        #return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]

        # quickselect

        coords = [(x**2 + y**2, [x, y]) for x, y in points]

        def quickselect(coords, k):
            pivot = random.choice(coords)[0]
            left, mid, right = [], [], []

            for dist, point in coords:
                if dist < pivot:
                    left.append((dist, point))
                elif dist == pivot:
                    mid.append((dist, point))
                else:
                    right.append((dist, point))
            
            if k <= len(left):
                return quickselect(left, k)
            elif len(left) + len(mid) < k:
                return left + mid + quickselect(right, k - len(left) - len(mid))
            else:
                return left + mid
        
        ans = [point for dist, point in quickselect(coords, k)]
        return ans