import sys
import os

file = os.path.basename(sys.argv[0])
sys.argv[0] = file
print "\nName of file invoked: ",file
print "\nNumber of arguments: " ,len(sys.argv)
print "\nThe arguments are -- " ,str(sys.argv)
