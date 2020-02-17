import numpy as np
import matplotlib.pyplot as plt

def xy(samples):
	Sn = np.sum(a=samples, axis=0)
	x = np.unique(Sn)
	y = []
	for i in range(x.shape[0]):
		y.append(np.sum(Sn==x[i]) / Sn.shape[0])

	return x, y

def uni_CLT(n, k):
	samples = np.random.choice(a=8, size=(n, k)) + 1
	return xy(samples)

def geo_CLT(n, k):
	samples = np.random.geometric(p=0.5, size=(n, k))
	return xy(samples)

def main():
	n_uni = [1, 2, 4, 32]
	n_geo = [1, 8, 16, 32]
	k = 100000 # If it's too slow, change it to 100000
	
	# uniform - CLT
	fig_uni = plt.figure(figsize=(12, 10))
	fig_uni.canvas.set_window_title('CLT - Uniform Distribution')
	fig_uni.suptitle('CLT - Uniform Distribution', fontsize=24)

	for i in range(len(n_uni)):
		x, y = uni_CLT(n_uni[i], k)
		uni_subplot = fig_uni.add_subplot(2,2,i+1)
		uni_subplot.scatter(x=x, y=y, s=10, label='n=%i' % n_uni[i])
		if i==0: uni_subplot.title.set_text('uniform distribution')
		else: uni_subplot.legend()

	# geometric - CLT
	fig_geo = plt.figure(figsize=(12, 10))
	fig_geo.canvas.set_window_title('CLT - Geometric Distribution')
	fig_geo.suptitle('CLT - Geometric Distribution', fontsize=24)

	for i in range(len(n_geo)):
		x, y = geo_CLT(n_geo[i], k)
		geo_subplot = fig_geo.add_subplot(2,2,i+1)
		geo_subplot.scatter(x=x, y=y, s=10, label='n=%i' % n_geo[i])
		if i==0: geo_subplot.title.set_text('geometric distribution')
		else: geo_subplot.legend()

	plt.show()

if __name__=='__main__':
	main()
