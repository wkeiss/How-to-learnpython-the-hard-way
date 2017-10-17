provinces = {
	'Guangxi': 'Nanning',
	'Hainan': 'Haikou',
	'Anhui': 'Hefei',
	'Guangdong': 'Guangzhou'
}

provinces['Hunan'] = 'Changsha'

for provinces, cities in provinces.items():
	print "the cpital city of %s is %s." % (provinces, cities)