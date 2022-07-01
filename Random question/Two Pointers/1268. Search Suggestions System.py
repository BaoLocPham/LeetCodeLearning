class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Approach 2 pointers
        # Time O(nlogn) sort + O(mlogn) run binary search on products m times
        # Space O(n)
        products.sort()
        rs = []
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            tmp = []
            remain = r - l + 1
            for j in range(min(3, remain)):
                tmp.append(products[l + j])
            rs.append(tmp)
        return rs
            
            