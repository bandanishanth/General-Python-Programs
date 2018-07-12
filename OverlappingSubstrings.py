'''
Counts the number of times a given substring occours in a String even if it overlaps.

Example:
String="CDCDC"
Substring="CDC"

The Substring occours 2 times in the given string.
'''

def count_substring(string,substring):
    if len(substring)==1:#If length of substring is 1, just simple count.
        counter=0 # A counter to note the number of times a substring occours.
        for i in string:
            if i==substring:
                counter+=1
        return counter
    count=0 #A Counter..
    index=0 #Index where the substring is found.
    position=0 #Position in the main string until where we have Traversed..
    while(position<len(string)): #While the position dosen't cross string length.
        index=string[position:].find(substring)#Search from slice string[position:] i.e current position to end.
        if index==-1:#If not found. Simplu return the value of counter.
            return count
        elif index==len(string[position:])-1:#Index is at the last position..i.e substring found at last position in string.
            count+=1 #Increment counter 1 time as it HAS occoured even though at the end.
            return count
        else:        # Otherwise
            count=count+1
            position+=index+len(substring)-1 #Increase position by index and then (len(substring)-1). In "CDC",again search from 'C'.
    
    #print(count)
    return count#Finally return counter.