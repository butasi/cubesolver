import numpy as np

class CubeSolver:

    algorithms = {
        "PLL": {
            "Aa": "x R' U R' D2 R U' R' D2 R2",
            "Ab": "x R2 D2 R U R' D2 R U' R",
            "E": "x' R U' R' D R U R' D' R U R' D R U' R' D'",
            "Ua": "R U' R U R U R U' R' U' R2",
            "Ub": "R2 U R U R' U' R' U' R' U R'",
            "H": "M2' U M2' U2 M2' U M2'",
            "Z": "M2' U M2' U M' U2 M2' U2 M' U2",
            "Ja": "R' U L' U2 R U' R' U2 L R U'",
            "Jb": "R U R' F' R U R' U' R' F R2 U' R' U'",
            "T": "R U R' U' R' F R2 U' R' U' R U R' F'",
            "Rb": "R' U2 R U2 R' F R U R' U' R' F' R2 U'",
            "Ra": "R U R' F' R U2 R' U2 R' F R U R U2 R' U'",
            "F": "R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R",
            "Ga": "R2' Uw R' U R' U' R Uw' R2' y' R' U R",
            "Gb": "R' U' R y R2' Uw R' U R U' R Uw' R2'",
            "Gc": "R2' Uw' R U' R U R' Uw R2 Fw R' Fw'",
            "Gd": "R U R' y' R2' Uw' R U' R' U R' Uw R2",
            "V": "R' U R' Dw' R' F' R2 U' R' U R' F R F",
            "Na": "z D R' U R2 D' R D U' R' U R2 D' R U' R",
            "Nb": "z U' R D' R2' U R' D U' R D' R2' U R' D R'",
            "Y": "F R U' R' U' R U R' F' R U R' U' R' F R F'"
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
        headlights = [i for i in range(1,5) if cube.cube[i][0][0] == cube.cube[i][0][2] and cube.cube[i][0][0] != cube.cube[i][0][1]]
        left_blocks = [i for i in range(1,5) if cube.cube[i][0][0] == cube.cube[i][0][1] and cube.cube[i][0][0] != cube.cube[i][0][2]]
        right_blocks = [i for i in range(1,5) if cube.cube[i][0][2] == cube.cube[i][0][1] and cube.cube[i][0][2] != cube.cube[i][0][1]]

        if len(complete_edges) == 4:
            # U rotations
            if cube.cube[1][0][1] == cube.cube[2][1][1]:
                moves.append("U'")
            elif cube.cube[1][0][1] == cube.cube[4][1][1]:
                moves.append("U")
            elif cube.cube[1][0][1] == cube.cube[3][1][1]:
                moves.append("U2")
        elif len(complete_edges) == 1 and len(headlights) == 3:
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
        elif len(headlights) == 4:
            if cube.cube[1][0][1] == cube.cube[3][0][0]:
                # H perm
                moves.extend(cls.algorithms["PLL"]["H"].split(" "))
            else:
                # Z perm
                if cube.cube[1][0][1] == cube.cube[4][0][0]:
                    moves.append("U")
                moves.extend(cls.algorithms["PLL"]["Z"].split(" "))
        elif len(headlights) == 1 and len(left_blocks) == 1 and len(right_blocks) == 1:
            if (right_blocks[0] % 4 == left_blocks[0] + 1):
                # A perms pre-rotations
                if right_blocks[0] == 1:
                    moves.append("U")
                elif right_blocks[0] == 3:
                    moves.append("U'")
                elif right_blocks[0] == 2:
                    moves.append("U2")
                else:
                    if headlights[0] == 3:
                        # Aa perm
                        moves.extend(cls.algorithms["PLL"]["Aa"].split(" "))
                    else:
                        # Ab perm
                        moves.extend(cls.algorithms["PLL"]["Ab"].split(" "))
        elif len(headlights) == 0 and len(left_blocks) == 0 and len(right_blocks) == 0:
            # E perm
            if cube.cube[4][0][0] == cube.cube[2][0][2]:
                moves.append("U")
            moves.extend(cls.algorithms["PLL"]["E"].split(" "))


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

