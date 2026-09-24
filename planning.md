# Planning and analysis

**Problem Formulation**  
Suppose you are managing your company’s cloud storage and need to consolidate N files into a single file. You can only merge files two at a time. The computational cost of merging two files is the sum of their sizes.


Goal: Design a strategy to minimize the total cost of merging all files.


Input: List of size N containing file sizes.


Problem Formulation: Break down the project prompt. Clearly define the input parameters, expected outputs, and constraints.


**Baseline Solutions: Design a simple algorithm that solves the problem to serve as a reference point for performance comparisons.**
To establish a functional baseline, we can implement a naive pairing strategy. This approach simply iterates through the list of files and pairs two smallest files together, before readding it to the list.

```
Input - list of file size n
Def base_solution(input)
	Files = n
	Computing cost = 0
	While len(files) != 0:  # should run n times, as it decreases by len of 1 each time
		Mins = [inf, inf]
		For n in files: # runs n rimes, with each loop getting 1 smaller
			If n is lower then mins[0]:
				Mins[0] = n
			Elif n is lower then mins[1]:
				Mins[1] = n
		files.remove(mins[0])
		files.remove(mins[1])
		New_file = mins[0] + mins[1]
		files.append(new_file)
		Computing_cost += new_file
Return computing_cost
``` 


**Algorithmic Strategy: Select an appropriate design paradigm (e.g., divide-and-conquer, dynamic programming, greedy). Write detailed pseudocode for your proposed solution**
Our algorithemic greedy, and our method is to use a heap to sort the list before adding the 2 smallest files, and resorting the new file into the heap until the length of the heap is 1.

Input Parameters: an array of file sizes, (List[int])
Expected output - the computing cost of consolidating the files (int]). 
			
```
Def heap_push(files, file_to_add): #takes O(n) = log base(2) of (n)
	files.append(file_to_add)
	Index = len(file) -1

	While index greater than 0:
		Parent = (index - 1) // 2
		If files[index] > files[parent]
			Break
		files[index], files[parent] = files[parent], files[index]
		Index = parent

Def heap_pop(files): # should be O(n) = log base(2) of (n)
	Result = files[0]
	Files[0] = files[-1]
Index = 0
While True: # this is like a tree and the value is moving down. Thus the most it can move down is log base(2) of n
	Child1 = index*2 +1
	Child2 = index*2 +2
Smallest = index
If left is in bounds and is smaller than files[smallest]:
	Smallest = left
If right is in bounds and smaller than files[smallest]:
	Smallest = right
If smallest == index:
	Break

Files[index], files[smallest] = files[smallest], files[index]
Index = smallest
		Return result

Def main(files):
	Heap_files = []
for file in files: # runs n times
	heap_push(heap_files, file)
Computing_cost = 0
While len(heap_files) > 1: # should run n - 1 times
	New_file = heap_pop(Heap_files) + heap_pop(Heap_files)
	Computing_cost += new_file
	heap_push(heap_files, new_file)
Return computing_cost
```



Complexity Analysis: Establish the theoretical running time bounds ($O$, $\Omega$, or $\Theta$). Provide mathematical justification for your claims.


Our solution - 
$O$ - O(n log n) as the heap functions run log n times, and the while loop causing it to run n times, which mean n * log n, resulting in n log n
$Ω$ - The input of data does not change the logic of code blocks the code runs, therefor Big Ω is the same as Big O of O(n) = n * log (n)
$ϴ$ - since Big O and Big Ω are the same, Big ϴ is ϴ(n) = n*log(n)
Baseline solution -
$O$ - O(n^2) as it searches the whole list twice to add up the two minimums
$Ω$ - The input of data does not change the logic of code blocks the code runs, therefor Big Ω is the same as Big O of O(n) = n^2
$ϴ$ - since Big O and Big Ω are the same, Big ϴ is ϴ(n) = n^2


