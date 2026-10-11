class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        response = 0
        for num in nums:
            if num - 1 not in nums:
                curr = 1
                curr_num = num
                while curr_num+1 in nums:
                    curr+=1
                    curr_num+=1
                response = max(curr, response)
        return response
