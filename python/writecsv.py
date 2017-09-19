import sys
from os import listdir
from os.path import join,exists, isdir

def buildcsv(outputs):
	csv=open('errorscsv.csv','w')
	csv.write('DATASET, MEAN-T, STD-T, MIN-T, MAX-T, MEAN-R, STD-R, MIN-R, MAX-R, NUMMEASURES\n')

	for f in listdir(outputs):
		if isdir(join(outputs,f)):
			for r in listdir(join(outputs,f)):

				if exists(join(join(outputs,f),r+'/Errors/RE/T.errors')):
					file=open(join(join(outputs,f),r+'/Errors/RE/T.errors'),'r')
					first=True

					for line in file:
						words=line.split(', ')
						if first is True:
							first=False
						else:
							csv.write(f+', '+words[0]+', '+words[1]+', '+words[2]+', '+words[3])

					file.close()

				if exists(join(join(outputs,f),r+'/Errors/RE/R.errors')):
					file=open(join(join(outputs,f),r+'/Errors/RE/R.errors'),'r')
					first=True

					for line in file:
						if first is True:
							first=False
						else:
							csv.write(', '+line)

					file.close()

	csv.close()

if __name__ == '__main__':
	buildcsv(sys.argv[1])