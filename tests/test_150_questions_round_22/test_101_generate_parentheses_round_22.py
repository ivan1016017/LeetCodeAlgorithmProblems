import pytest
from src.my_project.interviews.top_150_questions_round_22.ex_101_generate_parentheses import Solution


class TestGenerateParentheses:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with n = 3"""
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result = self.solution.generateParenthesis(n)
        assert sorted(result) == sorted(expected)
    
    def test_example_2(self):
        """Test with n = 1"""
        n = 1
        expected = ["()"]
        result = self.solution.generateParenthesis(n)
        assert result == expected
    
    def test_n_equals_2(self):
        """Test with n = 2"""
        n = 2
        expected = ["(())", "()()"]
        result = self.solution.generateParenthesis(n)
        assert sorted(result) == sorted(expected)
    
    def test_n_equals_4(self):
        """Test with n = 4 - verify all are well-formed"""
        n = 4
        result = self.solution.generateParenthesis(n)
        
        # Verify all results have correct length
        assert all(len(s) == 2 * n for s in result)
        
        # Verify all are well-formed
        for s in result:
            balance = 0
            for char in s:
                if char == '(':
                    balance += 1
                else:
                    balance -= 1
                # Balance should never go negative
                assert balance >= 0
            # Final balance should be 0
            assert balance == 0
        
        # For n=4, there should be 14 combinations (Catalan number C_4)
        assert len(result) == 14
    
    def test_all_results_are_unique(self):
        """Verify no duplicates in results"""
        n = 3
        result = self.solution.generateParenthesis(n)
        assert len(result) == len(set(result))
    
    def test_all_results_are_valid(self):
        """Verify all results are well-formed parentheses"""
        n = 3
        result = self.solution.generateParenthesis(n)
        
        for s in result:
            balance = 0
            for char in s:
                if char == '(':
                    balance += 1
                else:
                    balance -= 1
                # At any point, closing should not exceed opening
                assert balance >= 0
            # At the end, all parentheses should be matched
            assert balance == 0
