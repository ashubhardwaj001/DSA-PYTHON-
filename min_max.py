def min(A):
    min = A[0]
    for num in A:
        if num < min:
            min = num

    return min


def max(A):
    max = A[0]
    for num in A:
        if num > max:
            max = num

    return max

if __name__ == "__main__":

    A = [1,2,3,4,5,6]
    N = len(A)

    print("max = ", max(A))
    print("min = ", min(A))
