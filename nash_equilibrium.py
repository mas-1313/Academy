import random
import textwrap

# 乱数により利得行列を生成
A = []
B = []
for i in range(2):
    A.append([random.randrange(10, 60, 5), random.randrange(10, 60, 5)])
    B.append([random.randrange(10, 60, 5), random.randrange(10, 60, 5)])

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

# 利得行列を表示
print(string)

"""
以下ではA社/B社の最適反応戦略を求める
"""

# B社の戦略を固定してA社の最適反応戦略を求める処理
a_best_stra = set()
# 戦略X, 戦略Yでループ
for loop_idx in range(2):
    scores = []
    # A社の最高得点を求める
    if A[0][loop_idx] == A[1][loop_idx]:
        scores.append(A[0][loop_idx])
        scores.append(A[1][loop_idx])
    else:
        scores.append(max(A[0][loop_idx], A[1][loop_idx]))

    # A社にとって最高得点の解がA社の最適反応戦略
    for score in scores:
        if score == A[0][loop_idx]:
            a_best_stra.add((score, B[0][loop_idx]))
        if score == A[1][loop_idx]:
            a_best_stra.add((score, B[1][loop_idx]))


# A社の戦略を固定してB社の最適反応戦略を求める処理
b_best_stra = set()
# 戦略X, 戦略Yでループ
for loop_idx in range(2):
    scores = []
    # B社の最高得点を求める
    if B[loop_idx][0] == B[loop_idx][1]:
        scores.append(B[loop_idx][0])
        scores.append(B[loop_idx][1])
    else:
        scores.append(max(B[loop_idx][0], B[loop_idx][1]))

    # B社にとって最高得点の解がB社の最適反応戦略
    for score in scores:
        if score == B[loop_idx][0]:
            b_best_stra.add((A[loop_idx][0], score))
        if score == B[loop_idx][1]:
            b_best_stra.add((A[loop_idx][1], score))

print("A社/最適反応戦略: ", a_best_stra)
print("B社/最適反応戦略: ", b_best_stra)

# A社/B社 互いの最適反応戦略の組み合わせがナッシュ均衡解
nash = set()
for a in a_best_stra:
    if a in b_best_stra:
        nash.add(a)

if len(nash) == 0:
    print("\n解無し")
else:
    print("\nナッシュ均衡解: ", nash)
