class Solution:
    def totalMoney(self, n: int) -> int:
        fw = n // 7
        d = n % 7

        return (7 * fw * (fw + 7) + (2 * fw + d + 1) * d) // 2


class Solution1:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        return sum(28 + 7 * i for i in range(w)) + sum(w + i + 1 for i in range(n % 7))


class Solution2:
    def totalMoney(self, n: int) -> int:
        ans = 0
        w = n // 7
        for i in range(w):
            ans += 28 + 7 * i
        for i in range(n % 7):
            ans += w + i + 1
        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.totalMoney(n=4) == 10
    print('OK')

    print('Test 2... ', end='')
    assert sol.totalMoney(n=10) == 37
    print('OK')

    print('Test 3... ', end='')
    assert sol.totalMoney(n=20) == 96
    print('OK')


if __name__ == '__main__':
    test()
