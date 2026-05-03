class Solution:
    def rotateString(self, s, goal) -> str:
        if len(s) != len(goal):
            return False

        doubleS = s + s
        return self.kmp_search(doubleS, goal)

    def kmp_search(self, text, pattern):
        lps = self.compute_lps(pattern)
        j = 0
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]

            if text[i] == pattern[j]:
                j += 1

            if j == len(pattern):
                return i - j + 1

    def compute_lps(self, pattern) -> list[int]:
        lps = [0] * len(pattern)
        j = 0  # length of longest prefix which is also a suffix

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        return lps


s = Solution()
print(s.rotateString("abcde", "cdeab"))
