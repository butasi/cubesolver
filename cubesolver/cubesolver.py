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
            28: {
                "b_face": [1,0,1,0,1,1,1,1,1],
                "b_oll": [0,0,0,0,0,0,0,1,0,0,1,0],
                "solution": "M' U M U2 M' U M"
            },
            57: {
                "b_face": [1,0,1,1,1,1,1,0,1],
                "b_oll": [0,1,0,0,0,0,0,1,0,0,0,0],
                "solution": "R U R' U' M' U R U' r'"
            },
            20: {
                "b_face": [1,0,1,0,1,0,1,0,1],
                "b_oll": [0,1,0,0,1,0,0,1,0,0,1,0],
                "solution": "r' R U R U R' U' r2 R2' U R U' r'"
            },
            23: {
                "b_face": [1,1,1,1,1,1,0,1,0],
                "b_oll": [1,0,1,0,0,0,0,0,0,0,0,0],
                "solution": "R2' D R' U2 R D' R' U2 R'"
            },
            24: {
                "b_face": [1,1,0,1,1,1,1,1,0],
                "b_oll": [0,0,1,0,0,0,1,0,0,0,0,0],
                "solution": "r' U' L U R U' r' F"
            },
            25: {
                "b_face": [1,1,0,1,1,1,0,1,1],
                "b_oll": [1,0,0,0,0,1,0,0,0,0,0,0],
                "solution": "R' F R B' R' F' R B"
            },
            27: {
                "b_face": [0,1,0,1,1,1,1,1,0],
                "b_oll": [1,0,0,1,0,0,0,0,0,1,0,0],
                "solution": "R U R' U R U2 R'"
            },
            26: {
                "b_face": [0,1,1,1,1,1,0,1,0],
                "b_oll": [1,0,0,1,0,0,0,0,0,1,0,0],
                "solution": "R U2 R' U' R U' R'"
            },
            22: {
                "b_face": [0,1,0,1,1,1,0,1,0],
                "b_oll": [0,0,1,0,0,0,1,0,0,1,0,1],
                "solution": "R U2' R2' U' R2 U' R2' U2' R"
            },
            21: {
                "b_face": [0,1,0,1,1,1,0,1,0],
                "b_oll": [1,0,1,0,0,0,1,0,1,0,0,0],
                "solution": "R U2 R' U' R U R' U' R U' R'"
            },
            3: {
                "b_face": [0,0,0,0,1,0,0,0,1],
                "b_oll": [0,1,0,0,1,1,0,1,1,0,1,1],
                "solution": "f R U R' U' f' U' F R U R' U' F'"
            },
            4: {
                "b_face": [0,0,1,0,1,0,0,0,0],
                "b_oll": [1,1,0,1,1,0,0,1,0,1,1,0],
                "solution": "f R U R' U' f' U F R U R' U' F'"
            },
            17: {
                "b_face": [1,0,0,0,1,0,0,0,1],
                "b_oll": [0,1,0,0,1,0,1,1,0,0,1,1],
                "solution": "R U R' U R' F R F' U2 R' F R F'"
            },
            19: {
                "b_face": [1,0,1,0,1,0,0,0,0],
                "b_oll": [0,1,0,1,1,0,0,1,0,0,1,1],
                "solution": "r' R U R U R' U' r x R2' U R U'"
            },
            18: {
                "b_face": [0,0,0,0,1,0,1,0,1],
                "b_oll": [0,1,0,0,1,0,1,1,1,0,1,0],
                "solution": "F R U R' U y' R' U2 R' F R F'"
            },
            2: {
                "b_face": [0,0,0,0,1,0,0,0,0],
                "b_oll": [0,1,1,0,1,0,1,1,0,1,1,1],
                "solution": "F R U R' U' S R U R' U' f'"
            },
            1: {
                "b_face": [0,0,0,0,1,0,0,0,0],
                "b_oll": [0,1,0,1,1,1,0,1,0,1,1,1],
                "solution": "R U2 R2' F R F' U2' R' F R F'"
            },
            33: {
                "b_face": [0,0,1,1,1,1,0,0,1],
                "b_oll": [1,1,0,0,0,0,0,1,1,0,0,0],
                "solution": "R U R' U' R' F R F'"
            },
            45: {
                "b_face": [0,0,1,1,1,1,0,0,1],
                "b_oll": [0,1,0,0,0,0,0,1,0,1,0,1],
                "solution": "F R U R' U' F'"
            },
            44: {
                "b_face": [0,0,1,0,1,1,0,1,1],
                "b_oll": [0,0,0,1,1,1,0,1,0,0,0,0],
                "solution": "f R U R' U' f'"
            },
            43: {
                "b_face": [1,0,0,1,1,0,1,1,0],
                "b_oll": [0,0,0,1,1,1,0,1,0,0,0,0],
                "solution": "f' L' U' L U f"
            },
            32: {
                "b_face": [0,0,1,0,1,1,0,1,1],
                "b_oll": [1,0,0,0,0,0,0,1,1,0,1,0],
                "solution": "R d L' d' R' U l U l'"
            },
            31: {
                "b_face": [0,1,1,0,1,1,0,0,1],
                "b_oll": [1,1,0,0,0,0,0,0,1,0,1,0],
                "solution": "R' U' F U R U' R' F' R"
            },
            38: {
                "b_face": [0,1,1,1,1,0,1,0,0],
                "b_oll": [0,1,0,1,1,0,0,0,1,0,0,0],
                "solution": "R U R' U R U' R' U' R' F R F'"
            },
            36: {
                "b_face": [1,1,0,0,1,1,0,0,1],
                "b_oll": [0,1,0,0,0,0,1,0,0,0,1,1],
                "solution": "L' U' L U' L' U L U L F' L' F"
            },
            54: {
                "b_face": [0,1,0,0,1,1,0,0,0],
                "b_oll": [0,1,0,1,0,1,0,0,0,1,1,1],
                "solution": "r U R' U R U' R' U R U2' r'"
            },
            53: {
                "b_face": [0,0,0,0,1,1,0,1,0],
                "b_oll": [0,0,0,1,0,1,0,1,0,1,1,1],
                "solution": "r' U' R U' R' U R U' R' U2 r"
            },
            50: {
                "b_face": [0,0,0,0,1,1,0,1,0],
                "b_oll": [0,0,1,0,0,0,1,1,0,1,1,1],
                "solution": "R B' R B R2' U2 F R' F' R"
            },
            49: {
                "b_face": [0,1,0,0,1,1,0,0,0],
                "b_oll": [0,1,1,0,0,0,1,0,0,1,1,1],
                "solution": "R' F R' F' R2 U2 y R' F R F'"
            },
            48: {
                "b_face": [0,1,0,1,1,0,0,0,0],
                "b_oll": [0,1,1,0,1,0,1,0,0,1,0,1],
                "solution": "F R U R' U' R U R' U' F'"
            },
            47: {
                "b_face": [0,1,0,0,1,1,0,0,0],
                "b_oll": [1,1,0,1,0,1,0,0,1,0,1,0],
                "solution": "F' L' U' L U L' U' L U F"
            },
            39: {
                "b_face": [0,0,1,1,1,1,1,0,0],
                "b_oll": [0,1,0,1,0,0,0,1,1,0,0,0],
                "solution": "L F' L' U' L U F U' L'"
            },
            40: {
                "b_face": [1,0,0,1,1,1,0,0,1],
                "b_oll": [0,1,0,0,0,0,1,1,0,0,0,1],
                "solution": "R' F R U R' U' F' U R"
            },
            34: {
                "b_face": [0,0,0,1,1,1,1,0,1],
                "b_oll": [0,1,0,0,0,1,0,1,0,1,0,0],
                "solution": "R U R2' U' R' F R U R U' F'"
            },
            46: {
                "b_face": [1,1,0,0,1,0,1,1,0],
                "b_oll": [0,0,0,1,1,1,0,0,0,0,1,0],
                "solution": "R' U' R' F R F' U R"
            },
            5: {
                "b_face": [0,0,0,0,1,1,0,1,1],
                "b_oll": [0,0,0,0,0,1,0,1,1,0,1,1],
                "solution": "r' U2 R U R' U r"
            },
            6: {
                "b_face": [0,1,1,0,1,1,0,0,0],
                "b_oll": [1,1,0,1,0,0,0,0,0,1,1,0],
                "solution": "r U2 R' U' R U' r'"
            },
            7: {
                "b_face": [0,1,0,1,1,0,1,0,0],
                "b_oll": [0,1,1,0,1,1,0,0,1,0,0,0],
                "solution": "r U R' U R U2 r'"
            },
            12: {
                "b_face": [0,0,0,1,1,0,0,1,1],
                "b_oll": [1,0,0,0,1,0,1,1,0,1,0,0],
                "solution": "M U2 R' U' R U' R' U2 R U M'"
            },
            8: {
                "b_face": [1,0,0,1,1,0,0,1,0],
                "b_oll": [1,0,0,1,1,0,1,1,0,0,0,0],
                "solution": "r' U' R U' R' U2 r"
            },
            11: {
                "b_face": [0,0,0,0,1,1,1,1,0],
                "b_oll": [0,0,1,0,0,1,0,1,1,0,1,0],
                "solution": "r' R2 U R' U R U2 R' U M'"
            },
            37: {
                "b_face": [1,1,0,1,1,0,0,0,1],
                "b_oll": [1,1,0,0,1,1,0,0,0,0,0,0],
                "solution": "F R U' R' U' R U R' F'"
            },
            35: {
                "b_face": [1,0,0,0,1,1,0,1,1],
                "b_oll": [1,0,0,0,0,1,0,1,0,0,1,0],
                "solution": "R U2 R2 F R F' R U2 R'"
            },
            10: {
                "b_face": [0,0,1,1,1,0,0,1,0],
                "b_oll": [0,0,1,0,1,0,0,1,1,0,0,1],
                "solution": "R U R' U R' F R F' R U2 R'"
            },
            9: {
                "b_face": [0,1,0,1,1,0,0,0,1],
                "b_oll": [1,1,0,0,1,0,1,0,0,1,0,0],
                "solution": "R U R' U' R' F R2 U R' U' F'"
            },
            51: {
                "b_face": [0,0,0,1,1,1,0,0,0],
                "b_oll": [0,1,1,0,0,0,1,1,0,1,0,1],
                "solution": "f R U R' U' R U R' U' f'"
            },
            52: {
                "b_face": [0,1,0,0,1,0,0,1,0],
                "b_oll": [1,0,0,1,1,1,0,0,1,0,1,0],
                "solution": "R U R' U R d' R U' R' F'"
            },
            56: {
                "b_face": [0,1,0,0,1,0,0,1,0],
                "b_oll": [1,0,1,0,1,0,1,0,1,0,1,0],
                "solution": "f R U R' U' f' F R U R' U' R U R' U' F'"
            },
            55: {
                "b_face": [0,1,0,0,1,0,0,1,0],
                "b_oll": [0,0,0,1,1,1,0,0,0,1,1,1],
                "solution": "R U2 R2 U' R U' R' U2 F R F'"
            },
            13: {
                "b_face": [0,0,0,1,1,1,1,0,0],
                "b_oll": [0,1,1,0,0,1,0,1,1,0,0,0],
                "solution": "r U' r' U' r U r' y' R' U R"
            },
            16: {
                "b_face": [0,0,1,1,1,1,0,0,0],
                "b_oll": [1,1,0,1,0,0,0,1,0,1,0,0],
                "solution": "r U r' R U R' U' r U' r'"
            },
            14: {
                "b_face": [0,0,0,1,1,1,0,0,1],
                "b_oll": [1,1,0,0,0,0,1,1,0,1,0,0],
                "solution": "R' F R U R' F' R y' R U' R'"
            },
            15: {
                "b_face": [1,0,0,1,1,1,0,0,0],
                "b_oll": [0,1,1,0,0,1,0,1,0,0,0,1],
                "solution": "l' U' l L' U' L U l' U l"
            },
            41: {
                "b_face": [1,0,1,0,1,1,0,1,0],
                "b_oll": [1,0,1,0,0,0,0,1,0,0,1,0],
                "solution": "R U' R' U2 R U y R U' R' U' F'"
            },
            30: {
                "b_face": [1,0,1,0,1,1,0,1,0],
                "b_oll": [0,0,0,1,0,0,0,1,0,0,1,1],
                "solution": "R2' U R' B' R U' R2' U l U l'"
            },
            42: {
                "b_face": [1,0,1,1,1,0,0,1,0],
                "b_oll": [1,0,1,0,1,0,0,1,0,0,0,0],
                "solution": "L' U L U2' L' U' y' L' U L U F"
            },
            29: {
                "b_face": [1,0,1,1,1,0,0,1,0],
                "b_oll": [0,0,0,1,1,0,0,1,0,0,0,1],
                "solution": "L2 U' L B L' U L2 U' r' U' r"
            }
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
    def check_oll(cls, cube):
        face = np.all(cube.cube[0] == cube.cube[0][1][1])
        return face

    @classmethod
    def check_pll(cls, cube):
        front_edges = np.all(cube.cube[[1],[0]] == cube.cube[1][1][1])
        right_edges = np.all(cube.cube[[2],[0]] == cube.cube[2][1][1])
        back_edges = np.all(cube.cube[[3],[0]] == cube.cube[3][1][1])
        left_edges = np.all(cube.cube[[4],[0]] == cube.cube[4][1][1])
        return cls.check_oll(cube) and front_edges and right_edges and back_edges and left_edges

    @classmethod
    def check_solved(cls, cube):
        return cls.check_bottom(cube) and cls.check_middle(cube) and cls.check_pll(cube)

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
    def solve_oll(cls, cube):
        moves = []
        top_color = cube.cube[0][1][1]
        correct_edges = []
        correct_corners = []
        binary_top_face = []
        for k, v in enumerate(cube.cube[0].flatten()):
            if v == top_color:
                binary_top_face.append(1)
                if k in [0,2,6,8]:
                    correct_corners.append(k)
                elif k in [1,3,5,7]:
                    correct_edges.append(k)
            else:
                binary_top_face.append(0)
        outer_last_layer = cube.cube[[1,2,3,4],[0]].flatten()
        #binary_outer_last_layer = map(lambda x: x == top_color, outer_last_layer)
        binary_outer_last_layer = map(lambda x: 1 if x == top_color else 0, outer_last_layer)
        for alg in cls.algorithms["OLL"]:
            if np.array_equal(binary_top_face, cls.algorithms["OLL"][alg]["b_face"]) and \
                np.array_equal(binary_outer_last_layer, cls.algorithms["OLL"][alg]["b_oll"]):
                moves.extend(cls.algorithms["OLL"][alg]["solution"].split(" "))
                cube.execute_list(moves)
                return moves
            for i in range(1,4):
                if np.array_equal(np.rot90(np.array(binary_top_face).reshape(3,3),i).flatten(), cls.algorithms["OLL"][alg]["b_face"]) and \
                    np.array_equal(np.roll(binary_outer_last_layer, i*3), cls.algorithms["OLL"][alg]["b_oll"]):
                    if i == 1:
                        moves.append("U'")
                    elif i == 2:
                        moves.append("U2")
                    else:
                        moves.append("U")
                    moves.extend(cls.algorithms["OLL"][alg]["solution"].split(" "))
                    cube.execute_list(moves)
                    return moves
        raise Exception("Attempting to solve an unsolvable cube on OLL layer")

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
            orient_move = cls.orient_U(complete_edges[0], 3)
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
                orient_move = cls.orient_U(right_blocks[0], 4)
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
                orient_move = cls.orient_U(headlights[0], 4)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["T"].split(" "))
        elif scrambled_edges == 4:
            # E perm
            if cube.cube[4][0][0] == cube.cube[2][0][2]:
                moves.append("U")
            moves.extend(cls.algorithms["PLL"]["E"].split(" "))
        elif len(complete_edges) == 1 and len(left_blocks) == 3:
            # Ja perm
            orient_move = cls.orient_U(complete_edges[0], 1)
            if orient_move is not None:
                moves.append(orient_move)
            moves.extend(cls.algorithms["PLL"]["Ja"].split(" "))
        elif len(complete_edges) == 1 and len(right_blocks) == 3:
            # Jb perm
            orient_move = cls.orient_U(complete_edges[0], 4)
            if orient_move is not None:
                moves.append(orient_move)
            moves.extend(cls.algorithms["PLL"]["Jb"].split(" "))
        elif len(headlights) == 1 and len(left_blocks) == 1 and scrambled_edges == 2:
            if (left_blocks[0] == (headlights[0] + 1) % 4):
                # Ra perm
                orient_move = cls.orient_U(left_blocks[0], 1)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Ra"].split(" "))
            elif (left_blocks[0] == (headlights[0] + 2) % 4):
                # Gd perm
                orient_move = cls.orient_U(left_blocks[0], 2)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Gd"].split(" "))
            else:
                # Gc perm
                orient_move = cls.orient_U(left_blocks[0], 3)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Gc"].split(" "))
        elif len(headlights) == 1 and len(right_blocks) == 1 and scrambled_edges == 2:
            if ((right_blocks[0] + 1) % 4 == headlights[0]):
                # Rb perm
                orient_move = cls.orient_U(right_blocks[0], 1)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Rb"].split(" "))
            elif ((right_blocks[0] + 2) % 4 == headlights[0]):
                # Gb perm
                orient_move = cls.orient_U(right_blocks[0], 2)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Gb"].split(" "))
            else:
                # Ga perm
                orient_move = cls.orient_U(right_blocks[0], 0)
                if orient_move is not None:
                    moves.append(orient_move)
                moves.extend(cls.algorithms["PLL"]["Ga"].split(" "))
        elif len(complete_edges) == 1 and scrambled_edges == 3:
            # F perm
            orient_move = cls.orient_U(complete_edges[0], 4)
            if orient_move is not None:
                moves.append(orient_move)
            moves.extend(cls.algorithms["PLL"]["F"].split(" "))
        elif len(left_blocks) == 1 and len(right_blocks) == 1 and scrambled_edges == 2:
            orient_move = cls.orient_U(complete_edges[0], 1)
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
            raise Exception("Attempting to solve an unsolvable cube on PLL layer")

        if len(moves) > 0:
            cube.execute_list(moves)
            moves.extend(cls.solve_pll(cube))

        return moves

    @classmethod
    def solve(cls, cube):
        solution = []
        if not cls.check_cross(cube):
            # solve cross
            pass
        if not cls.check_bottom(cube):
            # solve f2l
            pass
        if not cls.check_middle(cube):
            # solve f2l
            pass
        if not cls.check_oll(cube):
            solution.extend(cls.solve_oll(cube))
        if not cls.check_pll(cube):
            solution.extend(cls.solve_pll(cube))
        return solution

