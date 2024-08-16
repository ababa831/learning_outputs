# AC: 2024/08/13 4:08
# スマートでない（切り上げをワンライナーで表現するには？）
h, a = map(int, input().split())
b = h % a
n_p = h // a
if b == 0:
    print(n_p)
else:
    print(n_p + 1)