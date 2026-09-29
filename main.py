from time import perf_counter
import random

def base_solution(files):
    computing_cost = 0
    while len(files) != 1:
        mins = [float('inf'), float('inf')]
        for n in files:
            if n < mins[0]:
                mins[1] = mins[0]
                mins[0] = n
            elif n < mins[1]:
                mins[1] = n
            # input(f"{n}, {mins[0]}, {mins[1]}")
        files.remove(mins[0])
        files.remove(mins[1])
        files.append(mins[0] + mins[1])
        computing_cost += mins[0] + mins[1]
    return computing_cost


def binary_check(insert, array):
    left = 0 # attempting to code a binary sort
    right = len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < insert:
            left = middle + 1
        else:
            right = middle
    if left == right:
         array.insert(left, insert)  #i hope this is correct
    return(array)


def heap_push(files, file_to_add): #takes O(n) = log base(2) of (n)
	files.append(file_to_add)
	index = len(files) -1

	while index > 0:
		parent = (index - 1) // 2
		if files[index] > files[parent]:
			break
		files[index], files[parent] = files[parent], files[index]
		index = parent


def heap_pop(files):
    result = files[0]
    files[0], files[-1] = files[-1], files[0]
    files.pop()

    index = 0
    while True:
        # input("running")
        child1 = index * 2 + 1
        child2 = index * 2 + 2
        smallest = index
        file_indexs = len(files) - 1

        if child1 <= file_indexs and files[child1] < files[smallest]:
            smallest = child1 

        if child2 <= file_indexs and files[child2] < files[smallest]:
            smallest = child2
        if smallest == index:
            #  input("breaking")
             break
        # input(f"Files: {files}\nIndex: {index}\nAt_I: {files[index]}\nsmallest: {smallest}\nAt_S: {files[smallest]}")
        files[index], files[smallest] = files[smallest], files[index]
        index = smallest
    return result


def compute_cost(files):
    heap_files = []
    computing_cost = 0
    for file in files:
        heap_push(heap_files, file)
    # input(heap_files)
    while len(heap_files) > 1:
        file1 = heap_pop(heap_files)
        file2 = heap_pop(heap_files)
        new_file = file1 + file2
        computing_cost += new_file
        # input(f"{heap_files}, {new_file}, {computing_cost}")
        heap_push(heap_files, new_file)
        # input(heap_files)
    return computing_cost


def list_generater(length, min = 1, max = 1000, seed = None):
    if seed is not None:
         random.seed = seed
    L = []
    for _ in range(length):
        L.append(random.randint(min, max))
    return L


def main():
    tests = [100, 200, 400, 800, 1600, 3200, 6400] #each are mupltipled by 2
    benchmark_times = []
    heap_times = []
    print("running tests...")
    for t in tests:
        t_difference = 0
        for _ in range(10):
             t_start = perf_counter()
             base_solution(list_generater(t))
             t_end = perf_counter()
             t_difference += t_end - t_start
        benchmark_times.append(t_difference/10)

        t_difference = 0
        for _ in range(10):
             t_start = perf_counter()
             compute_cost(list_generater(t))
             t_end = perf_counter()
             t_difference += t_end - t_start
        heap_times.append(t_difference/10)
        

    print(benchmark_times, heap_times)
    # THAT SHOULD BE THE DATA YOU NEED FOR YOUR GRAPHS
    

if __name__ == "__main__":
     main()