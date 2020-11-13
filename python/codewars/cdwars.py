# %%
# Mumbling

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(t):
    return '-'.join(map(str.title ,[a * (i+1)  for i, a in enumerate(t)]))


accum("abcd")
accum("ZpglnRxqenU")

# %%
