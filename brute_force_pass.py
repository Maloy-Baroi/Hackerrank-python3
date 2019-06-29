from itertools import combinations


def allcombos(str):
    # Get all permutations of string 'ABC'
    comList = combinations(str,len(str))

    # print all permutations
    for c in list(comList):
        print(''.join(c))

    # Driver program


if __name__ == "__main__":
    str = 'ABCDEFG'
    allcombos(str)