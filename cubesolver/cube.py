import numpy as np

class Cube:
    '''
    Numpy Array Faces
    0 = U
    1 = F
    2 = R
    3 = B
    4 = L
    5 = D
    '''

    def __init__(self, arr = None):
        if arr == "test":
            self.cube = np.array([
                [
                    ['Y1', 'Y2', 'Y3'],
                    ['Y4', 'Y5', 'Y6'],
                    ['Y7', 'Y8', 'Y9']
                ], [
                    ['G1', 'G2', 'G3'],
                    ['G4', 'G5', 'G6'],
                    ['G7', 'G8', 'G9']
                ], [
                    ['O1', 'O2', 'O3'],
                    ['O4', 'O5', 'O6'],
                    ['O7', 'O8', 'O9']
                ], [
                    ['B1', 'B2', 'B3'],
                    ['B4', 'B5', 'B6'],
                    ['B7', 'B8', 'B9']
                ], [
                    ['R1', 'R2', 'R3'],
                    ['R4', 'R5', 'R6'],
                    ['R7', 'R8', 'R9']
                ], [
                    ['W1', 'W2', 'W3'],
                    ['W4', 'W5', 'W6'],
                    ['W7', 'W8', 'W9']
                ]
            ])
        else:
            if arr is None:
                arr = ['Y','Y','Y','Y','Y','Y','Y','Y','Y','G','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','O','B','B','B','B','B','B','B','B','B','R','R','R','R','R','R','R','R','R','W','W','W','W','W','W','W','W','W']
            self.cube = np.array(arr).reshape(6,3,3)

    def move_R(self, prime=False, double=False):
        if prime:
            self.cube[2] = np.rot90(self.cube[2], 1)  # CCW
            temp = self.cube[[1],[0,1,2],[2,2,2]]
            self.cube[[1],[0,1,2],[2,2,2]] = self.cube[[0],[0,1,2],[2,2,2]]
            self.cube[[0],[0,1,2],[2,2,2]] = self.cube[[3],[2,1,0],[0,0,0]]
            self.cube[[3],[2,1,0],[0,0,0]] = self.cube[[5],[0,1,2],[2,2,2]]
            self.cube[[5],[0,1,2],[2,2,2]] = temp
        else:
            self.cube[2] = np.rot90(self.cube[2], -1)  # CW
            temp = self.cube[[1],[0,1,2],[2,2,2]]
            self.cube[[1],[0,1,2],[2,2,2]] = self.cube[[5],[0,1,2],[2,2,2]]
            self.cube[[5],[0,1,2],[2,2,2]] = self.cube[[3],[2,1,0],[0,0,0]]
            self.cube[[3],[2,1,0],[0,0,0]] = self.cube[[0],[0,1,2],[2,2,2]]
            self.cube[[0],[0,1,2],[2,2,2]] = temp
        if double:
            self.move_R(prime)
        return True

    def move_L(self, prime=False, double=False):
        if prime:
            self.cube[4] = np.rot90(self.cube[4], 1)  # CCW
            temp = self.cube[[1],[0,1,2],[0,0,0]]
            self.cube[[1],[0,1,2],[0,0,0]] = self.cube[[5],[0,1,2],[0,0,0]]
            self.cube[[5],[0,1,2],[0,0,0]] = self.cube[[3],[2,1,0],[2,2,2]]
            self.cube[[3],[2,1,0],[2,2,2]] = self.cube[[0],[0,1,2],[0,0,0]]
            self.cube[[0],[0,1,2],[0,0,0]] = temp
        else:
            self.cube[4] = np.rot90(self.cube[4], -1)  # CW
            temp = self.cube[[1],[0,1,2],[0,0,0]]
            self.cube[[1],[0,1,2],[0,0,0]] = self.cube[[0],[0,1,2],[0,0,0]]
            self.cube[[0],[0,1,2],[0,0,0]] = self.cube[[3],[2,1,0],[2,2,2]]
            self.cube[[3],[2,1,0],[2,2,2]] = self.cube[[5],[0,1,2],[0,0,0]]
            self.cube[[5],[0,1,2],[0,0,0]] = temp
        if double:
            self.move_L(prime)
        return True

    def move_U(self, prime=False, double=False):
        if prime:
            self.cube[0] = np.rot90(self.cube[0], 1)  # CCW
            temp = self.cube[[1],[0]]
            self.cube[[1],[0]] = self.cube[[4],[0]]
            self.cube[[4],[0]] = self.cube[[3],[0]]
            self.cube[[3],[0]] = self.cube[[2],[0]]
            self.cube[[2],[0]] = temp
        else:
            self.cube[0] = np.rot90(self.cube[0], -1)  # CW
            temp = self.cube[[1],[0]]
            self.cube[[1],[0]] = self.cube[[2],[0]]
            self.cube[[2],[0]] = self.cube[[3],[0]]
            self.cube[[3],[0]] = self.cube[[4],[0]]
            self.cube[[4],[0]] = temp
        if double:
            self.move_U(prime)
        return True

    def move_D(self, prime=False, double=False):
        if prime:
            self.cube[5] = np.rot90(self.cube[5], 1)  # CCW
            temp = self.cube[[1],[2]]
            self.cube[[1],[2]] = self.cube[[2],[2]]
            self.cube[[2],[2]] = self.cube[[3],[2]]
            self.cube[[3],[2]] = self.cube[[4],[2]]
            self.cube[[4],[2]] = temp
        else:
            self.cube[5] = np.rot90(self.cube[5], -1)  # CW
            temp = self.cube[[1],[2]]
            self.cube[[1],[2]] = self.cube[[4],[2]]
            self.cube[[4],[2]] = self.cube[[3],[2]]
            self.cube[[3],[2]] = self.cube[[2],[2]]
            self.cube[[2],[2]] = temp
        if double:
            self.move_D(prime)
        return True

    def move_F(self, prime=False, double=False):
        if prime:
            self.cube[1] = np.rot90(self.cube[1], 1)  # CCW
            temp = self.cube[[0],[2,2,2],[2,1,0]]
            self.cube[[0],[2]] = self.cube[[2],[0,1,2],[0,0,0]]
            self.cube[[2],[0,1,2],[0,0,0]] = self.cube[[5],[0,0,0],[2,1,0]]
            self.cube[[5],[0,0,0],[0,1,2]] = self.cube[[4],[0,1,2],[2,2,2]]
            self.cube[[4],[0,1,2],[2,2,2]] = temp
        else:
            self.cube[1] = np.rot90(self.cube[1], -1)  # CW
            temp = self.cube[[0],[2,2,2],[0,1,2]]
            self.cube[[0],[2]] = self.cube[[4],[2,1,0],[2,2,2]]
            self.cube[[4],[0,1,2],[2,2,2]] = self.cube[[5],[0,0,0],[0,1,2]]
            self.cube[[5],[0,0,0],[0,1,2]] = self.cube[[2],[2,1,0],[0,0,0]]
            self.cube[[2],[0,1,2],[0,0,0]] = temp
        if double:
            self.move_R(prime)
        return True

    def move_B(self, prime=False, double=False):
        if prime:
            self.cube[3] = np.rot90(self.cube[3], 1)  # CCW
            temp = self.cube[[0],[0,0,0],[0,1,2]]
            self.cube[[0],[0]] = self.cube[[4],[2,1,0],[0,0,0]]
            self.cube[[4],[0,1,2],[0,0,0]] = self.cube[[5],[2,2,2],[0,1,2]]
            self.cube[[5],[2,2,2],[0,1,2]] = self.cube[[2],[2,1,0],[2,2,2]]
            self.cube[[2],[0,1,2],[2,2,2]] = temp
        else:
            self.cube[3] = np.rot90(self.cube[3], -1)  # CW
            temp = self.cube[[0],[0,0,0],[2,1,0]]
            self.cube[[0],[0]] = self.cube[[2],[0,1,2],[2,2,2]]
            self.cube[[2],[0,1,2],[2,2,2]] = self.cube[[5],[2,2,2],[2,1,0]]
            self.cube[[5],[2,2,2],[0,1,2]] = self.cube[[4],[0,1,2],[0,0,0]]
            self.cube[[4],[0,1,2],[0,0,0]] = temp
        if double:
            self.move_R(prime)
        return True

    def move_M(self, prime=False, double=False):
        if prime:  # CW from right
            temp = self.cube[[1],[0,1,2],[1,1,1]]
            self.cube[[1],[0,1,2],[1,1,1]] = self.cube[[5],[0,1,2],[1,1,1]]
            self.cube[[5],[0,1,2],[1,1,1]] = self.cube[[3],[2,1,0],[1,1,1]]
            self.cube[[3],[2,1,0],[1,1,1]] = self.cube[[0],[0,1,2],[1,1,1]]
            self.cube[[0],[0,1,2],[1,1,1]] = temp
        else:  # CCW from right
            temp = self.cube[[1],[0,1,2],[1,1,1]]
            self.cube[[1],[0,1,2],[1,1,1]] = self.cube[[0],[0,1,2],[1,1,1]]
            self.cube[[0],[0,1,2],[1,1,1]] = self.cube[[3],[2,1,0],[1,1,1]]
            self.cube[[3],[2,1,0],[1,1,1]] = self.cube[[5],[0,1,2],[1,1,1]]
            self.cube[[5],[0,1,2],[1,1,1]] = temp
        if double:
            self.move_M(prime)
        return True

    def move_E(self, prime=False, double=False):
        if prime:
            temp = self.cube[[1],[1]]
            self.cube[[1],[1]] = self.cube[[2],[1]]
            self.cube[[2],[1]] = self.cube[[3],[1]]
            self.cube[[3],[1]] = self.cube[[4],[1]]
            self.cube[[4],[1]] = temp
        else:
            temp = self.cube[[1],[1]]
            self.cube[[1],[1]] = self.cube[[4],[1]]
            self.cube[[4],[1]] = self.cube[[3],[1]]
            self.cube[[3],[1]] = self.cube[[2],[1]]
            self.cube[[2],[1]] = temp
        if double:
            self.move_E(prime)
        return True

    def move_S(self, prime=False, double=False):
        if prime:
            temp = self.cube[[0],[1,1,1],[2,1,0]]
            self.cube[[0],[1]] = self.cube[[2],[0,1,2],[1,1,1]]
            self.cube[[2],[0,1,2],[1,1,1]] = self.cube[[5],[1,1,1],[2,1,0]]
            self.cube[[5],[1,1,1],[0,1,2]] = self.cube[[4],[0,1,2],[1,1,1]]
            self.cube[[4],[0,1,2],[1,1,1]] = temp
        else:
            temp = self.cube[[0],[1,1,1],[0,1,2]]
            self.cube[[0],[1]] = self.cube[[4],[2,1,0],[1,1,1]]
            self.cube[[4],[0,1,2],[1,1,1]] = self.cube[[5],[1,1,1],[0,1,2]]
            self.cube[[5],[1,1,1],[0,1,2]] = self.cube[[2],[2,1,0],[1,1,1]]
            self.cube[[2],[0,1,2],[1,1,1]] = temp
        if double:
            self.move_S(prime)
        return True

    def move_u(self, prime=False, double=False):
        self.move_U(prime, double)
        self.move_E(not prime, double)
        return True

    def move_r(self, prime=False, double=False):
        self.move_R(prime, double)
        self.move_M(not prime, double)
        return True

    def move_l(self, prime=False, double=False):
        self.move_L(prime, double)
        self.move_M(prime, double)
        return True

    def move_d(self, prime=False, double=False):
        self.move_D(prime, double)
        self.move_E(prime, double)
        return True

    def move_f(self, prime=False, double=False):
        self.move_F(prime, double)
        self.move_S(prime, double)
        return True

    def move_b(self, prime=False, double=False):
        self.move_B(prime, double)
        self.move_S(not prime, double)
        return True

    def move_x(self, prime=False, double=False):
        if prime:  # CCW from right
            self.cube[2] = np.rot90(self.cube[2], 1)  # CCW right
            self.cube[4] = np.rot90(self.cube[4], -1)  # CW left
            temp = np.copy(self.cube[1])
            self.cube[1] = np.copy(self.cube[0])
            self.cube[0] = np.fliplr(self.cube[3][::-1])
            self.cube[3] = np.fliplr(self.cube[5][::-1])
            self.cube[5] = temp
        else:  # CW from right
            self.cube[2] = np.rot90(self.cube[2], -1)  # CW right
            self.cube[4] = np.rot90(self.cube[4], 1)  # CCW left
            temp = np.copy(self.cube[1])
            self.cube[1] = np.copy(self.cube[5])
            self.cube[5] = np.fliplr(self.cube[3][::-1])
            self.cube[3] = np.fliplr(self.cube[0][::-1])
            self.cube[0] = temp
        if double:
            self.move_x(prime)
        return True

    def move_y(self, prime=False, double=False):
        if prime:  # CCW from top
            self.cube[0] = np.rot90(self.cube[0], 1)  # CCW top
            self.cube[5] = np.rot90(self.cube[5], -1)  # CW bottom
            temp = np.copy(self.cube[1])
            self.cube[1] = np.copy(self.cube[4])
            self.cube[4] = np.copy(self.cube[3])
            self.cube[3] = np.copy(self.cube[2])
            self.cube[2] = temp
        else:  # CW from top
            self.cube[0] = np.rot90(self.cube[0], -1)  # CW top
            self.cube[5] = np.rot90(self.cube[5], 1)  # CCW bottom
            temp = np.copy(self.cube[1])
            self.cube[1] = np.copy(self.cube[2])
            self.cube[2] = np.copy(self.cube[3])
            self.cube[3] = np.copy(self.cube[4])
            self.cube[4] = temp
        if double:
            self.move_y(prime)
        return True

    def move_z(self, prime=False, double=False):
        if prime:  # CCW from front
            self.cube[3] = np.rot90(self.cube[3], -1)  # CW back
            self.cube[1] = np.rot90(self.cube[1], 1)  # CCW front
            temp = np.copy(np.rot90(self.cube[0], 1))
            self.cube[0] = np.rot90(self.cube[2], 1)
            self.cube[2] = np.rot90(self.cube[5], 1)
            self.cube[5] = np.rot90(self.cube[4], 1)
            self.cube[4] = temp
        else:  # CW from front
            self.cube[3] = np.rot90(self.cube[3], 1)  # CCW back
            self.cube[1] = np.rot90(self.cube[1], -1)  # CW front
            temp = np.copy(np.rot90(self.cube[0], -1))
            self.cube[0] = np.rot90(self.cube[4], -1)
            self.cube[4] = np.rot90(self.cube[5], -1)
            self.cube[5] = np.rot90(self.cube[2], -1)
            self.cube[2] = temp
        if double:
            self.move_z(prime)
        return True

    def execute_list(self, moves=[]):
        for move in moves:
            prime = True if "'" in move else False
            double = True if "2" in move else False
            if "R" in move:
                self.move_R(prime, double)
            elif "L" in move:
                self.move_L(prime, double)
            elif "U" in move:
                self.move_U(prime, double)
            elif "D" in move:
                self.move_D(prime, double)
            elif "F" in move:
                self.move_F(prime, double)
            elif "B" in move:
                self.move_B(prime, double)
            elif "M" in move:
                self.move_M(prime, double)
            elif "r" in move:
                self.move_r(prime, double)
            elif "l" in move:
                self.move_l(prime, double)
            elif "u" in move:
                self.move_u(prime, double)
            elif "d" in move:
                self.move_d(prime, double)
            elif "f" in move:
                self.move_f(prime, double)
            elif "b" in move:
                self.move_b(prime, double)
            elif "x" in move:
                self.move_x(prime, double)
            elif "y" in move:
                self.move_y(prime, double)
            elif "z" in move:
                self.move_z(prime, double)
            else:
                raise Exception("Failed to attempt unrecognized move {}".format(move))

    def execute_string(self, moves=""):
        moves = moves.split(" ")
        return self.execute_list(moves)

    def show(self):
        print self.cube

