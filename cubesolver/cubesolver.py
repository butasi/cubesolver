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
            "Ga": "R2' u R' U R' U' R u' R2' y' R' U R",
            "Gb": "R' U' R y R2' u R' U R U' R u' R2'",
            "Gc": "R2' u' R U' R U R' u R2 f R' f'",
            "Gd": "R U R' y' R2' u' R U' R' U R' u R2",
            "V": "R' U R' d' R' F' R2 U' R' U R' F R F",
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
    def orient_U(cls, source, target):
        num_turns = (target - source) % 4
        if num_turns == 1:
            return "U'"
        elif num_turns == 2:
            return "U2"
        elif num_turns == 3:
            return "U"
        else:
            return None

    @classmethod
    def solve_pll(cls, cube):
        moves = []
        complete_edges = [i for i in range(1,5) if np.all(cube.cube[[i],[0]] == cube.cube[[i],[0],[1]])]
        headlights = [i for i in range(1,5) if cube.cube[i][0][0] == cube.cube[i][0][2] and cube.cube[i][0][0] != cube.cube[i][0][1]]
        left_blocks = [i for i in range(1,5) if cube.cube[i][0][0] == cube.cube[i][0][1] and cube.cube[i][0][0] != cube.cube[i][0][2]]
        right_blocks = [i for i in range(1,5) if cube.cube[i][0][2] == cube.cube[i][0][1] and cube.cube[i][0][2] != cube.cube[i][0][1]]
        scrambled_edges = 4 - (len(complete_edges) + len(headlights) + len(left_blocks) + len(right_blocks))

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
            orient_move = orient_U(complete_edges[0], 3)
            if orient_move is not None:
                moves.append(orient_move)
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
            if ((right_blocks[0] + 1) % 4 == left_blocks[0]):
                # A perms pre-rotations
                orient_move = orient_U(right_blocks[0], 4)
                if orient_move is not None:
                    moves.append(orient_move)
                else:
                    if headlights[0] == 3:
                        # Aa perm
                        moves.extend(cls.algorithms["PLL"]["Aa"].split(" "))
                    else:
                        # Ab perm
                        moves.extend(cls.algorithms["PLL"]["Ab"].split(" "))
            else:
                # T perm
                orient_move = orient_U(headlights[0], 4)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["T"].split(" "))
        elif len(scrambled_edges) == 4:
            # E perm
            if cube.cube[4][0][0] == cube.cube[2][0][2]:
                moves.append("U")
            moves.extend(cls.algorithms["PLL"]["E"].split(" "))
        elif len(complete_edges) == 1 and len(left_blocks) == 3:
            # Ja perm
            orient_move = orient_U(complete_edges[0], 1)
            if orient_move is not None:
                moves.append(orient_move)
            moves.extend(cls.algorithms["PLL"]["Ja"].split(" "))
        elif len(complete_edges) == 1 and len(right_blocks) == 3:
            # Jb perm
            orient_move = orient_U(complete_edges[0], 4)
            if orient_move is not None:
                moves.append(orient_move)
            moves.extend(cls.algorithms["PLL"]["Jb"].split(" "))
        elif len(headlights) == 1 and len(left_blocks) == 1 and len(scrambled_edges) == 2:
            if (left_blocks[0] == (headlights[0] + 1) % 4):
                # Ra perm
                orient_move = orient_U(left_blocks[0], 1)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Ra"].split(" "))
            elif (left_blocks[0] == (headlights[0] + 2) % 4):
                # Gd perm
                orient_move = orient_U(left_blocks[0], 2)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Gd"].split(" "))
            else:
                # Gc perm
                orient_move = orient_U(left_blocks[0], 3)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Gc"].split(" "))
        elif len(headlights) == 1 and len(right_blocks) == 1 and len(scrambled_edges) == 2:
            if ((right_blocks[0] + 1) % 4 == headlights[0]):
                # Rb perm
                orient_move = orient_U(right_blocks[0], 1)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Rb"].split(" "))
            elif ((right_blocks[0] + 2) % 4 == headlights[0]):
                # Gb perm
                orient_move = orient_U(right_blocks[0], 2)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Gb"].split(" "))
            else:
                # Ga perm
                orient_move = orient_U(right_blocks[0], 0)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Ga"].split(" "))
        elif len(complete_edges) == 1 and len(scrambled_edges) == 3:
            # F perm
            orient_move = orient_U(complete_edges[0], 4)
            if orient_move is not None:
                moves.append(orient_move)
            moves.extend(cls.algorithms["PLL"]["F"].split(" "))
        elif len(left_blocks) == 1 and len(right_blocks) == 1 and len(scrambled_edges) == 2:
            orient_move = orient_U(complete_edges[0], 1)
            if orient_move is not None:
                moves.append(orient_move)
            if ((right_blocks[0] + 1) % 4 == left_blocks[0]):
                # V perm
                moves.extend(cls.algorithms["PLL"]["V"].split(" "))
            else:
                # Y perm
                moves.extend(cls.algorithms["PLL"]["Y"].split(" "))
        elif len(right_blocks) == 4:
            # Na perm
            if cube.cube[1][0][0] == cube.cube[3][0][1]:
                moves.append("U")
            moves.extend(cls.algorithms["PLL"]["Na"].split(" "))
        elif len(left_blocks) == 4:
            # Nb perm
            if cube.cube[1][0][2] == cube.cube[3][0][1]:
                moves.append("U")
            moves.extend(cls.algorithms["PLL"]["Nb"].split(" "))
        else:
            raise Exception("Attempting to solve an unsolvable cube")

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

