class Backend:
    N = 2
    M = 10

    def __init__(self) -> None:
        self.matrix: list = []
        self.new_matrix: list = []
        self.napolnit()

    def napolnit(self):
        list_dr = [
            [30, 53, 36, 55, 60, 75, 40, 43, 67, 47],
            [12, 9.8, 15.5, 13.2, 14, 11.1, 12.1, 12.5, 11.3, 10]
        ]
        self.matrix = list_dr

    @staticmethod
    def sort(user_list: list):
        list_dr = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        for i in range(2):
            for j in range(10):
                if i == 1:
                    list_dr[j].append(f'{j+1}')
                    list_dr[j].append(user_list[i][j])
                    list_dr[j].append(user_list[i-1][j])

        sorted_list = sorted(list_dr, key=lambda x: x[1])
        for i in sorted_list:
            print(i)
        return sorted_list

    def normalization(self):
        max1 = 0
        max2 = 0
        for i in range(len(self.matrix)):
            for j in range(10):
                if i == 0 and self.matrix[i][j] > max1:
                    max1 = self.matrix[i][j]
                if i == 1 and self.matrix[i][j] > max2:
                    max2 = self.matrix[i][j]
        for i in range(2):
            for j in range(10):
                if i == 0:
                    self.matrix[i][j] = self.matrix[i][j]/max1
                if i == 1:
                    self.matrix[i][j] = self.matrix[i][j]/max2
        sorted_list = Backend.sort(self.matrix)
        self.yslovaie_neo(sorted_list)
        return sorted_list

    def yslovaie_neo(self, matrix: list):
        sum_str = 0
        for i in range(self.M):
            for j in range(self.N+1):
                if j != 0:
                    sum_str += matrix[i][j]
                    if j == 2:
                        matrix[i].append(sum_str/self.M)
                        sum_str = 0
        print('Добавдение критерия')
        for i in matrix:
            print(i)

        sorted_list = sorted(matrix, key=lambda x: x[3])
        max_value = sorted_list[-1][3]

        for i in matrix:
            print(i)

        print('------------')

        for i in range(10):
            print(sorted_list[i])

        print('-------------')
        print(f'Максимальное значение критерия равно {max_value}')

b = Backend()
list = b.normalization()
