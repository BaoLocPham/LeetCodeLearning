class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.og = list(nums)

    def reset(self) -> List[int]:
        self.array = self.og.copy()
        return self.array

    def shuffle(self) -> List[int]:
        # Approach 1: Brute Force
        # Time O(n^2) -> list.pop()
        # Space O(n)
        # aux = self.array.copy()
        # for indx in range(len(self.array)):
        #     remove_indx = random.randrange(len(aux))
        #     self.array[indx] = aux.pop(remove_indx)
        # return self.array
        # Fisher-Yates Algorithm
        # Time O(n)
        # Space O(1)
        for i in range(len(self.array)):
            swap_indx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_indx] = self.array[swap_indx], self.array[i]
        return self.array
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()