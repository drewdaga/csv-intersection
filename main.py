import csv_intersection
import sys

# check if the correct number of command line parameters were provided and print usage if not
if (len(sys.argv) < 3): 
    print ('num filenames:', len(sys.argv))
    print ('arg list:', str(sys.argv))
    print ("Usage: python3 ",sys.argv[0], " file1.csv file2.csv")

# correct number of arguments were provided, call function and print results
else: 
    print ("printing csv intersections...")
    filename1, filename2 = sys.argv[1], sys.argv[2]
    print (csv_intersection.get_csv_intersection(filename1, filename2))