import sys
import numpy as np

class Cube(object):
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
            elif "x" in move:
                self.move_x(prime, double)
            elif "y" in move:
                self.move_y(prime, double)
            else:
                raise Exception("Failed to attempt unrecognized move {}".format(move))

    def execute_string(self, moves=""):
        moves = moves.split(" ")
        return self.execute_list(moves)

    def show(self):
        print self.cube


class CubeSolver(object):

    algorithms = {
        "PLL": {
            "Aa": "x R' U R' D2 R U' R' D2 R2",
            "Ab": "x R2 D2 R U R' D2 R U' R",
            "E": "x' R U' R' D R U R' D' R U R' D R U' R' D'",
            "Ua": "R U' R U R U R U' R' U' R2",
            "Ub": "R2 U R U R' U' R' U' R' U R'",
            "H": "M2' U M2' U2 M2' U M2'",
            "Z": "M2' U M2' U M' U2 M2' U2 M' U2",
            "Ja": "",
            "Jb": "",
            "T": "",
            "Rb": "",
            "Ra": "",
            "F": "",
            "Ga": "",
            "Gb": "",
            "Gc": "",
            "Gd": "",
            "V": "",
            "Na": "",
            "Nb": "",
            "Y": ""
        },
        "OLL": {
        },
        "F2L": {
        }
    }

    @classmethod
    def check_cross(cls, cube):
        face = np.all(cube.cube[[5],[0,1,1,2],[1,0,2,1]] == cube.cube[5][1][1])
        front_edge = cube.cube[1][2][1] == cube.cube[1][1][1]
        right_edge = cube.cube[2][2][1] == cube.cube[2][1][1]
        back_edge = cube.cube[3][2][1] == cube.cube[3][1][1]
        left_edge = cube.cube[4][2][1] == cube.cube[4][1][1]
        return face and front_edge and right_edge and back_edge and left_edge

    @classmethod
    def check_bottom(cls, cube):
        face = np.all(cube.cube[5] == cube.cube[5][1][1])
        front_edges = np.all(cube.cube[[1],[2]] == cube.cube[1][1][1])
        right_edges = np.all(cube.cube[[2],[2]] == cube.cube[2][1][1])
        back_edges = np.all(cube.cube[[3],[2]] == cube.cube[3][1][1])
        left_edges = np.all(cube.cube[[4],[2]] == cube.cube[4][1][1])
        return face and front_edges and right_edges and back_edges and left_edges

    @classmethod
    def check_middle(cls, cube):
        front_middle = np.all(cube.cube[[1],[2],[0,2]] == cube.cube[1][2][1])
        right_middle = np.all(cube.cube[[2],[2],[0,2]] == cube.cube[2][2][1])
        back_middle = np.all(cube.cube[[3],[2],[0,2]] == cube.cube[3][2][1])
        left_middle = np.all(cube.cube[[4],[2],[0,2]] == cube.cube[4][2][1])
        return front_middle and right_middle and back_middle and left_middle

    @classmethod
    def check_top(cls, cube):
        face = np.all(cube.cube[0] == cube.cube[0][1][1])
        return face

    @classmethod
    def check_ll(cls, cube):
        front_edges = np.all(cube.cube[[1],[0]] == cube.cube[1][1][1])
        right_edges = np.all(cube.cube[[2],[0]] == cube.cube[2][1][1])
        back_edges = np.all(cube.cube[[3],[0]] == cube.cube[3][1][1])
        left_edges = np.all(cube.cube[[4],[0]] == cube.cube[4][1][1])
        return cls.check_top(cube) and front_edges and right_edges and back_edges and left_edges

    @classmethod
    def check_solved(cls, cube):
        return cls.check_bottom(cube) and cls.check_middle(cube) and cls.check_ll(cube)

    @classmethod
    def solve_pll(cls, cube):
        moves = []
        complete_edges = [i for i in range(1,5) if np.all(cube.cube[[i],[0]] == cube.cube[[i],[0],[1]])]
        semi_complete_edges = [i for i in range(1,5) if cube.cube[i][0][0] == cube.cube[i][0][2] and cube.cube[i][0][0] != cube.cube[i][0][1]]

        if len(complete_edges) == 4:
            # U rotations
            if cube.cube[1][0][1] == cube.cube[2][1][1]:
                moves.append("U'")
            elif cube.cube[1][0][1] == cube.cube[4][1][1]:
                moves.append("U")
            elif cube.cube[1][0][1] == cube.cube[3][1][1]:
                moves.append("U2")
        elif len(complete_edges) == 1 and len(semi_complete_edges) == 3:
            # U perms pre-rotations
            if complete_edges[0] == 1:
                moves.append("U2")
            elif complete_edges[0] == 2:
                moves.append("U'")
            elif complete_edges[0] == 4:
                moves.append("U")
            else:
                if cube.cube[1][0][1] == cube.cube[2][0][0]:
                    # Ua perm
                    moves.extend(cls.algorithms["PLL"]["Ua"].split(" "))
                else:
                    # Ub perm
                    moves.extend(cls.algorithms["PLL"]["Ub"].split(" "))
        elif len(semi_complete_edges) == 4:
            if cube.cube[1][0][1] == cube.cube[3][0][0]:
                # H perm
                moves.extend(cls.algorithms["PLL"]["H"].split(" "))
            else:
                # Z perm
                if cube.cube[1][0][1] == cube.cube[4][0][0]:
                    moves.append("U")
                moves.extend(cls.algorithms["PLL"]["Z"].split(" "))

        if len(moves) > 0:
            cube.execute_list(moves)
            moves.extend(cls.solve_pll(cube))

        return moves

    @classmethod
    def solve(cls, cube):
        solution = []
        moves = []
        if not cls.check_cross(cube):
            # solve cross
            pass
        if not cls.check_bottom(cube):
            # solve f2l
            pass
        if not cls.check_middle(cube):
            # solve f2l
            pass
        if not cls.check_top(cube):
            # solve oll
            pass
        if not cls.check_ll(cube):
            moves.extend(cls.solve_pll(cube))
            solution.extend(moves)
        return solution


