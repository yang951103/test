a = [1,2,3,4]
for i in a:
    print(i)
    if i == 2:
        a.remove(1)
# >>>1 2 4
# 列表in等同于:
j = 0
while j < len(a):
    i = a[j]
    j += 1

d = {1:1, 2:2}
for k in d:
    d.pop(k)    # >>> RuntimeError
