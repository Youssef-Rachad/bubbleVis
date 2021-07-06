def copyArray(A, B, begin, end):
    for i in range(begin, end):
        B.append(A[i])

# This is the top-down approach
def mergeArray(A, B, begin, middle, end):
    i = begin
    j = middle

    # While there are elements in either left or right run
    for k in range(begin, end):
        #print("array A:", A)
        #print("array B:", B)
        # if left sub_array exists and is smaller than right sub_array
        if i < middle and (j >= end or A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

def split_mergeArray(B, begin, end, A):
    # Until we get 1 number arrays
    if end - begin <= 1:
        return
    print("array A:", A)
    print("array B:", B)
    print(f"begin: {begin}, end: {end}")
    # Define middle (rounding down)
    middle = (end + begin)//2
    # Keep dividing
    split_mergeArray(A, begin, middle, B)
    split_mergeArray(A, middle, end, B)
    # Put it back, in order
    mergeArray(B, A, begin, middle, end)


# Sorting whole array : n = len(A)
# Where A is array to sort and B is work array
def sort(A, B, n):
    copyArray(A, B, 0, n)
    split_mergeArray(B, 0, n, A)

#copyArray([], [], 0, 10)
A = [6.4,4.2,5.5,7,3,10,3,35,235,21,5,6,1,10,9,33,90]
B = []
sort(A, B, len(A))
print(A)
