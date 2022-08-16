#Author: Dominic Portolese
from difflib import SequenceMatcher

"""
identicalSequenceFinder()

Arguments: two strings that each represent a chunk of a genome

Process: searches for the longest common substring shared between
         these strings
         
Output: returns a string representing the largest common substring
        shared between these strings
"""
def identicalSequenceFinder(input1, input2):
    toReturn = ""
    
    match = SequenceMatcher(None, input1, input2).find_longest_match()

    toReturn = (input1[match.a:match.a + match.size])  
    

    return toReturn



"""
genomeSplitter()

Arguments: genomeToSplit is a string of an entire genome
           start is an integer representing what chunk of genome to use
           
Process: uses start to find where to start cutting into the genome, then cuts
         out the next 100 chars of genome
         
Output: returns a string representing the 100 chars of genome that was cut out
        of the whole genome
"""
def genomeSplitter(genomeToSplit, start):
    toReturn = ""
    
    start = start*100
    end = start+100
    
    toReturn = genomeToSplit[start:end]
    
  
    return toReturn


"""
genomeSegmentAssigner()

Arguments: two strings each representing an entire genome
           intensity is an integer representing how many chunks of genome to make
           
Process: uses intensity to decide how many chunks of genome to make, then uses 
         genomeSplitter to split the genome into these chunks. These split chunks are
         then sent to identicalSequenceFinder to find the longest common sequence. 
         These longest common sequences are then compared against the existing longest
         sequence, and checked for Ns.
         
Output: A string representing the longest common sequence present among the number of
        chunks of genome scanned between both whole genomes (capped at 100)
"""
def genomeSegmentAssigner(genome1, genome2, intensity):
    longestString = ""
    temp = ""
    for x in range(intensity):
        temp = identicalSequenceFinder(genomeSplitter(genome1, x), genomeSplitter(genome2, x))
    #eliminating sequences with N to prevent erroneous matches
        if len(temp) > len(longestString) and temp.find("N") == -1:
           longestString = temp
        
    return longestString

#main----------------------------------------------------------------------
text_file = open(r"C:\Users\Dominic\Desktop\Genome1Orangutang.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome2Chimp.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome3Dog.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome4Rat.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome5Lion.txt", "r")

#text_file = open(r"C:\Users\Dominic\Desktop\Genome6Alligator.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome7Komodo.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome8Chameleon.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome9Python.txt", "r")
#text_file = open(r"C:\Users\Dominic\Desktop\Genome10SnappingTurtle.txt", "r")

input1 = text_file.read()
text_file.close()

#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome1Orangutang.txt", "r")
text_file2 = open(r"C:\Users\Dominic\Desktop\Genome2Chimp.txt", "r")
#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome3Dog.txt", "r")
#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome4Rat.txt", "r")
#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome5Lion.txt", "r")

#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome6Alligator.txt", "r")
#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome7Komodo.txt", "r")
#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome8Chameleon.txt", "r")
#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome9Python.txt", "r")
#text_file2 = open(r"C:\Users\Dominic\Desktop\Genome10SnappingTurtle.txt", "r")

input2 = text_file2.read()
text_file2.close()

"""
TO USE:
   1. replace commented out text_file strings with strings relevant to files on your computer
   2. change the third argument to represent how thoroughly you want to search each genome, each number
       equates to one 100 char chunk being searched, therefore 10000 equates to 2,000,000 chars being searched
   3. The length of the longest shared sequence found as well as the sequence itself will be output
   4. Should take <10 seconds
"""
answer = genomeSegmentAssigner(input1, input2, 10000)
print("Length: ", len(answer))
print("Answer: ", answer)
