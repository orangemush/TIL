# LIS(Longest Increasing Subsequence) algorithm
# 주어진 배열을 기준으로 가장 긴 증가 부분수열을 구하는 알고리즘

def lis(seq) -> int:
    """
    seq: 랜덤으로 주어지는 수열 ex) [1, 5, 2, 4, 3, 10, 8, 21]
    여기에서 lis는 1, 2, 4, 10, 21
    주어진 배열을 기준으로 가장 긴 증가 부분수열을 구하는 알고리즘
    """
    result = list()

    # 1. 최대 길이는 주어지는 seq의 길이
    # 2. 전의 숫자보다 커야 된다.
    temp = 0
    for outer_idx in range(len(seq)):
        num = seq[outer_idx]
        for compare_idx in range(outer_idx + 1, len(seq)):
            if num >= seq[compare_idx]:
                continue






    return result