def main(argv):
    #test_cube = Cube("test")
    #print test_cube.show()
    #test_cube.execute_string("x")
    #print test_cube.show()
    #test_cube.execute_string("x'")
    #print test_cube.show()
    solved_cube = Cube()
    cube = Cube()
    assert np.array_equal(cube.cube, solved_cube.cube)
    cube.execute_string("R U R' U' R U R' U' R U R' U' R U R' U' R U R' U' R U R' U'")
    assert np.array_equal(cube.cube, solved_cube.cube)
    cube.execute_string("M' U M' U M' U M' U M' U M' U M' U M' U")
    assert np.array_equal(cube.cube, solved_cube.cube)
    cube.execute_string("F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R' F R U R'")
    assert np.array_equal(cube.cube, solved_cube.cube)
    assert CubeSolver.check_solved(cube)
    cube.execute_string("U")
    assert CubeSolver.check_cross(cube)
    assert CubeSolver.check_bottom(cube)
    assert CubeSolver.check_middle(cube)
    assert CubeSolver.check_top(cube)
    assert not CubeSolver.check_ll(cube)
    cube.execute_string("U' R U R'")
    assert CubeSolver.check_cross(cube)
    assert not CubeSolver.check_bottom(cube)
    assert not CubeSolver.check_middle(cube)
    assert not CubeSolver.check_top(cube)
    assert not CubeSolver.check_ll(cube)
    cube.execute_string("R U' R'")
    assert CubeSolver.check_solved(cube)
    cube.execute_string("R U' R U R U R U' R' U' R2 U'")
    solution = CubeSolver.solve(cube)
    print " ".join(solution)
    cube.execute_string("R2 U R U R' U' R' U' R' U R' U")
    solution = CubeSolver.solve(cube)
    print " ".join(solution)
    cube.execute_string("M2' U M2' U2 M2' U M2'")
    solution = CubeSolver.solve(cube)
    print " ".join(solution)
    cube.execute_string("M2' U M2' U M' U2 M2' U2 M' U2")
    solution = CubeSolver.solve(cube)
    print " ".join(solution)

if __name__ == "__main__":
    main(sys.argv[1:])
