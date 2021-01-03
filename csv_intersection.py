import csv

# define as a function to make it testable
def get_csv_intersection(filename1, filename2):
    
    # ensure we can open both csv files before continuing 
    with open(filename1) as file1:
        with open(filename2) as file2:

            # define an array of 2 readers, one for each csv
            readers = [csv.reader(file1, delimiter=","), csv.reader(file2, delimiter=",")]
            
            # define an array of 2 python sets, one for each csv
            sets = [set(), set()]

            # index to track which reader/csv we are using
            index = 0

            # loop once for each reader in the array of readers 
            for reader in readers:
                # set to add data to depends on which csv we are reading
                currentSet = sets[index]
                # loop through every row in the csv file
                for row in reader:
                    # if the row isn't blank
                    if row:
                        # loop through every cell in the row
                        for cell in row:
                            # add the data from the cell to the currentSet
                            currentSet.add(cell)
                # increment the index so we use the correct set for the next reader we loop through
                index += 1
            
            # sort and return the intersection of the two sets
            return sorted(sets[0].intersection(sets[1]))
