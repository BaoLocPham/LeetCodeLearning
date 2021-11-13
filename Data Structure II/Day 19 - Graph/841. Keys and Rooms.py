class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Approach 1: dfs
        # Time O(n)
        # Space O(n)
        seen = [0]*len(rooms)
        seen[0] = 1
        stack = [0]
        while stack:
            node = stack.pop()
            for key in rooms[node]:
                if not seen[key]:
                    seen[key]=1
                    stack.append(key)
        return all(seen)