'''
This Program takes a string as input and returns all the possible combinations of substrings as the output.
We go through each charachter i in the string.
Build pieces of that charachter from begginig to end with increasing size until we don;t breach the string size.
Example:
BANANA
First Pass:
B
BA
BAN
BANA
BANAN
BANANA

Second Pass:
A
AN
ANA
ANAN
ANANA

......AND SO ON.....
Keep a counter 'i' for each letter and for each i , itierate j from i+1 to end.
Put that slice in the list.
'''
def subsets_of_string(string):
	#Take a list..
	l=[]
	#--------------------------------------------------------------------------------------------------------------
	for i in range(len(string)): #Itiearate over every charachter.
		for j in range(i+1,len(string)+1): #We take len(string)+1 as in slice string[i:j] . The value of j will be one less.
			l.append(string[i:j]) #Append the string to the list.
	#--------------------------------------------------------------------------------------------------------------

	#The above block can also be written in one line.
	#l=[string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
	#--------------------------------------------------------------------------------------------------------------
	
	#To return all combinations
	return l
	#To return uniqe (Non repeating) just return a set.


