# cnfの配列を返す関数
def generate_cnf(n):
    # closureを入れる配列と、命題変数の数を定義
    closures = []
    propositional_var = n*n

    # cnf生成
    # 制約1: 各行には一つ以上のqueenが入っている
    for i in range(1,n):
        base = n*(i-1)
        closure = set()
        for j in range(1,n):
            closure.add(base+j)
        closures.append(closure)

    # 制約2: 各行には最大一つだけしかqueenが入らない
    for i in range(1,n):
        base = n*(i-1)
        for j in range(1,n):  
            for k in range(j+1,n):
                closure = {-(base+j),-(base+k)}
                closures.append(closure)

    # 制約3: 各列には一つ以上のqueenが入っている
    for i in range(1,n):
        closure = set()
        for j in range(1,n):
            base = n*(j-1)
            closure.add(base+i)
        closures.append(closure)

    # 制約4: 各行には最大一つだけしかqueenが入らない
    for i in range(1,n):
        for j in range(1,n):
            base_j = n*(j-1)
            for k in range(j+1,n):
                base_k = n*(k-1)
                closure = {-(base_j+i),-(base_k+i)}
                closures.append(closure)

    # 制約5: 各ななめ列には高々1つのqueenしか入らない
    for i in range(1,n):
        for j in range(1,i):
            for k in range(j+1,i):
                closure = {-(n*(i-j)+j),-(n*(i-k)+k)}
                closures.append(closure)

    for i in range(1,n-1):
        for j in range(1,i):
            for k in range(j+1,i):
                closure = {-(n*(n-j)+(n-i+j)),-(n*(n-k)+(n-i+k))}
                closures.append(closure)

    for i in range(1,n):
        for j in range(1,i):
            for k in range(j+1,i):
                closure = {-(n*(n-i+j-1)+j),-(n*(n-i+k-1)+k)}
                closures.append(closure)

    for i in range(1,n-1):
        for j in range(1,i):
            for k in range(j+1,i):
                closure = {-(n*(j-1)+(n-i+j)),-(n*(k-1)+(n-i+k))}
                closures.append(closure)

    return closures

def main():
    size_n = 8
    cnf_n = generate_cnf(size_n)

    # tmp.logに出力
    with open('tmp.log', 'w') as log:
        print(f"p cnf {size_n*size_n} {len(cnf_n)}")
        for closure in cnf_n:
            for l in closure:
                print(l,end=" ")
            print(0)
