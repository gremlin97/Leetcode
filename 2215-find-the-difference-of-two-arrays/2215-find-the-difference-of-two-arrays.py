class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        common = list(set(nums1).intersection(nums2))
        arr1 = list(set([x for x in nums1 if x not in common]))
        arr2 = list(set([x for x in nums2 if x not in common]))
        return [arr1, arr2]
        