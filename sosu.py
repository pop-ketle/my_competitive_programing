def get_prime(n):
    # エラストテネスの篩でnまでの素数のリストをゲット
    # math.sqrt()使ったほうが若干早いっぽいけど環境依存だしとりあえずなしで
    C,P=[i for i in range(2,n+1)],[]
    while True:
        prime=min(C)
        if prime>n**0.5: break
        P.append(prime)

        i=0
        while i<len(C):
            if C[i]%prime==0: C.pop(i)
            i+=1

    for c in C:
        P.append(c)

    return P

def is_prime(n,k=50):
    import random
    # nが素数かを高速で判定
    n = abs(n)
    if n==2: return True
    if n<2 or n&1==0: return False

    # ミラー・ラビンテストというらしい ちゃんと理解してないので要復習
    d=(n-1)>>1
    while d&1==0:
        d>>=1

    for i in range(k):
        a=random.randint(1,n-1)
        t=d
        y=pow(a,t,n)
        while t!=n-1 and y!=1 and y!=n-1:
            y=pow(y,2,n)
            t<<=1
        if y!=n-1 and t&1==0:
            return False
        return True
