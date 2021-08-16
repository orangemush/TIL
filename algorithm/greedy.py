# 21/06/24 ~ 21/06/26
# 코딩테스트 연습 -> 탐욕법(Greedy) -> 체육복
def solution(n, lost, reserve):
    """
    :n      : 전체 학생 수
    :lost   : 체육복을 잃어버린 학생 번호들을 담은 리스트
    :reserve: 체육복을 2벌 가지고 있는 학생 번호들을 담은 리스트
    :return : 체육복 하나 이상을 가진 학생의 수
    """
    # 여벌의 체육복을 가진 학생들 중, 도난 당한 학생들을 저장
    reserve_lost = reserve[::]

    # 여벌의 체육복을 가진 학생들 중, 도난 당한 학생들 제외
    for r in reserve_lost:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    answer = n - len(lost)

    # 잃어버린 학생 번호 앞 뒤에,
    # 체육복 2개 가지고 있는 학생 번호 존재하면,
    # answer += 1
    for l in lost:
        if (l + 1) in reserve:
            reserve.remove(l + 1)
            answer += 1

        elif (l - 1) in reserve:
            reserve.remove(l - 1)
            answer += 1

    return answer

"""
Greedy algorithm(탐욕 알고리즘)
    최적해를 구하는 데에 사용되는 알고리즘
    최적의 해에 가까운 값(근사치)을 구하는 방법 중 하나
    여러 경우 중 하나를 결정해야 할 때마다, 그 부분의 최적의 값을
    구하여, 전체의 최적의 값이길 바라는 알고리즘
"""

# 21/06/26 ~ 21/06/30
# 코딩테스트 연습 -> 탐욕법(Greedy) -> 조이스틱
def solution(name):
    answer = 0

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    # 좌우 스틱을 최대로 움직일 수 있는 횟수
    n = len(name)
    move = n - 1

    for idx in range(n):
        next_idx = idx + 1

        # 다음 문자가 A이면, A가 아닐 때까지 계속해서 확인한다.
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer



# 21/07/01 ~
# 코딩테스트 연습 -> 탐욕법(Greedy) -> 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883/
def solution(number: str, k: int):
    """
    number: 1자리 이상, 1,000,000자리 이하의 숫자.
    k     : 1 <= k < number의 자릿수, 자연수입니다.
    중요한 건, 리스트의 순서를 정렬하지 않은 상황에서의
    가장 큰 수를 만드는 것입니다.

    1. 맨 앞에서 k개 까지 탐색하여 가장 큰 수 앞자리까지 자른다.
    2. 남은 k개를 큰 수 뒷자리중 최솟값들을 전부 다 자른다.
    """
    """
    """

    front_numbers = number[:k]
    front_num_idx = number.find(str(max(map(int, front_numbers))))
    back_numbers = number[front_num_idx:]
    k -= front_num_idx

    # back_numbers: 77252841
    copy_list = back_numbers[:]
    for i in range(len(back_numbers) - 1):
        cur_num = int(back_numbers[i])
        next_num = int(back_numbers[i + 1])
        if cur_num < next_num:
            copy_list = copy_list.replace(str(cur_num), '')
            k -= 1
        if k == 0:
            break

    answer = copy_list

    return answer

a = "123"
a.replace("1", '')
print(a)

print(5%  10)

# -- 1. 8학년 보다 낮은 학생들의 이름을 원하지 않는다.(Ketty)
# -- 2. descending order by grade
# -- 3. grade가 같은 학생이 있다면 이름을 철자순으로 정렬하라.
# -- 4. 8학년보다 낮은 학생들의 이름은 전부 NULL로 처리하라(order by grades)
# -- 5. 8학년보다 낮은 학생들 중 같은 학년인 학생들을 정렬할 땐, marks를 ascending으로 정렬해라.