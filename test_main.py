from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(9, 3, 3) == 27
	assert simple_work_calc(16, 2, 4) == 28

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(8, 2, 2, lambda n: 1) == 15
	assert work_calc(4, 2, 2, lambda n: n**2) == 28
	assert work_calc(3, 2, 2, lambda n: n) == 5
	
	
	


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	a, b = 2,2
	ns = [1, 2, 4, 8, 16]

	work_fn1 = lambda n: work_calc(n,a,b, lambda n: n**0.5)
	work_fn2 = lambda n: work_calc(n,a,b, lambda n: n**1)

	res = compare_work(work_fn1, work_fn2, ns)

	print(res)

	
def test_compare_span():
	#TODO
	a, b= 2, 2
	ns = [1, 2, 4, 8, 16]

	span_fn1 = lambda n: span_calc(n, a, b, lambda n: 1)

	span_fn2 = lambda n: span_calc(n, a, b, lambda n: math.log(n, 2) if n>1 else 0)

	span_fn3 = lambda n: span_calc(n, a, b, lambda n: n)

	print("Comparing span functions")
	print(compare_span(span_fn1, span_fn2, ns))
	print(compare_span(span_fn2, span_fn3, ns))
 
