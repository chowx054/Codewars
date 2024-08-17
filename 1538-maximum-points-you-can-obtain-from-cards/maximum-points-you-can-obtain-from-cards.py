class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

            if k == len(cardPoints):
                return sum(cardPoints)
            
            left, right = 0, len(cardPoints)-k
            total_score = sum(cardPoints[right:])
            score = total_score
            
            while right < len(cardPoints):
                total_score += (cardPoints[left] - cardPoints[right])
                score = max(score, total_score)
                left += 1
                right += 1
            
            return score