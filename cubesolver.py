import sys
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
            else:
                raise Exception("Failed to attempt unrecognized move")

    def execute_string(self, moves=""):
        moves = moves.split(" ")
        return self.execute_list(moves)

    def show(self):
        print self.cube


class CubeSolver:

    def __init__(self, cube):
        self.cube = cube
        self.solution = []

    def check_cross(self):
        face = np.all(self.cube.cube[[5],[0,1,1,2],[1,0,2,1]] == self.cube.cube[5][1][1])
        front_edge = self.cube.cube[1][2][1] == self.cube.cube[1][1][1]
        right_edge = self.cube.cube[2][2][1] == self.cube.cube[2][1][1]
        back_edge = self.cube.cube[3][2][1] == self.cube.cube[3][1][1]
        left_edge = self.cube.cube[4][2][1] == self.cube.cube[4][1][1]
        return face and front_edge and right_edge and back_edge and left_edge

    def check_bottom(self):
        face = np.all(self.cube.cube[5] == self.cube.cube[5][1][1])
        front_edges = np.all(self.cube.cube[[1],[2]] == self.cube.cube[1][1][1])
        right_edges = np.all(self.cube.cube[[2],[2]] == self.cube.cube[2][1][1])
        back_edges = np.all(self.cube.cube[[3],[2]] == self.cube.cube[3][1][1])
        left_edges = np.all(self.cube.cube[[4],[2]] == self.cube.cube[4][1][1])
        return face and front_edges and right_edges and back_edges and left_edges

    def check_middle(self):
        front_middle = np.all(self.cube.cube[[1],[2],[0,2]] == self.cube.cube[1][2][1])
        right_middle = np.all(self.cube.cube[[2],[2],[0,2]] == self.cube.cube[2][2][1])
        back_middle = np.all(self.cube.cube[[3],[2],[0,2]] == self.cube.cube[3][2][1])
        left_middle = np.all(self.cube.cube[[4],[2],[0,2]] == self.cube.cube[4][2][1])
        return front_middle and right_middle and back_middle and left_middle

    def check_top(self):
        face = np.all(self.cube.cube[0] == self.cube.cube[0][1][1])
        return face

    def check_ll(self):
        front_edges = np.all(self.cube.cube[[1],[0]] == self.cube.cube[1][1][1])
        right_edges = np.all(self.cube.cube[[2],[0]] == self.cube.cube[2][1][1])
        back_edges = np.all(self.cube.cube[[3],[0]] == self.cube.cube[3][1][1])
        left_edges = np.all(self.cube.cube[[4],[0]] == self.cube.cube[4][1][1])
        return self.check_top() and front_edges and right_edges and back_edges and left_edges

    def check_solved(self):
        return self.check_bottom() and self.check_middle() and self.check_ll()

    def solve(self):
        if not self.check_cross():
            # solve cross
        if not self.check_bottom():
            # solve f2l
        if not self.check_middle():
            # solve f2l
        if not self.check_top():
            # solve oll
        if not self.check_ll():
            # solve pll
        return self.check_solved()


def main(argv):
    solved_cube = Cube()
    cube = Cube()
    assert np.array_equal(cube.cube, solved_cube.cube)
    cube.execute_string("R U R' U' R U R' U' R U R' U' R U R' U' R U R' U' R U R' U'")
    assert np.array_equal(cube.cube, solved_cube.cube)
    cube.execute_string("M' U M' U M' U M' U M' U M' U M' U M' U")
    assert np.array_equal(cube.cube, solved_cube.cube)
    cube.execute_string("F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R'")
    assert np.array_equal(cube.cube, solved_cube.cube)
    solver = CubeSolver(cube)
    assert solver.check_solved()
    cube.execute_string("U")
    assert solver.check_cross()
    assert solver.check_bottom()
    assert solver.check_middle()
    assert solver.check_top()
    assert not solver.check_ll()
    cube.execute_string("U' R U R'")
    assert solver.check_cross()
    assert not solver.check_bottom()
    assert not solver.check_middle()
    assert not solver.check_top()
    assert not solver.check_ll()
    cube.execute_string("R U' R'")
    assert solver.check_solved()

    cube.show()


if __name__ == "__main__":
    main(sys.argv[1:])
