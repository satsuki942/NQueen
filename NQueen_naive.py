import itertools
import time

def issatisfied(arr):
    size = len(arr)
    # 各列内に2つ以上配置されていないかを検査
    for i in range(0,size):
        for j in range(i+1,size):
            if arr[i] == arr[j]:
                return False
    # 各ななめ列に2つ以上配置されていないかを検査
    for i in range(0,size):
        for j in range(i+1,size):
            abs_diff = abs(i-j)
            if abs(arr[i]-arr[j]) == abs_diff:
                return False
    return True

def solve_nqueen(n):
    # 順列を使用し全てのqueen配置を生成
    queenpos_set = []
    for i in range(1,n+1):
        queenpos_set.append(i)
    possible_boardlist = itertools.permutations(queenpos_set,n)

    # 生成したqueen配置全てに対し、制約を満たすかを検査。満たせばその配置を返す
    for elem in possible_boardlist:
        if issatisfied(elem):
            return elem
        
    return False

def main():
    size = int(input())
    start_time = time.time()
    b = solve_nqueen(size)
    end_time = time.time()
    diff_time = end_time - start_time
    if b:
        print(f"{size}-Queens Pazzle is Satisfiable: {diff_time:.4f} seconds")
        for i in range(0,size):
            pos = size*i+b[i]
            print(pos,end=" ")
        print("")
    else:
        print(f"{size}-Queens Pazzle is Unatisfiable: {diff_time:.4f} seconds")

main()
