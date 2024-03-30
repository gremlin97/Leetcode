class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        common = nums1.intersection(nums2)
        left = [x for x in nums1 if x not in common]
        right = [x for x in nums2 if x not in common]
        
        return [left, right]