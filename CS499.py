import csv
import sys

#run script by executing command:
#python CS499.py csffile.csv


#import file
if len(sys.argv) < 2:
	print 'Please put the filename to import as a command line argument'
	exit()
else:
	filetoimport = sys.argv[1]
	newfile = "updated" + filetoimport

f = open(filetoimport,"rb")
reader = csv.reader(f)
rownum = 0
formatwrong = False

#create 2-D array for elements to be switched
w, h = 2, 18;
switch = [['N/A' for x in range(w)] for y in range(h)]

#default resets the switch matrix for each row
default = [['N/A' for x in range(w)] for y in range(h)]

#iterate through each row
for row in reader:
	#if row is zero, then it is MAKE,MODEL, etc
	if rownum == 0:
		for i in range(17):
			#get the index of where MAKE on the inputed file is 
			#equal to MAKE on the original template
			if (row[0] != "MAKE"):
				if(row[i] == "MAKE"):
					switch[0][0] = 0
					switch[0][1] = i
			elif (row[0] == "MAKE"):
                                switch[0][0] = 0
                                switch[0][1] = 0
				
			#repeate the same process for each header	
			if (row[1] != "MODEL"):
				if(row[i] == "MODEL"):
					switch[1][0] = 1
			 		switch[1][1] = i
                        elif (row[1] == "MODEL"):
                                switch[1][0] = 1
                                switch[1][1] = 1

                        if (row[2] != "MYR"):
                                if(row[i] == "MYR"):
                                        switch[2][0] = 2
                                        switch[2][1] = i
                        elif (row[2] == "MYR"):
                                switch[2][0] = 2
                                switch[2][1] = 2

                        if (row[3] != "OL"):
                                if(row[i] == "OL"):
                                        switch[3][0] = 3
                                        switch[3][1] = i
                        elif (row[3] == "OL"):
                                switch[3][0] = 3
                                switch[3][1] = 3

                        if (row[4] != "OW"):
                                if(row[i] == "OW"):
                                        switch[4][0] = 4
                                        switch[4][1] = i
                        elif (row[4] == "OW"):
                                switch[4][0] = 4
                                switch[4][1] = 4
			

                        if (row[5] != "OH"):
                                if(row[i] == "OH"):
                                        switch[5][0] = 5
                                        switch[5][1] = i
                        elif (row[5] == "OH"):
                                switch[5][0] = 5
                                switch[5][1] = 5

                        if (row[6] != "WB"):
                                if(row[i] == "WB"):
                                        switch[6][0] = 6
                                        switch[6][1] = i
                        elif (row[6] == "WB"):
                                switch[6][0] = 6
                                switch[6][1] = 6
			
                        if (row[7] != "CW"):
                                if(row[i] == "CW"):
                                        switch[7][0] = 7
                                        switch[7][1] = i
                        elif (row[7] == "CW"):
                                switch[7][0] = 7
                                switch[7][1] = 7

                        if (row[8] != "A1"):
                                if(row[i] == "A1"):
                                        switch[8][0] = 8
                                        switch[8][1] = i
                        elif (row[8] == "A1"):
                                switch[8][0] = 8
                                switch[8][1] = 8

                        if (row[9] != "B1"):
                                if(row[i] == "B1"):
                                        switch[9][0] = 9
                                        switch[9][1] = i
                        elif (row[9] == "B1"):
                                switch[9][0] = 9
                                switch[9][1] = 9

                        if (row[10] != "C1"):
                                if(row[i] == "C1"):
                                        switch[10][0] = 10
                                        switch[10][1] = i
                        elif (row[10] == "C1"):
                                switch[10][0] = 10
                                switch[10][1] = 10

                        if (row[11] != "D1"):
                                if(row[i] == "D1"):
                                        switch[11][0] = 11
                                        switch[11][1] = i
                        elif (row[11] == "D1"):
                                switch[11][0] = 11
                                switch[11][1] = 11

                        if (row[12] != "E1"):
                                if(row[i] == "E1"):
                                        switch[12][0] = 12
                                        switch[12][1] = i
                        elif (row[12] == "E1"):
                                switch[12][0] = 12
                                switch[12][1] = 12

                        if (row[13] != "F1"):
                                if(row[i] == "F1"):
                                        switch[13][0] = 13
                                        switch[13][1] = i
                        elif (row[13] == "F1"):
                                switch[13][0] = 13
                                switch[13][1] = 13	

                        if (row[14] != "G1"):
                                if(row[i] == "G1"):
                                        switch[14][0] = 14
                                        switch[14][1] = i
                        elif (row[14] == "G1"):
                                switch[14][0] = 14
                                switch[14][1] = 14

                        if (row[15] != "TWF"):
                                if(row[i] == "TWF"):
                                        switch[15][0] = 15
                                        switch[15][1] = i

                        elif (row[15] == "TWF"):
                                switch[15][0] = 15
                                switch[15][1] = 15

                        if (row[16] != "TWR"):
                                if(row[i] == "TWR"):
                                        switch[16][0] = 16
                                        switch[16][1] = i

                        elif (row[16] == "TWR"):
                                switch[16][0] = 16
                                switch[16][1] = 16

                        if (row[17] != "WDIST"):
                                if(row[i] == "WDIST"):
                                        switch[17][0] = 17
                                        switch[17][1] = i

                        elif (row[17] == "WDIST"):
                                switch[17][0] = 17
                                switch[17][1] = 17

		#initialize default
                default[0][0] = switch[0][0] 
                default[0][1] = switch[0][1]
                default[1][0] = switch[1][0]
                default[1][1] = switch[1][1]
                default[2][0] = switch[2][0]
                default[2][1] = switch[2][1]
                default[3][0] = switch[3][0]
                default[3][1] = switch[3][1]
                default[4][0] = switch[4][0]
                default[4][1] = switch[4][1]
                default[5][0] = switch[5][0]
                default[5][1] = switch[5][1]
                default[6][0] = switch[6][0]
                default[6][1] = switch[6][1]
                default[7][0] = switch[7][0]
                default[7][1] = switch[7][1]
                default[8][0] = switch[8][0]
                default[8][1] = switch[8][1]
                default[9][0] = switch[9][0]
                default[9][1] = switch[9][1]
                default[10][0] = switch[10][0]
                default[10][1] = switch[10][1]
                default[11][0] = switch[11][0]
                default[11][1] = switch[11][1]
                default[12][0] = switch[12][0]
                default[12][1] = switch[12][1]
                default[13][0] = switch[13][0]
                default[13][1] = switch[13][1]
                default[14][0] = switch[14][0]
                default[14][1] = switch[14][1]
                default[15][0] = switch[15][0]
                default[15][1] = switch[15][1]
                default[16][0] = switch[16][0]
                default[16][1] = switch[16][1]
                default[17][0] = switch[17][0]
                default[17][1] = switch[17][1]
 
	

		#make the switches to get the columns where they need to be
		for i in range(17):
			if (switch[i][0] == switch[i][1]) and (switch[i][0] != 'N/A'):
				row[i] = row[i]
			elif (switch[i][0] == 'N/A'):
				temp = row[i]
				row[i] = 'N/A'
				row[17]=temp
				switch[i][1] = 17;
			else:
				
				temp = row[i]
				row[i] = row[switch[i-1][1]]
				row[switch[i-1][1]]=temp
				switch[i][1]= switch[i-1][1]
				switch[i-1][1]=i	
   
	
		#this will be the last value, which will then create a trim column and write to a file
		else:
            
			row.append(18)
	                for n in range(18):
	                        if (n<16):
	                                row[18-n]=row[17-n]
	                        if (n==16):
	                                row[2] = "TRIM"
	                                row[1] = "MODEL"
					row[0] = "MAKE"
	                        

			row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17],row[18]]
			with open(newfile, 'a') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerow(row)

			csvFile.close()
				
	#for all rows other than the first
	else:
		
		#re initialize the switch matrix
                switch[0][0] = default[0][0]
                switch[0][1] = default[0][1]
                switch[1][0] = default[1][0]
                switch[1][1] = default[1][1]
                switch[2][0] = default[2][0]
                switch[2][1] = default[2][1]
                switch[3][0] = default[3][0]
                switch[3][1] = default[3][1]
                switch[4][0] = default[4][0]
                switch[4][1] = default[4][1]
                switch[5][0] = default[5][0]
                switch[5][1] = default[5][1]
                switch[6][0] = default[6][0]
                switch[6][1] = default[6][1]
                switch[7][0] = default[7][0]
                switch[7][1] = default[7][1]
                switch[8][0] = default[8][0]
                switch[8][1] = default[8][1]
                switch[9][0] = default[9][0]
                switch[9][1] = default[9][1]
                switch[10][0] = default[10][0]
                switch[10][1] = default[10][1]
                switch[11][0] = default[11][0]
                switch[11][1] = default[11][1]
                switch[12][0] = default[12][0]
                switch[12][1] = default[12][1]
                switch[13][0] = default[13][0]
                switch[13][1] = default[13][1]
                switch[14][0] = default[14][0]
                switch[14][1] = default[14][1]
                switch[15][0] = default[15][0]
                switch[15][1] = default[15][1]
                switch[16][0] = default[16][0]
                switch[16][1] = default[16][1]
                switch[17][0] = default[17][0]
                switch[17][1] = default[17][1]

		#switch values
                for i in range(17):
                        if (switch[i][0] == switch[i][1]) and (switch[i][0] != "N/A"):
                                row[i] = row[i]
                        elif (switch[i][0] == "N/A"):
                                temp = row[i]
                                row[i] = "N/A"
                                row[17]=temp
                                switch[i][1] = 17;
                        else:

                                temp = row[i]
                                row[i] = row[switch[i-1][1]]
                                row[switch[i-1][1]]=temp
                                switch[i][1]= switch[i-1][1]
                                switch[i-1][1]=i

		
		#parse the trim from model
		row[1] = row[1].split(' ',1)
		row.append(18)
		
		#add the trim
		for n in range(18):
			if (n<16):
				row[18-n]=row[17-n]
			if (n==16 and len(row[1])==2):
				row[2] = row[1][1]
				row[1] = row[1][0]
			if (n==16 and len(row[1])==1):
				row[2] = 'N/A'
				row[1] = row[1][0]
		
		#update year if not
		if (row[3] != "N/A"):
			if int(row[3]) > 65:
				row[3] = "19" + row[3]
			if int(row[3]) < 25:
				row[3] = "20" + row[3]
		
		row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]]
		with open(newfile, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row)

		csvFile.close()
	rownum += 1

f.close()
