# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    heights = [0] * n

    for i in range(n):
        node_height = 0
        current = i
        while current != -1:
            if heights[current] != 0:
                node_height += heights[current]
                break
            node_height += 1
            current = parents[current]
        heights[i] = node_height
    return max(heights)


def main():
    mode = input()
    if "I" in mode:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in mode:
        filename = input()
        if 'a' in filename:
            return
        with open(f"test/{filename}") as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))

    print(compute_height(n, parents))
            


    # implement input form keyboard and from file
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
#print(numpy.array([1,2,3]))
