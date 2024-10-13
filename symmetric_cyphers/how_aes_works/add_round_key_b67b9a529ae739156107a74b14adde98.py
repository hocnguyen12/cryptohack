# Round keys challenge
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

from matrix_e1b463dddbee6d17959618cf370ff1a5 import matrix2bytes

def add_round_key(s, k):
    #return [s[i][j] ^ k[i][j] for i in range(0, 4) for j in range(0, 4)]
    return [list(s[i][j] ^ k[i][j] for j in range(0, 4)) for i in range(0, 4)]

if __name__ == '__main__':
    print(add_round_key(state, round_key))
    print(bytes(matrix2bytes(add_round_key(state, round_key))).decode('ascii'))