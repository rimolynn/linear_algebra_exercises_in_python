# -*- coding: utf-8 -*-
# calculate determinant of a 2D matrix 

def det(mat, sign):
	w = len(mat)
	if w==1:
		return mat[0][0]*sign
	else:
		total = 0
		for i in range(w):
			if i % 2 == 0:
				mul = sign
			else:
				mul = -sign
			mat2 = np.delete(np.delete(mat,0,0),i,1)
			d = mat[0][i]*det(mat2,mul)
			total += d
			#print(d)
			#print(mat2)
		return total