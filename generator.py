import random
import numpy as np

def PossibleValueAtPosition(pz:[], row:int, col:int):
	r=row//3*3
	c=col//3*3
	return {1,2,3,4,5,6,7,8,9}.difference(set(pz[r:r+3,c:c+3].flat)).difference(set(pz[row,:])).difference(set(pz[:,col]))

def Solution_Count(pz:[], n:int, Nof_solution:int):
	if Nof_solution>1:
		return Nof_solution
	if n>=81:
		Nof_solution+=1
		return Nof_solution
	(row,col) = divmod(n,9)
	if pz[row][col]>0:
		Nof_solution = Solution_Count(pz, n+1, Nof_solution)
	else:
		l = PossibleValueAtPosition(pz, row,col)
		for v in l:
			pz[row][col] = v
			Nof_solution = Solution_Count(pz, n+1, Nof_solution)
			pz[row][col] = 0
	return Nof_solution	

def SudokuSolver(pz:[], n:int):
	if n==81:
		return True
	(row,col) = divmod(n,9)
	if pz[row][col]>0:
		if SudokuSolver(pz, n+1):
			return True
	else:
		l = list(PossibleValueAtPosition(pz, row,col))
		random.shuffle(l)
		for v in l:
			pz[row][col] = v
			if SudokuSolver(pz, n+1):
				return True
			pz[row][col] = 0
	return False

def DigHoles(pz:[], randomlist:[], n:int):
	if n>=81:
		return
	(row,col) = divmod(randomlist[n],9)
	if pz[row][col]>0:
		pz_check=pz.copy()
		pz_check[row][col]=0
		Nof_solution = Solution_Count(pz_check, 0, 0)
		if Nof_solution==1:
			pz[row][col]=0
			print(pz)
			print("{} zeros".format(sum(pz.flat==0)))
			print()
	DigHoles(pz, randomlist, n+1)

def main():
	puzzle = np.zeros((9,9), dtype=int)
	SudokuSolver(puzzle, 0)
	print(puzzle, "--------- Answer\n")
	randomlist = list(range(81))
	random.shuffle(randomlist)
	DigHoles(puzzle, randomlist, 0)

if __name__ == "__main__":
	main()


