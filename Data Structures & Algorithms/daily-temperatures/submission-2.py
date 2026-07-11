class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        temps = temperatures
        stk = []
        
        for i, t in enumerate(temps):
            print(stk)
            while stk and stk[-1][1] < t:
                stk_i, stk_t = stk.pop()
                ans[stk_i] = i - stk_i
            stk.append((i,t))
        return ans