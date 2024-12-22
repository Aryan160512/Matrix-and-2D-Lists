matrix = [75, 45, 52], [74, 95, 26], [47, 68, 19]

print('The Primary Diagonal: ')
for i in range(len(matrix)):
    print(matrix[i][i])

print('\nThe Secondary Diagonal: ')
for j in range(len(matrix)):
    print(matrix[j][(len(matrix) - j - 1)])
        