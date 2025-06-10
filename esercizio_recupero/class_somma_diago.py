from string import ascii_lowercase, ascii_uppercase


def sum_primary_diagonal(matrix):
    return sum(matrix[i][i] 
               for i in range(len(matrix)))

def sum_secondary_diagonal(matrix):
    n = len(matrix)
    return sum(matrix[i][n - 1 - i]
                for i in range(n))
matri1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Somma diagonale primaria:", sum_primary_diagonal(matri1))      
print("Somma diagonale secondaria:", sum_secondary_diagonal(matri1))  


