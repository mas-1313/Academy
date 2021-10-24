import random
import textwrap

# 利得行列
A = []
B = []
for i in range(2):
    A.append([random.randrange(10, 60, 5), random.randrange(10, 60, 5)])
    B.append([random.randrange(10, 60, 5), random.randrange(10, 60, 5)])

test = False
if test:
    A = [[10, 30], [40, 15]]
    B = [[20, 40], [30, 15]]

X_X = (A[0][0],B[0][0])
X_Y = (A[0][1],B[0][1])
Y_X = (A[1][0],B[1][0])
Y_Y = (A[1][1],B[1][1])
string = textwrap.dedent('''
[利得行列]
--------------------------------
                    B社
              戦略X     戦略Y
A社  戦略X  {X_X}   {X_Y}
     戦略Y  {Y_X}   {Y_Y} 
--------------------------------
''').format(X_X=X_X, X_Y=X_Y, Y_X=Y_X,Y_Y=Y_Y)
print(string)

b_answer = []
# B = xで固定
# Aの最大値
score = max(A[0][0], A[1][0])
skip = False
# インデックス番号
if score == A[0][0] and score == A[1][0]:
    skip = True
if not skip and score == A[0][0]:
    idx = 0
elif not skip and score == A[1][0]:
    idx = 1
if not skip:
    b_answer.append((score, B[idx][0]))

# B = yで固定したときのAの最大値
# Aの最大値
score = max(A[0][1], A[1][1])
skip = False
if score == A[0][1] and score == A[1][1]:
    skip = True
if not skip and score == A[0][1]:
    idx = 0
elif not skip and score == A[1][1]:
    idx = 1
if not skip:
    b_answer.append((score, B[idx][1]))

a_answer = []
# A = xで固定したときのBの最大値
score = max(B[0][0], B[0][1])
skip = False
if score == B[0][0] and score == B[0][1]:
    skip == True
if not skip and score == B[0][0]:
    idx = 0
elif not skip and score == B[0][1]:
    idx = 1
if not skip:
    a_answer.append((A[0][idx], score))

# A = yで固定したときのBの最大値
score = max(B[1][0], B[1][1])
skip = False
print(score, B[1][0],B[1][1])
if score == B[1][0] and score == B[1][1]:
    skip = True
if not skip and score == B[1][0]:
    idx = 0
elif not skip and score == B[1][1]:
    idx = 1
if not skip:
    a_answer.append((A[1][idx], score))

nash = []
for a in a_answer:
    if a in b_answer:
        nash.append(a)

if len(nash) == 0:
    print("解無し")
else:
    print("[ナッシュ均衡解]")
    print(nash)
print("A ans:", a_answer)
print("B ans:", b_answer)