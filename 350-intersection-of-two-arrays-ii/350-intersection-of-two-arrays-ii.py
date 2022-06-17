class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return [num for num in nums1 if num in nums2] 
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        result = nums1 & nums2
        return list(result.elements())