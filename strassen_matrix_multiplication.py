import copy

class Matrix:
    def __init__(self, matrix):
        for i in range(1, len(matrix)):
            if len(matrix[i]) != len(matrix[i-1]):
                raise ValueError('Input matrix not valid.')
        self.columns_count = len(matrix)
        self.rows_count = len(matrix[0])
        self.matrix = matrix

    def enlarge_matrix_dim_to_even(self):
        if self.rows_count % 2:
            for i in self.matrix:
                i.append(0)
            self.rows_count += 1
        if self.columns_count % 2:
            self.matrix.append([0 for i in range(self.rows_count)])
            self.columns_count += 1

    def slice_matrix(self, new_columns_count, new_rows_count):
        self.matrix = self.matrix[:new_columns_count]
        self.columns_count = new_columns_count
        for i in range(self.columns_count):
            self.matrix[i] = self.matrix[i][:new_rows_count]
        self.rows_count = new_rows_count

    @staticmethod
    def sum_matrix(matrix_1, matrix_2):
        answer = copy.deepcopy(matrix_1)
        for i in range(answer.columns_count):
            for j in range(answer.rows_count):
                answer.matrix[i][j] = answer.matrix[i][j] + matrix_2.matrix[i][j]
        return answer

    @staticmethod
    def subtract_matrix(matrix_1, matrix_2):
        answer = copy.deepcopy(matrix_1)
        for i in range(answer.columns_count):
            for j in range(answer.rows_count):
                answer.matrix[i][j] = answer.matrix[i][j] - matrix_2.matrix[i][j]
        return answer

    def split_matrix_to_4(self):
        self.enlarge_matrix_dim_to_even()
        a = Matrix([self.matrix[i][:self.rows_count // 2] for i in range(self.columns_count // 2)])
        b = Matrix([self.matrix[i][:self.rows_count // 2] for i in range(self.columns_count // 2, self.columns_count)])
        c = Matrix([self.matrix[i][self.rows_count // 2:self.rows_count] for i in range(self.columns_count // 2)])
        d = Matrix([self.matrix[i][self.rows_count // 2:self.rows_count] for i in range(self.columns_count // 2, self.columns_count)])
        return a, b, c, d

    @staticmethod
    def build_from_4(left_upper, right_upper, left_down, right_down):
        left_matrix = left_upper.matrix
        for i in range(len(left_matrix)):
            left_matrix[i] += left_down.matrix[i]
        right_matrix = right_upper.matrix
        for i in range(len(right_matrix)):
            right_matrix[i] += right_down.matrix[i]
        left_matrix += right_matrix
        return Matrix(left_matrix)

    @staticmethod
    def multiplication(matrix_1, matrix_2):
        if matrix_1.columns_count != matrix_2.rows_count:
            raise ValueError('Matrices {} and {} cannot be multiplied.'.format(matrix_1.matrix, matrix_2.matrix))
        answer = [[0 for i in range(matrix_1.rows_count)] for j in range(matrix_2.columns_count)]
        for i in range(matrix_1.rows_count):
            for j in range(matrix_2.columns_count):
                for k in range(matrix_1.columns_count):
                    answer[j][i] += matrix_1.matrix[k][i] * matrix_2.matrix[j][k]
        return Matrix(answer)

    @staticmethod
    def by_4_multiplication(matrix_1, matrix_2):
        if matrix_1.columns_count != matrix_2.rows_count:
            raise ValueError('Matrices {} and {} cannot be multiplied.'.format(matrix_1.matrix, matrix_2.matrix))
        if matrix_1.columns_count <= 2 or matrix_2.rows_count <= 2:
            return Matrix.multiplication(matrix_1, matrix_2)
        answer_columns_count = matrix_2.columns_count
        answer_rows_count = matrix_1.rows_count
        a, b, c, d = matrix_1.split_matrix_to_4()
        e, f, g, h = matrix_2.split_matrix_to_4()
        ae = Matrix.by_4_multiplication(a, e)
        af = Matrix.by_4_multiplication(a, f)
        bg = Matrix.by_4_multiplication(b, g)
        bh = Matrix.by_4_multiplication(b, h)
        ce = Matrix.by_4_multiplication(c, e)
        cf = Matrix.by_4_multiplication(c, f)
        dg = Matrix.by_4_multiplication(d, g)
        dh = Matrix.by_4_multiplication(d, h)
        left_upper = Matrix.sum_matrix(ae, bg)
        right_upper = Matrix.sum_matrix(af, bh)
        left_down = Matrix.sum_matrix(ce, dg)
        right_down = Matrix.sum_matrix(cf, dh)
        answer = Matrix.build_from_4(left_upper, right_upper, left_down, right_down)
        answer.slice_matrix(answer_columns_count, answer_rows_count)
        return answer

    @staticmethod
    def strassen_multiplication(matrix_1, matrix_2):
        if matrix_1.columns_count != matrix_2.rows_count:
            raise ValueError('Matrices {} and {} cannot be multiplied.'.format(matrix_1.matrix, matrix_2.matrix))
        if matrix_1.columns_count <= 2 or matrix_2.rows_count <= 2:
            return Matrix.multiplication(matrix_1, matrix_2)
        answer_columns_count = matrix_2.columns_count
        answer_rows_count = matrix_1.rows_count
        a, b, c, d = matrix_1.split_matrix_to_4()
        e, f, g, h = matrix_2.split_matrix_to_4()
        p1 = Matrix.multiplication(a, Matrix.subtract_matrix(f, h))
        p2 = Matrix.multiplication(Matrix.sum_matrix(a, b), h)
        p3 = Matrix.multiplication(Matrix.sum_matrix(c, d), e)
        p4 = Matrix.multiplication(d, Matrix.subtract_matrix(g, e))
        p5 = Matrix.multiplication(Matrix.sum_matrix(a, d), Matrix.sum_matrix(e, h))
        p6 = Matrix.multiplication(Matrix.subtract_matrix(b, d), Matrix.sum_matrix(g, h))
        p7 = Matrix.multiplication(Matrix.subtract_matrix(a, c), Matrix.sum_matrix(e, f))
        left_upper = Matrix.sum_matrix(p5, p4)
        left_upper = Matrix.subtract_matrix(left_upper, p2)
        left_upper = Matrix.sum_matrix(left_upper, p6)
        right_upper = Matrix.sum_matrix(p1, p2)
        left_down = Matrix.sum_matrix(p3, p4)
        right_down = Matrix.sum_matrix(p1, p5)
        right_down = Matrix.subtract_matrix(right_down, p3)
        right_down = Matrix.subtract_matrix(right_down, p7)
        answer = Matrix.build_from_4(left_upper, right_upper, left_down, right_down)
        answer.slice_matrix(answer_columns_count, answer_rows_count)
        return answer

a = [[0 for i in range(3)] for j in range(4)]
a[0][0] = 1
a[0][1] = 5
a[0][2] = 0
a[1][0] = 2
a[1][1] = 6
a[1][2] = 9
a[2][0] = 3
a[2][1] = 7
a[2][2] = 1
a[3][0] = 4
a[3][1] = 8
a[3][2] = 0

b = [[0 for i in range(4)] for j in range(2)]
b[0][0] = 7
b[0][1] = 0
b[0][2] = 9
b[0][3] = 6
b[1][0] = 8
b[1][1] = 2
b[1][2] = 4
b[1][3] = 1


print(Matrix.strassen_multiplication(Matrix(a), Matrix(b)).matrix)
