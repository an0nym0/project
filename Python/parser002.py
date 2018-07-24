# for Tushakov, Timur
# 18/07/2018
#



import re

def main():
	in_f = open('E:/Projects/parse_emails_and_other_stuff/export5/export5.csv',"r")
	out_f = open('E:/Projects/parse_emails_and_other_stuff/export5/export6.csv',"w")
	i = 0

	for l in in_f.readlines():
		
		string = l.split(";") 
#		print string  ### TODO delete debug

		i = i+1
		string[10] = string[10][:-1]
#		raw_input("Press Enter to continue...")  ### TODO delete debug
		if i == 1 :
			out_f.write(";".join(string)+"\n")
			continue


		if not (re.match(r'\A[A-Z0-9-]{36}\Z', string[0])):
			print "\nDied in string " + str(i) + " arg 1: \n" + l
			exit(1)
		elif not (re.match(r'\A[ ,A-Za-z-()]*\Z', string[4])):
			print "\nDied in string " + str(i) + " arg 5: " + string[4] +"\n" + l
			exit(1)			
#		elif not re.search('[A-Z]|\d|-{22}', string[10] ):
#			print "\nDied in string " + str(i) + " arg 10: \n" + l
#			exit(1)
		else: 
			out_f.write(";".join(string)+"\n")
						


if __name__ == "__main__":
	main()