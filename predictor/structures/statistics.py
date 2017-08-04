''' Stats
Auxiliary class that stores mean and standard deviation of a generic metric.
*Could* turn out to be a duplicate of RunStats, but for now I'm going to keep them
separate as they represent different things (RunStats also has min, max, numSamples).'''

class Stats():
	def __init__(self, mean, std):
		self._mean = mean
		self._std = std

	@property
	def mean(self):
		""" Returns the mean of the specified quantity across a series of runs. """
		return self._mean

	@property
	def std(self):
		""" Returns the standard deviation of the specified quantity across a series of runs. """
		return self._std

	def __repr__(self):
		return "Mean: "+str(self._mean)+"\n"+ \
		"Standard deviation: "+str(self._std)+"\n"

''' ErrorStats
Auxiliary class that stores the metricEvaluator statistics of the error of a series of runs. 
This is the main class that represents the performances of an actual dataset when evaluated with
the metricEvaluator; each of the three measures it contains (mean and standard deviation of the
error, and number of samples used to compute it) has two further attributes, mean and standard
deviation, provided by the Stats class and meant to express its variability across several runs.'''

class ErrorStats():
	def __init__(self, mean, std, numSamples):
		self._mean = mean
		self._std = std
		self._numSamples = numSamples

	@property
	def mean(self):
		""" Returns the stats (mean and standard deviation) of the mean of the error across several runs. """
		return self._mean

	@property
	def std(self):
		""" Returns the stats (mean and standard deviation) of the standard deviation of the error across several runs."""
		return self._std

	@property
	def numSamples(self):
		""" Returns the stats (mean and standard deviation) of the number of samples that were extracted from the population for the analysis across several runs. """
		return self._numSamples

	def __repr__(self):
		return "Mean and standard deviation of the error mean: "+"\n"+ \
		str(self._mean)+ \
		"Mean and standard deviation of the error standard deviation: "+"\n"+ \
		str(self._std)+ \
		"Mean and standard deviation of the number of samples: "+"\n"+\
		str(self._numSamples)+"\n"

''' PerfStats
Auxiliary class that acts as a container for the translational and rotational error statistics
over a series of runs.'''

class PerfStats():
	def __init__(self, tError, rError, totalTime=None, totalLength=None):
		self._transError = tError
		self._rotError = rError
		self._totalTime = totalTime
		self._totalLength = totalLength

	@property
	def transError(self):
		""" Returns the stats of the transational error across several runs. """
		return self._transError

	@property
	def rotError(self):
		""" Returns the stats of the rotational error error across several runs."""
		return self._rotError

	@property
	def totalTime(self):
		""" Returns the stats (mean and standard deviation) of the total time that was required to explore this environment. """
		return self._totalTime

	@property
	def totalLength(self):
		""" Return the stats (mean and standard deviation) of the total length that was explored by the robot. """
		return self._totalLength

	def __repr__(self):
		return "Transational error: "+"\n"+\
		str(self._transError)+ \
		"Rotational error: "+"\n"+\
		str(self._rotError)

''' RunStats
Auxiliary class that stores the metricEvaluator statistics over the error of a run. '''

class RunStats():
	def __init__(self, mean, std, minErr, maxErr, numSamples):
		self._mean = mean
		self._std = std
		self._min = minErr
		self._max = maxErr
		self._numSamples = numSamples

	@property
	def mean(self):
		""" Returns the mean of the observations. """
		return self._mean

	@property
	def std(self):
		""" Returns the standard deviation of the observations. """
		return self._std

	@property
	def min(self):
		""" Returns the minimum of the observations. """
		return self._min

	@property
	def max(self):
		""" Returns the maximum of the observations. """
		return self._max

	@property
	def numSamples(self):
		""" Returns the number of samples that were extracted from the population for the analysis. """
		return self._numSamples

	def __repr__(self):
		return "Mean: "+str(self._mean)+"\n"+ \
		"Standard deviation: "+str(self._std)+"\n"+ \
		"Min: "+str(self._min)+"\n"+ \
		"Max: "+str(self._max)+"\n"+ \
		"Number of samples: "+str(self._numSamples)+"\n"