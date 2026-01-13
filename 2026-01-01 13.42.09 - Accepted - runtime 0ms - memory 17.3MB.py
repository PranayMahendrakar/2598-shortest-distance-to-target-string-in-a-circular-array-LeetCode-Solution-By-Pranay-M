class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if target not in words:
            return -1
        
        min_dist = float('inf')
        for i in range(n):
            if words[i] == target:
                forward = (i - startIndex) % n
                backward = (startIndex - i) % n
                min_dist = min(min_dist, forward, backward)
        
        return min_dist
    
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        return self.closetTarget(words, target, startIndex)