import numpy as np

#1. numpy 배열 생성
py_list = [1, 2, 3, 4, 5]
print(f'py_list {py_list}')

np_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f'np_arr {np_arr}')
print(f'np_arr type {type(np_arr)}')

# n차원 numpy배열 생성
# 2차원
np_arr = np.array(
    [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
    ])
print(f'np_arr \n{np_arr}')
print(f'np_arr type {type(np_arr)}')
print(np_arr[1][3]) #9

for idx, arr in enumerate(np_arr):
    print(f'idx{idx}')
    for num in arr:
        print(f'num {num}')

# 3차원
np_arr = np.array(
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0]
        ],
        [
            [10, 20, 30, 40, 50],
            [60, 70, 80, 90, 100]
        ],
        [
            [100, 200, 300, 400, 500],
            [600, 700, 800, 900, 1000]
        ]
    ]
)

for arr1th in np_arr:
    for arr2nd in arr1th:
        for arr3rd in arr2nd:
            print(f'arr3rd: {arr3rd}')

# numpy 복사
np_arr = np.array([1, 2, 3, 4, 5])
print(f'np_arr{np_arr}')

np_arr_copy = np_arr.copy()    #깊은복사
print(np_arr is np_arr_copy)   #메모리 주소 비교 : False. 깊은 복사이기 때문
print(np.array_equal(np_arr, np_arr_copy))# 값 자체를 비교
print(np_arr == np_arr_copy)     #원소 (item)마다 비교

# numpy 배열 연산
np_arr =np.array([10, 20, 30, 40, 50])
print(f'np_arr{np_arr}')

print(f'np_arr + 10 {np_arr + 10}')
print(f'np_arr - 10 {np_arr - 10}')
print(f'np_arr * 5 {np_arr * 5}')
print(f'np_arr * 10 {np_arr / 10}') #실수형으로 결괏값이 나옴
print(f'np_arr % 10 {np_arr % 10}')
print(f'np_arr // 10 {np_arr // 10}')

# numpy 배열 속성 확인
# 1. 배열 원소 데이터 타입(dtype)설정
np_arr = np.array([1, 2, 3], dtype=float) #원래 타입은 정수형이다.
print(f'np_arr: {np_arr}')

np_arr = np_arr.astype(np.int64) #정수형으로 캐스팅
print(f'np_arr: {np_arr}')
print(f'np_arr: {type(np_arr)}') #numpy.ndarray

# 2. 배열 속성(차원, 형태, 데이터타입) 확인
np_arr = np.array(
    [
        [1., 2., 3., 4., 5.],
        [10, 20, 30, 40, 50],
        [100, 200, 300, 400, 500]
    ]
)
# 배열 차원
print(f'차원: {np_arr.ndim}') #2
# 배열 형태
print(f'형태: {np_arr.shape}') #(3, 5) 3행 5열
# 배열 데이터타입
print(f'데이터 타입 : {np_arr.dtype}')

# 모든 원소가 X인 배열 만들기
# 1. ones() & ones_like()
np_arr = np.ones((3, 5), dtype=int)
print(np_arr)

py_list = [1, 2, 3]
np_arr = np.ones_like(py_list, dtype=float)
print(np_arr)

py_list = [[1, 2, 3],[4, 5, 6]]
np_arr = np.ones_like(py_list, dtype=float)
print(np_arr)

# 2. zeros() & zeros_like()
# 모든 원소가 0인 배열 만들기
np_arr = np.zeros((3, 5), dtype=int)
print(np_arr)

py_list = [1, 2, 3]
np_arr = np.zeros_like(py_list, dtype=int)
print(np_arr)

py_list = [[1, 2, 3],[4, 5, 6]]
np_arr = np.zeros_like(py_list, dtype=int)
print(np_arr)

# 3. empty() & empty_like()
np_arr = np.empty((3, 5), dtype=int)
print(np_arr)

py_list = [1, 2, 3]
np_arr = np.empty_like(py_list, dtype=int)
print(np_arr)