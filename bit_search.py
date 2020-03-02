# bit全探索
for i in range(2**n):
  for j in range(n):
    if (i>>j) & 1:
      # 任意の処理
      
# nグループ分け bit全探索は2グループにしか分けられないが、それ以上に分けたいことがあるため
num = 'グループ数'
for i in range(num**n):
  G=[[] for _ in range(num)]
  for j in range(n):
    G[(i//(num**j))%num].append(j)
  for g in G:
    # 任意の処理
