class Solution:
    """
    Generates Lexographical ordering both iterative and recursive
    """

    def lexicalOrderIterative(self, n: int) -> list[int]:
        ans = []
        num = 1
        for _ in range(n):
            ans.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num >= n:
                    num //= 10
                    num += 1
        return ans

    def lexicalOrderDFS(self, n: int) -> list[int]:
        answer = []
        for start in range(1, 10):
            self.generate_lexical_order(start, n, answer)
        return answer

    def generate_lexical_order(
        self, current_number: int, limit: int, result: list[int]
    ):
        if current_number > limit:
            return
        result.append(current_number)
        for next_digit in range(10):
            next_number = current_number * 10 + next_digit
            if next_number <= limit:
                self.generate_lexical_order(next_number, limit, result)
            else:
                break
