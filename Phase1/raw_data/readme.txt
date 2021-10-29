param range:
  N = {500,1000}:
  w = np.round(np.arange(1.0,2,0.025),3)
	== 1.000 1.025 1.050 1.075 1.100 ... 1.975

  N = 4000:
  w = np.round(np.arange(1.0,2+0.005,0.005),3)
 	== 1.000 1.005 1.010 1.015 1.020 ... 2.000

  N = 2000:
  w = np.round(np.arange(1.0,2.05,0.025),3)
	== 1.000 1.025 1.050 1.075 1.100 ... 2.025

file names:
   N = {0.5k , 1k , 4k}:
	'N'+str(N)+' j1.5 d1.5 g7.0 w'+str(w)+' base'+str(base)+' PA_Wid_pos.npy'
	'N'+str(N)+' j1.5 d1.5 g7.0 w'+str(w)+' base'+str(base)+' PA_Hei_pos.npy'
   N = 2000:
	'j1.5 d150 g7.0 w'+str(w)+' base'+str(base)+' PHei.npy'
	'j1.5 d150 g7.0 w'+str(w)+' base'+str(base)+' PWid.npy'

protocols:
	type: numpy.ndarray numpy.int32
	Dimension: 1D
	first element == minimum of distribution
	each element (except first one) shows how many times avalanche with that size/duration has been occurred.(need to be normalized)
	so if Hei[26] is equal to 1234 and Hei[0]=6 then it means 1234 avalanches happened with size of 19 (=24-1-6)
example:	
	data = np.load(path+'N'+str(N)+' j1.5 d1.5 g7.0 w'+str(w)+' base'+str(base)+' PA_Hei_pos.npy')
	x = np.arange(data[0],data[0]+len(data)-1)
	y = data[1:]

	plt.loglog()
	z = y!=0
	plt.scatter(x[z],y[z]/y.sum(),s=5)
