from typing import List

MOD = 10**9 + 7


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        if n == 1:
            return m % MOD

        def matmul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            size = len(A)
            C = [[0] * size for _ in range(size)]

            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue

                    aik = A[i][k]
                    for j in range(size):
                        C[i][j] = (C[i][j] + aik * B[k][j]) % MOD

            return C

        def matpow(M: List[List[int]], exp: int) -> List[List[int]]:
            size = len(M)

            result = [
                [1 if i == j else 0 for j in range(size)]
                for i in range(size)
            ]

            while exp:
                if exp & 1:
                    result = matmul(result, M)

                M = matmul(M, M)
                exp >>= 1

            return result

        L = [
            [1 if y < x else 0 for y in range(m)]
            for x in range(m)
        ]

        U = [
            [1 if y > x else 0 for y in range(m)]
            for x in range(m)
        ]

        steps = n - 1
        block = matmul(U, L)
        P = matpow(block, steps // 2)

        if steps % 2 == 1:
            P = matmul(L, P)

        one_pattern = sum(sum(row) for row in P) % MOD
        return (2 * one_pattern) % MOD