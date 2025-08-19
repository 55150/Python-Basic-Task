class Matrix():
    def __init__(self):
        self.matrix_1 = []
        self.matrix_2 = []
        self.mul_matrix = []

    def multiplication(self):
        for i in range(3):
            row = []
            for j in range(3):
                mul = 0
                for z in range(3):
                    mul += self.matrix_1[i][z]*self.matrix_2[z][j]
                row += [mul]
            self.mul_matrix += [row]
                
        print(f" Matrix 1 : {self.matrix_1}")
        print(f" Matrix 2 : {self.matrix_2}")
        print(f" Multiplication Matrix : {self.mul_matrix}")

    def useInput(self):
        for mat in range(2):
            for i in range(3):
                row = []
                for j in range(3):
                    while True:
                        element = input(f"Matrix - {mat+1} Row - [{i+1}] , column - [{j+1}]\nEnter Digit Element :")
                        if not element.isdigit():
                            print('Please Enter Digit Only')
                            continue
                        else:
                            element = int(element)
                            row +=[element]
                            break
                if len(self.matrix_1) ==3 and len(row) ==3:
                    self.matrix_2 += [row]
                else:
                    self.matrix_1 += [row]
        self.multiplication()
        
m1 = Matrix()
m1.useInput()