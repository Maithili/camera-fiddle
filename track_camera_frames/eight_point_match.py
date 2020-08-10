import numpy

def eight_point_match(points):
	matrix = get_flat_points_matrix(points)
	F_flat = extract_null_space(matrix)
	F = F_flat.reshape((3,3))
	u,s,vt = numpy.linalg.svd(F)
	print("F : ")
	pretty_print(F)
	print("Eigenvalues of F :",s)
	s[2] = 0
	s = numpy.diag(s)
	F_rank_reduced = numpy.dot(numpy.dot(u,s),vt)
	print("After rank reductin, F :")
	pretty_print(F_rank_reduced)
	return F_rank_reduced
	
def get_flat_points_matrix(points):
	matrix = numpy.ones((8, 9))

	for idx, (pt1, pt2) in enumerate(points):
		matrix[idx][0] = pt1[0]*pt2[0]
		matrix[idx][1] = pt1[1]*pt2[0]
		matrix[idx][2] = pt2[0]
		matrix[idx][3] = pt1[0]*pt2[1]
		matrix[idx][4] = pt1[1]*pt2[1]
		matrix[idx][5] = pt2[1]
		matrix[idx][6] = pt1[0]
		matrix[idx][7] = pt1[1]
	return matrix


def extract_null_space(matrix):
	# U.S.Vt = matrix 8x9
	# Vt = 9x9
	u, s, vt = numpy.linalg.svd(matrix, full_matrices=True)
	null_space = vt.T[:,-1]
	return null_space

def check_F(point_pair, F):
	p1 = numpy.ones((3,1))
	p1[0,0] = point_pair[0][0]
	p1[1,0] = point_pair[0][1]
	p2 = numpy.ones((3,1))
	p2[0,0] = point_pair[1][0]
	p2[1,0] = point_pair[1][1]
	print("This should be zero : ",numpy.dot(numpy.dot(p2.T, F),p1))

def pretty_print(A):
	print('\n'.join(['   '.join(['{:10}'.format(item) for item in row]) 
      for row in A]))