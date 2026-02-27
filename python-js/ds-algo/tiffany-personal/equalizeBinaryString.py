from itertools import combinations
from heapq import heappush, heappop

class Solution:
    def priority(self, state, k):
        # I can only think of being a certain number
        # of flips away from done based on this
        return state.count('0') % k

    def applyMove(self, strng, indices):
        ret = list(strng)
        for i in indices:
            ret[i] = '0' if ret[i] == '1' else '1'
        return ''.join(ret)
    
    def minOperations(self, s: str, k: int) -> int:
        if s.count('0') == 0:
            return 0
        goal = '1'*len(s)
        # frontier should also track number of moves taken
        frontier_tracker, reached, frontier = {}, {}, []
        reached[s] = True
        legalMoves = list(combinations(range(len(s)), k))

        for move in legalMoves:
            state = self.applyMove(s, move)
            if state == goal:
                return 1
            if state not in frontier_tracker:
                heappush(frontier, (self.priority(state, k), state, 1))
                frontier_tracker[state] = True
        
        while len(frontier) != 0:
            _, state, number_of_moves = heappop(frontier)
            reached[state] = True
            if state == goal:
                return number_of_moves
            for move in legalMoves:
                child_state = self.applyMove(state, move)
                if child_state not in reached and child_state not in frontier_tracker:
                    heappush(frontier, (self.priority(child_state, k), child_state, number_of_moves+1))
                    frontier_tracker[child_state] = True
        # reach here if no solution
        return -1

test = Solution()
print(test.minOperations('110', 1))
print(test.minOperations('0101', 3))
print(test.minOperations('101', 2))
print(test.minOperations('00001001', 7))
print(test.minOperations('0101000001001', 3))
print(test.minOperations('01000011010111', 8))
