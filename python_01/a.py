
# class Solution:
#     def fibonacci(self, n):
#         a = 0
#         b = 1
#         for i in range(n - 1):
#             a, b = b, a + b
#         return a
# if __name__ == "__main__":
#     so = Solution()
#     print(so.fibonacci(100))

class Solution:
    def fibonacci(self, n):
        a,b = 0,1
        num = 1
        while num < n:
            a,b = b,a+b
            num += 1
        return a

if __name__ == "__main__":
    so = Solution()
    print(so.fibonacci(100))