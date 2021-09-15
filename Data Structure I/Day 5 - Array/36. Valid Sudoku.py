class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # This problem is straightforward
        # Because limit only 9x9 board sudoku
        # O(n^2) double loop
        # O(n) size of hash set

        # Approach 1: using only one hashSet()
        hashSet = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val!='.':
                    r = f"{val} found in row {i}"
                    c = f"{val} found in col {j}"
                    sub = f"{val} found in sub mat {i//3}-{j//3}"
                    if (r in hashSet or c in hashSet or sub in hashSet):
                        return False
                    hashSet.add(r)
                    hashSet.add(c)
                    hashSet.add(sub)

        # Approach 2: using 9^3 hashSet
        # Faster than approach 2
        rSet = [set() for _ in range(9)]
        cSet = [set() for _ in range(9)]
        bSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in rSet[i] or val in cSet[j] or val in bSet[((i // 3) * 3 + j // 3)]:
                        return False
                    rSet[i].add(val)
                    cSet[j].add(val)
                    bSet[(i // 3) * 3 + j // 3].add(val)
        return True