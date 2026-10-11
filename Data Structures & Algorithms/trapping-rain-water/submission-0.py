class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]

        left_max[0] = height[0]
        for i in range(1,len(height)):
             left_max[i] = max(left_max[i-1],height[i])

        right_max[-1] = height[-1]

        for i in range(len(height)-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])

        response = 0
        for i in range(1,len(height)-1):
            response += max(min(left_max[i-1],right_max[i+1]) - height[i] , 0)

        return response