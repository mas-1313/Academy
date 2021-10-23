# 利得行列
A = [[40, 30], [50, 20]]
B = [[45, 50], [35, 25]]

def get_index(lists, value):
    for list in lists:
        if value in list:
            return lists.index(list)

answer_list = []

# B = xで固定したときのAの最大値
a_score = max(A[0][0], A[1][0])
a_index = get_index(A, a_score)
answer = (a_score, B[a_index][0])
answer_list.append(answer)

# B = yで固定したときのAの最大値
# Aの最大値
a_score = max(A[0][1], A[1][1])
a_index = get_index(A, a_score)
answer = (a_score, B[a_index][1])
answer_list.append(answer)


# A = xで固定したときのBの最大値
score = max(B[0])
# Bのインデックス番号を取得
index = B[0].index(score)
# 解
answer = (A[0][index], score)
if answer not in answer_list:
    answer_list.append(answer)

# A = yで固定したときのBの最大値
score = max(B[1])
# Bのインデックス番号を取得
index = B[1].index(score)
# 解
answer = (A[1][index], score)
if answer not in answer_list:
    answer_list.append(answer)

print(answer_list)
