class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lo, hi = min(strs), max(strs)
        i = 0
        while i < len(lo) and lo[i] == hi[i]:
            i += 1
        return lo[:i]
        