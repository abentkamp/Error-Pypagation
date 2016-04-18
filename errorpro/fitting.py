from scipy.optimize import curve_fit
from sympy.utilities.lambdify import lambdify
import numpy as np

def fit(func, xdata, ydata, params, ydata_axes=0, weighted=None, absolute_sigma=False):
	""" fits function to data
	Args:
	- xdata: Quantity of x-axis data or list of quantities
	- ydata: Quantity of y-axis data
	- params: list of Quantity objects. parameters to be fitted.
    - ydata_axes: int or tuple of ints. Specifies which axes of the ydata to use
    			  for the fit. On other axes, fit will be repeated separately.
	- weighted: bool. If fit should be weighted by errors or not.
	- absolute_sigma: bool. If False, uses errors only to weight data points.
					  Overall magnitude of errors doesn't affect output errors.
					  If True, estimated output errors will be based on input
					  error magnitude.
	"""

	# create fit function
	args = list(xdata) + list(params)
	np_func = lambdify(tuple(args), func, "numpy")
	def fit_func(x, 

	# list starting values
	start_params = []
	for p in params:
		if p.value == None:
			start_params.append(np.float_(1))
		else:
			if isinstance(p.value,np.ndarray):
				raise ValueError("fit parameter '%s' is a data set." % p.name)
			else:
				start_params.append(p.value)

	# weight fit
	if weighted is True or weighted is None:
		yerrors = ydata.error
	else:
		yerrors = None

	if weighted is True and ydata.error is None:
		raise RuntimeError("can't perform weighted fit because error of '%s' is not set." % ydata.name)

	# make ydata_axes an array
	if isinstance(ydata_axes, int):
		ydata_axes = (ydata_axes,)
		
	if not len(ydata_axes) == len(xdata):
		raise ValueError("amount of xdata 1-dim. quantities must equal"\
						"the amount of used ydata axes.\n %s != %s"\
						 % (len(xdata),len(ydata_axes)))

    # number of dimensions to iterate
	dim_num = len(ydata.shape)-len(ydata_axes)

    # get new order of axes
	# first: find axes that are not used for fit, hence iterated
	iterated_axes = []
	for ax in reversed(range(len(ydata.shape))):
		if ax not in ydata_axes:
			iterated_axes = [ax] + iterated_axes
    # second: add all these axes in front
	ydata_axes = iterated_axes + list(ydata_axes)

    # get axes in right order
	yvalues = ydata.value.transpose(ydata_axes)
	if yerrors is not None:
		yerrors = ydata.error.transpose(ydata_axes)

	# variables to save the parameters
	params_opt = np.zeros([ydata.value.shape[ax_num] for ax_num in iterated_axes]
						  + [len(start_params)])
	params_err = params_opt.copy()

    # iterate over the first d axes
	for i in np.ndindex(yvalues.shape[:dim_num]):
		if yerrors is not None:
			err = yerrors[i]
			absolute = absolute_sigma
		else:
			err = None
			absolute = False
		# perform fit
		params_opt[i], params_covar = curve_fit (np_func,xdata.value, yvalues[i],
					sigma=err, p0=start_params, absolute_sigma=absolute)

		# calculate errors
		params_err[i] = np.sqrt(np.diag(params_covar))

	params_opt = np.rollaxis(params_opt,len(params_opt.shape)-1)
	params_err = np.rollaxis(params_err,len(params_err.shape)-1)
	return (params_opt,params_err)