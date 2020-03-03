def rle(S):
  # ランレングス圧縮 AAABCDEE->A3B1C1D1E2
  cnt,now,rle=1,S[0],''
  for i in range(1,len(S)):
    if now!=S[i]:
      rle+=now+str(cnt)
      cnt,now=1,S[i]
    else:
      cnt+=1
  return rle+now+str(cnt)

def rle(S):
  # ランレングス圧縮 AAABCDEE->A3BCDE2
  cnt,now,rle=1,S[0],''
  for i in range(1,len(S)):
    if now!=S[i]:
      rle+=now if cnt==1 else now+str(cnt)
      cnt,now=1,S[i]
    else:
      cnt+=1
  return rle+now if cnt==1 else rle+now+str(cnt)
