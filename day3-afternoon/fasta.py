#!/usr/bin/env python

"""Parse every FASTA record from a file and print"""

import sys
subset = open(sys.argv[1])

#class defines related data and methods
class FASTAReader(object):
    
    def __init__( self, input_file ):
        self.file = input_file
        self.last_ident = None
        
    def __iter__(self):
        return self
        
    def next(self):
        #if this is the first call/sequence
        if self.last_ident is None:

            line = subset.readline()

            #verify it is a header line

            #assert line.startswith(">")

            # or ident = line.split()[0].lstrip(">")
            #extract identifier
            ident = line.split()[0][1:]
        #if we have been called before/seen a sequence before
        else:
            ident = self.last_ident
            #empty list to put values in 
        sequences = []

        while True: 
            line = self.file.readline().rstrip("\r\n")
            if line.startswith( ">" ):
                self.last_ident = line.split()[0][1:]
                break 
            elif line == "":
                if sequences:
                    return ident, "".join(sequences)
                raise StopIteration 
            else: 
                sequences.append( line )
        return ident, "".join( sequences ) 

