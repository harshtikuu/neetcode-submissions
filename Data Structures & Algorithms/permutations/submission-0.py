class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        response = []

        def dfs(i, curr):
            curr.append(nums[i])
            if len(curr) == len(nums):
                response.append(curr[:])
                curr.pop()
                return
            
            for k in range(len(nums)):
                if nums[k] not in curr:
                    dfs(k, curr)
            curr.pop()

        for i in range(len(nums)):
            dfs(i, [])

        return response