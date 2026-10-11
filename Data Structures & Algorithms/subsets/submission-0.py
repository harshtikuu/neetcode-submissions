class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = [[]]
        for i in range(len(nums)):
            self.dfs(i, nums,  response,  [])
        return response
    
    def dfs(self, i, nums, response, curr):
        curr.append(nums[i])
        response.append(curr[:])
        for k in range(i+1, len(nums)):
            self.dfs(k, nums, response, curr)
        curr.pop()
