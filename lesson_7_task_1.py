class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f"{self.matrix}"

    def __add__(self, other):
        return Matrix([[self.matrix[0][0]+other.matrix[0][0], self.matrix[0][1]+other.matrix[0][1]], [self.matrix[1][0]+other.matrix[1][0], self.matrix[1][1]+other.matrix[1][1]]])

matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[3, 5], [4, 2]])
print(matrix_1 + matrix_2)