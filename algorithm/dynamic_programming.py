# recursive case + base case(재귀법)
# 1(0) + 1(1) + 2(2) + 3(3) + 5(4) + 8(5) + 13(6) ...
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(7))

# memoization
# 작은 문제의 해를 이용해서 주어진 문제의 해를 구한다.
# 재귀 호출되는 과정에서 동일한 문제가 중복 발생할 경우 처음에 계산된 결과를 저장한 후,
# 후, 재호출 시 이전에 계산된 결과를 바로 return 한다.
# 모든 경우를 확인할 경우 exponential time algorithm
# 중간 계산 결과를 재활용 할 경우, polynomial time으로 개선된다.


# dynamic programming(동적 프로그래밍)
# 최적해를 구할 때 사용. 수학적으로는 순환성을 표현해야 하기 때문에, 점화식으로 표현함
# 여러 개의 소문제로 분할하여 각 소문제의 해결안을 바탕으로 주어진 문제를 해결
def dp_fib(n):
    fib = [0 for i in range(n)]
    fib[0], fib[1] = 0, 1

    # [0, 1, 0, 0, 0, 0]
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2] # memoization
    return fib

print(dp_fib(5))
print(dp_fib(8))

"""
dynamic programming vs greedy algorithm
공통점)
    Optimal substructure를 사용한다.
차이점)
    동적 프로그래밍은 매 step에서 여러 개의 sub-problem을 해결한다. (최적의 해를 찾아낸다.)
    탐욕 알고리즘은 매 step에서 한 개의 sub-problem만 처리한다. (그 순간의 최선의 값만 찾아낸다.)
"""