import numpy as np

seq_a = "GACGGATTAG"
seq_b = "GATCGGAATAG"


scoring_matrix = np.zeros((len(seq_a) + 1, len(seq_b) + 1))
helper_matrix = np.zeros((len(seq_a), len(seq_b)))

# scoring scheme
same_score = 1
diff_score = 0
space_score = -1

# build helper matrix
for i in range(len(seq_a)):
    for j in range(len(seq_b)):
        if seq_a[i] == seq_b[j]:
            helper_matrix[i][j] = same_score
        else:
            helper_matrix[i][j] = diff_score

print(helper_matrix)

# Initialize scoring matrix
for i in range(len(seq_a) + 1):
    scoring_matrix[i][0] = i * space_score
for j in range(len(seq_b) + 1):
    scoring_matrix[0][j] = j * space_score

# fill scoring matrix
for i in range(1, len(seq_a) + 1):
    for j in range(1, len(seq_b) + 1):
        scoring_matrix[i][j] = max(scoring_matrix[i - 1][j - 1] + helper_matrix[i - 1][j - 1],
                                scoring_matrix[i - 1][j] + space_score,
                                scoring_matrix[i][j - 1] + space_score)

print(scoring_matrix)

# modifying to output optimal alignment as well

aligned_a = ""
aligned_b = ""

ti = len(seq_a)
tj = len(seq_b)

while (ti > 0 and tj > 0):

    if (ti > 0 and tj > 0 and scoring_matrix[ti][tj] == scoring_matrix[ti - 1][tj - 1] + helper_matrix[ti - 1][
        tj - 1]):

        aligned_a = seq_a[ti - 1] + aligned_a
        aligned_b = seq_b[tj - 1] + aligned_b

        ti = ti - 1
        tj = tj - 1

    elif (ti > 0 and scoring_matrix[ti][tj] == scoring_matrix[ti - 1][tj] + space_score):
        aligned_a = seq_a[ti - 1] + aligned_a
        aligned_b = " " + aligned_b

        ti = ti - 1
    else:
        aligned_a = " " + aligned_a
        aligned_b = seq_b[tj - 1] + aligned_b

        tj = tj - 1

print(aligned_a)
print(aligned_b)
