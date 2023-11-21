'''
2461. Maximum Sum of Distinct Subarrays With Length K

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        seen  = set()
        left = ans = cur = 0
        for right in range(n):
            cur += nums[right]
            while nums[right] in seen or right+1-left > k:
                seen.remove(nums[left])
                cur -= nums[left]
                left +=1
            seen.add(nums[right])
            if right+1-left == k:
                ans = max(ans, cur)
        return ans or 0