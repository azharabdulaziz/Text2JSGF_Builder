# This Program is Automatic BNF Finite State Grammar
# The input is any Text file and the out put will be JSGF FSG in the form of Bakus-Nou Form (BNF)
# This style could be used in many Automatic speech Recognition (ASR) Application
# By: Azhar Sabah Abdulaziz 
#2015
########################## Get arg Function #######################################
import time
import sys, getopt

def get_arg(argv):
	inputfile = ''
	outputfile = ''
	try:
	  opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
	  print 'test.py -i <inputfile> -o <outputfile>'
	  sys.exit(2)
	for opt, arg in opts:
	  if opt == '-h':
		 print 'text2jsgf.py -i <inputfile> -o <outputfile>'
		 sys.exit()
	  elif opt in ("-i", "--ifile"):
		 inputfile = arg
	  elif opt in ("-o", "--ofile"):
		 outputfile = arg
	return(inputfile,outputfile)
##############################################################################################

############################## Main Function #################################################
# Call get_ar 
[infile,outfile] = get_arg(sys.argv[1:])
if (infile == ""):
	print("Error: There is no input file. Correct syntax is: python text2jsgff.py -i inputfile -o outputfile")
	exit(1)
if (outfile == ""):
	print("Error: There is no output file. Correct syntax is: python text2jsgff.py -i inputfile -o outputfile")
	exit(1)


print "This Program is Automatic BNF Finite State Grammar"
print "The input is any Text file and the out put will be JSGF FSG in the form of Bakus-Nou Form (BNF)"
print "This style could be used in many Automatic speech Recognition (ASR) Application"
print "By: Azhar Sabah Abdulaziz 2015"	
print "Input text file is:", infile
print "The JSGF grammar is stored in the same directory and named",outfile
t1 = time.time()
sen_size = []
with open(infile,'r') as f:
	lines = f.readlines()
	
	for line in lines:
		words = line.split()
		sen_size.append(len(words))	
		f.close
max_sen = max(sen_size)
name_list = []
f.close()

for i in range(0,max_sen):
	
	name = "a" + str(i)
	name_list.append(name)

for i in range(0,max_sen):
	name_list[i]= []



f = open(infile,'r')
lines = f.readlines()
for line in lines:
	words = line.split()
	j = 0
	for word in words:
		name_list[j].append(word)
		
		j = j+1
#print(max_sen)
##################################################################
# clean up 
# 1-Calculate Weights of each token
red_list = []
for i in range(0,max_sen):
	
	name = "r" + str(i)
	red_list.append(name)

for i in range(0,max_sen):
	red_list[i]= []
	
for i in range(0,max_sen):
	for element in name_list[i]:
		red_list[i].append(name_list[i].count(element))
		
################################## Test ##############################
#for i in range(0,len(red_list)):
#	for j in range(0,len(red_list[i])):
#		print(red_list[i][j])
#print(red_list[0][2])
##########################################################################

# 2- Remove redundancy and add weights and "|"
for i in range(0,max_sen):
	temp_list =[]
	j=0
	for element in name_list[i]:
		
		if element not in temp_list:
			
			temp_list.append("/")
			temp_list.append(str(red_list[i][j]))
			j=j+1
			temp_list.append("/ ")
			temp_list.append(element)
			temp_list.append("|")
			
		else:
			j=j+1
	name_list[i] = temp_list
# 3- Remove the final "|" from each list
for i in range(0,max_sen):
	name_list[i].pop()

t2 = time.time()
elapsed_t = t2-t1
print "The Elapsed Time", elapsed_t

# Writing the JSGF into output file

f2 = open(outfile,'w')
f2.write("#JSGF V1.0;" + "\n")
f2.write("/******************************" + "\n")
f2.write("* Grammar generated automatically" + "\n")
f2.write("* It is a Bakus-Nou Finite State Grammar which is known as BNF-FSG" + "\n")
f2.write("* By: Azhar Sabah Abdulaziz " + "\n")
f2.write("******************************/" + "\n" + "\n" + "\n")
f2.write("grammar my_JSGF;" + "\n")
f2.write("public <s> =")

ind = 0 

for i in range(ind,len(name_list)):

	f2.write("(")
	for a in name_list[ind]:
		f2.write(a)
	f2.write(")"+"\n")
	ind = ind +1

f2.write(";")

f2.close()

