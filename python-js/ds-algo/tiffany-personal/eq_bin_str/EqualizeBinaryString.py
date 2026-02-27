import unittest
from time import time as timer
from heapq import heappush, heappop

# running: python -m unittest EqualizeBinaryString.TestClass
class Solution:
    # moves format: (<flip 0s to 1s>, <flip 1s to 0s>)
    def findLegalMoves(self, state, k):
        # first find the number of 1s and 0s
        zeros, ones, moves = 0, 0, []
        if type(state) == str:
            zeros = state.count('0')
            ones = len(state) - zeros
        else:
            zeros, ones = state
        # second, choose up to k zeros to flip
        min_zeros = 0 if k - ones < 0 else k - ones
        max_zeros = min(zeros, k) + 1
        return min_zeros, max_zeros

    def evaluateGoal(self, moves, zeros_left, k):
        if (zeros_left == 0):
            return moves
        else:
            if (zeros_left % k) == 0:
                return moves + (zeros_left // k)
        return -1
    
    def priority(self, moves, zeros_left, k):
        # heavily favor states that are within range of solving
        return 5*(zeros_left % k) + (zeros_left // k) + moves
    
    def validState(self, state):
        if state[0] >= 0 and state[1] >= 0:
            return True
        return False

    # move format: (<flip 0s to 1s>, <flip 1s to 0s>)
    # state format: (0s count, 1s count)
    def applyMove(self, state, move):
        ret = (state[0] - move[0] + move[1], state[1] - move[1] + move[0])
        return ret
    
    def minOperations(self, s: str, k: int) -> int:
        zeros_left = s.count('0')
        total = len(s)
        if (try_goal := self.evaluateGoal(0, zeros_left, k)) != -1:
            return try_goal
        # dictionaries for checking inclusion quickly, then frontier is a PQ
        # need to revamp trackers to check by number of zeros in a state
        frontier_tracker, reached, frontier = {}, {}, []
        reached[zeros_left] = 0
        # another optimization: change legalMoves to return only moves that make unique states
        # these moves should flip a different number of zeros at least
        min_zeros, max_zeros = self.findLegalMoves(s, k)
        start = (zeros_left, total - zeros_left)

        for i in range(min_zeros, max_zeros):
            state = self.applyMove(start, (i, k-i))
            if self.validState(state):
                zeros_left = state[0]
                if zeros_left not in frontier_tracker:
                    frontier.append(((zeros_left, total - zeros_left), 1))
                    frontier_tracker[zeros_left] = 1
        
        for state, number_of_moves in frontier:
            zeros_left = state[0]
            reached[zeros_left] = number_of_moves
            min_zeros, max_zeros = self.findLegalMoves(state, k)
            for i in range(min_zeros, max_zeros):
                child_state = self.applyMove(state, (i, k-i))
                if self.validState(child_state):
                    child_zeros_left = child_state[0]
                    if (try_goal:= self.evaluateGoal(number_of_moves + 1, child_zeros_left, k)) != -1:
                        return try_goal
                    if child_zeros_left not in reached:
                        if child_zeros_left not in frontier_tracker:
                            frontier.append((child_state, number_of_moves + 1))
                            frontier_tracker[child_zeros_left] = number_of_moves + 1
                        else:
                            # keep frontier clean by only adding states with a different
                            # number of zeros left (no duplicate states)
                            if frontier_tracker[child_zeros_left] > (number_of_moves + 1):
                                frontier_tracker[child_zeros_left] = number_of_moves + 1
                                frontier = [node for node in frontier if node[-1] != child_zeros_left]
                                frontier.append((child_state, number_of_moves + 1))
                    
        # reach here if no solution
        return -1

    def testing(test_set):
        tester = Solution()
        for problem in test_set:
            s, k, sol = problem
            print(f"Problem {s}: Length of problem: {len(s)}")
            start = timer()
            test_soln = tester.minOperations(s, k)
            end = timer()
            print(f"Time: {end - start}")
            assert test_soln == sol, f"failed {problem}, got {test_soln} and expected {sol}"

soln = Solution()
print(soln.minOperations('00001001', 7)) #6
