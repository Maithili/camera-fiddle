
def overwrite_parameters(input_params, default_params):
	for key in default_params.keys():
		if key in input_params.keys():
			default_params[key] = input_params[key]
	return default_params
	