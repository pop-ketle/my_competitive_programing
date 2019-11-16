# mod対応の組み合わせ
def comb(n,r,mod):
  def framod(n,mod,a=1):
    for i in range(1,n+1):
      a=a*i % mod
    return a
  
  def pow(n,r,mod):
    if r==0:
      return 1
    if r%2==0:
      return pow(n*n % mod, r//2, mod) % mod
    if r%2==1:
      return n*pow(n, r-1, mod) % mod
  
  a=framod(n,mod)
  b=framod(r,mod)
  c=framod(n-r,mod)
  return (a*pow(b, mod-2, mod) * pow(c, mod-2, mod)) % mod
