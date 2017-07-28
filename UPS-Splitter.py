#isa to first LX|

#LX through next CD3|

#last CD3 to end

#-DONE- B307 == L305

#-DONE- SE01 == | count minus 5

#-DONE- Add all the L104 segments up

#L305/B307 == L104 count (add all up)

#GE01 = 1

def lxSplitter():
	with open('UPS-batch.txt', 'r+') as f:
		for line in f:
			LXsegments = line.split('LX')
		return LXsegments

def header(data):
	header = data[0]
	return header

def footer(data):
	footer = "LX" + data[-1]
	return footer


def lxFinder(data):
	m = 0
	LXlist = []

	#Looks for tracking number, N9*CN, then pulls out the containing LX segments
	while m < len(data):
		if '1ZV093480100055729' in data[m]:
			LXlist.append('LX' + data[m])
		elif '1Z4573160140032524' in data[m]:
			LXlist.append('LX' + data[m])
		else:
			pass

		m+=1

	return LXlist

def segmentsplitter(data):
	segment = data.split('|')

	return segment

def elementsplitter(segment):
	#Split segments by elements, return them in a list
	splitdata = []

	for letter in segment:
		splitdata.append(letter.split('~'))
	return splitdata 

def segmentcounter(data):
	#Counts segments and then replaces SE01 with new value
	for element in data:
		if element[0] == 'SE':
			element[1] = len(data)-5
			print 'Changing SE01 to segment total: ' + str(element[1])
			return data

def b3l3Checker(data):
	#Checks to make sure B307 and L305 are the same
	B307 = data[3][7]
	L305 = data[-5][5]

	if B307 == L305:
		print "B307 and L305 = " + data[3][7]

	else:
		print "B307 and L305 don't match"

	return B307
	return L305


def totalSum(data):
	#Totals all L104 segments and then changes B307 and L305 to that value
	L1segment = []

	for segment in data:
		if segment[0] == 'L1':
				L1segment.append(int(segment[4]))
	L104 = sum(L1segment)

	data[3][7] = L104
	data[-5][5] = L104
	
	print data[3]
	print data[-5]

	return data

def geChange(data):
	#Change GE01 to 1
	for element in data:
		#print element[0]
		if element[0] == 'GE':
			element[1] = 1
			print 'Changing GE01 to: ' + str(element[1])
			return data

def headerSegment(data):
	#Pull ISA to first, but not including LX segment
	header = data[:13:]
	#print 'Header is\n' + str(header)
	return header

def footerSegment(data):
	#Pulls last CD3 segment to the end
	footer = data[-9:]
	#print 'Footer is\n' + str(footer)
	return footer

def fileWriter(data):

	SegmentDelimiter = '|'
	ElementDelimiter = '~'

	outputpath = "C:/Users/bsfelde/Desktop/"
	filename = 'UPS-redrop.txt'

	with open(outputpath + filename, "w") as text_file:

		for segment in data:
			for element in segment[:-1]:
				text_file.write(str(element)+str(ElementDelimiter))
				#writes tilde per element, except the last one
			text_file.write(str(segment[-1]))
			#appends last index to each segment
			if segment[0] == 'IEA':
				pass
			else:	
				text_file.write(SegmentDelimiter)
				#writes in | after each segment

		

	#-------------------------------------


def main():

	print '\n\n'

	segments = lxSplitter()

	t = header(segments)

	z = footer(segments)

	y = lxFinder(segments)
	x = ''.join(y)

	new_file = t + x + z
	print 'Pulling invoices with erred tracking numbers...'

	print '\n\n'

	print new_file

	print '\n\n'

	segments = segmentsplitter(new_file)

	dater = elementsplitter(segments)
	
	headerSegment(dater)

	footerSegment(dater)
	
	secount = segmentcounter(dater)

	print '\n\n'

	geChange(dater)

	#print secount

	print '\n\n'

	print 'Checking if B307 and L305 match...'

	b3l3Checker(dater)

	print '\n\n'

	#L1 = 
	#x = TotalSum(dater)
	print 'Changing B307 and L307 to L104 total'
	print '\n'

	totalSum(dater)
	#print x

	print '\n\n'

	#print dater
	print 'Writing new file, UPS-redrop.txt, to Desktop..'

	fileWriter(dater)

	print '\n\n'

if __name__ == '__main__':
     main()
