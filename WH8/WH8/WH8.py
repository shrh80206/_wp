
# 1. ��X�̤j��
def find_max(numbers):
    A = numbers[0]
    for B in numbers:
        if B > A:
            A = B
    return A


# 2. �p�⥭����
def average(nums):
    A = sum(nums)
    B = len(nums)
    return round(A / B, 1)


# 3. �_������
def classify_even_odd(numbers):
    A = {'even': [], 'odd': []}
    for B in numbers:
        if B % 2 == 0:
            A['even'].append(B)
        else:
            A['odd'].append(B)
    return A


# 4. �Ʀr��P���ϧ�
def print_stars(n):
    for A in range(1, n + 1):
        print('*' * A)


# 5. �^�妨�Z�൥��
def grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'


# 6. �p��r���X�{����
def count_chars(s):
    A = {}
    for B in s:
        A[B] = A.get(B, 0) + 1
    return A


# 7. �r���ഫ���r��
def dict_to_string(d):
    A = [f"{B}:{C}" for B, C in d.items()]
    return ', '.join(A)


# 8. �P�_���
def is_prime(n):
    if n <= 1:
        return False
    for A in range(2, int(n**0.5) + 1):
        if n % A == 0:
            return False
    return True


# 9. ��X list ���X�{���Ƴ̦h���Ʀr
def most_common(nums):
    A = {}
    for B in nums:
        A[B] = A.get(B, 0) + 1
    return max(A, key=A.get)


# 10. �έp�ǥ��`���P����
def summary(data):
    for A in data:
        B = A['name']
        C = A['scores']
        D = sum(C)
        E = D / len(C)
        print(f"{B}: �`�� = {D}, ���� = {E:.1f}")
