import unittest
from time import time as timer
from itertools import combinations
from heapq import heappush, heappop

# need a better criteria for no solution than a timeout
# running: python -m unittest EqualizeBinaryString.TestClass
# need to remove redundant states
class Solution:
    def findLegalMoves(self, state, k):
        # can flip up to k zeros
        # first find all the zero indices
        zero_indices, one_indices, moves = [], [], []
        for i in range(len(state)):
            if state[i] == '0':
                zero_indices.append(i)
            else:
                one_indices.append(i)
        # second, choose up to k zeros to flip
        for i in range(len(zero_indices)):
            new_move = zero_indices[:i] + one_indices[:(k-i)]
            if len(new_move) == k:
                moves.append(new_move)
        return moves
    
    def priority(self, moves, zeros_left, k):
        # heavily favor states that are within range of solving
        return 5*(zeros_left % k) + (zeros_left // k) + moves

    def evaluateGoal(self, state, moves, zeros_left, k, goal):
        if (state == goal):
            return moves
        else:
            if (zeros_left % k) == 0:
                return moves + (zeros_left // k)
        return -1

    def applyMove(self, strng, indices):
        ret = list(strng)
        for i in indices:
            ret[i] = '0' if ret[i] == '1' else '1'
        return ''.join(ret)
    
    def minOperations(self, s: str, k: int) -> int:
        goal = '1'*len(s)
        zeros_left = s.count('0')
        if (try_goal := self.evaluateGoal(s, 0, s.count('0'), k, goal)) != -1:
            return try_goal
        # dictionaries for checking inclusion quickly, then frontier is a PQ
        # need to revamp trackers to check by number of zeros in a state
        frontier_tracker, reached, frontier = {}, {}, []
        reached[zeros_left] = 0
        # another optimization: change legalMoves to return only moves that make unique states
        # these moves should flip a different number of zeros at least
        legalMoves = self.findLegalMoves(s, k)

        for move in legalMoves:
            state = self.applyMove(s, move)
            zeros_left = state.count('0')
            if zeros_left not in frontier_tracker:
                heappush(frontier, (self.priority(1, zeros_left, k), state, 1, zeros_left))
                frontier_tracker[zeros_left] = 1
        
        while len(frontier) > 0:
            _, state, number_of_moves, zeros_left = heappop(frontier)
            if (try_goal:= self.evaluateGoal(state, number_of_moves, zeros_left, k, goal)) != -1:
                return try_goal
            reached[zeros_left] = number_of_moves
            legalMoves = self.findLegalMoves(state, k)
            for move in legalMoves:
                child_state = self.applyMove(state, move)
                child_zeros_left = child_state.count('0')
                if child_zeros_left not in reached:
                    if child_zeros_left not in frontier_tracker:
                        heappush(frontier, (self.priority(number_of_moves + 1, child_zeros_left, k), child_state, number_of_moves + 1, child_zeros_left))
                        frontier_tracker[child_zeros_left] = number_of_moves + 1
                    else:
                        # keep frontier clean by only adding states with a different
                        # number of zeros left (no duplicate states)
                        if frontier_tracker[child_zeros_left] > (number_of_moves + 1):
                            frontier_tracker[child_zeros_left] = number_of_moves + 1
                            frontier = [node for node in frontier if node[-1] != child_zeros_left]
                            heappush(frontier, (self.priority(number_of_moves + 1, child_zeros_left, k), child_state, number_of_moves + 1, child_zeros_left))
                    
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
print(soln.minOperations('01000011010111', 8))

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.startTime = timer()
        self.agent = Solution()
        
    def tearDown(self):
        self.endTime = timer()
        t = self.endTime - self.startTime
        print('%s: %.5f' % (self.id(), t))
        
    #('110', 1, 1),
    def test_01(self):
        s = '110'
        k = 1
        answer = 1
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
    
    # ('0101', 3, 2)
    def test_02(self):
        s = '0101'
        k = 3
        answer = 2
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
    
    # ('101', 2, -1),
    def test_03_no_soln(self):
        s = '101'
        k = 2
        answer = -1
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
        
    # ('00001001', 7, 6),
    def test_04(self):
        s = '00001001'
        k = 7
        answer = 6
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
    
    # ('0101000001001', 3, 3),
    def test_05(self):
        s = '0101000001001'
        k = 3
        answer = 3
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
        
    # ('01000011010111', 8, -1),
    def test_06_no_soln(self):
        s = '01000011010111'
        k = 8
        answer = -1
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)

    # ('000100000', 7, 4),
    def test_07(self):
        s = '000100000'
        k = 7
        answer = 4
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
        
    # ('0010110001100', 6, 2),
    def test_08(self):
        s = '0010110001100'
        k = 6
        answer = 2
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)

    # ('0110010001', 4, 2),
    def test_09(self):
        s = '0110010001'
        k = 4
        answer = 2
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
    
    # ('0101111110', 7, 3)
    def test_10(self):
        s = '0101111110'
        k = 7
        answer = 3
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)
    
    def test_11(self):
        s = '000101101011110'
        k = 13
        answer = 5
        test_soln = self.agent.minOperations(s, k)
        self.assertEqual(test_soln, answer)

    if __name__ == '__main__':
        unittest.main()
