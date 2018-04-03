import sys
sys.path.append('/Users/hari/Desktop/Cal/rise')
import jarvis

def test_plate():
	ex = jarvis.Experiment('plate_demo')

	ex.groundClient('git')

	ones = ex.literal([1, 2, 3], "ones")
	ones.forEach()

	tens = ex.literal([10, 100], "tens")
	tens.forEach()

	@jarvis.func
	def multiply(x, y):
	    z = x*y
	    print(z)
	    return z

	doMultiply = ex.action(multiply, [ones, tens])
	product = ex.artifact('product.txt', doMultiply)

	product.pull()
	product.plot()