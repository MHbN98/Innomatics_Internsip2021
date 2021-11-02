th = 'M{0,3}'
hu = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
di = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (th,hu,ten,di)	# Do not delete 'r'.