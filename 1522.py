s = list(input())
src_len = len(s)
ws = s.count("a")
s.extend(s[:ws - 1])
b_cnt = s[:ws].count("b")
m = b_cnt
for i in range(src_len - 1):
    b_cnt -= s[i] == "b"
    b_cnt += s[i + ws] == "b"
    m = min(m, b_cnt)
print(m)