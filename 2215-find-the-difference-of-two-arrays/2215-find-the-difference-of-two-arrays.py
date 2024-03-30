class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        common = list(set(nums1).intersection(set(nums2)))
        left = [x for x in set(nums1) if x not in common]
        right = [x for x in set(nums2) if x not in common]
        
        return [left, right]