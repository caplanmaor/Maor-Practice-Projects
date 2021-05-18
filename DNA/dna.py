import csv
from sys import argv

def main():

    #check for correct number of arguments
    #.csv file in second argument
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    # Open files
    database_file = open("./" + argv[1])
    dna_file = open("./" + argv[2])

    # Get DNA types from top row of database csv
    database_header = csv.DictReader(database_file)
    dna_types = database_header.fieldnames[1:]

    # Copy DNA file
    dna = dna_file.read()
    dna_file.close()

    # Count how many times the DNA type shows up in the sequence
    dna_fingerprint = {}
    for str in dna_types:
        dna_fingerprint[str] = consec_repeats(str, dna);



    # print the matching persons name
    for row in database_header:
        if match(dna_types, dna_fingerprint, row):
            print(f"{row['name']}")
            database_file.close()
            return
    print("No Match")
    database_file.close()


# Determines the maximum numbef of consecutive repeates of a DNA type
def consec_repeats(str, dna):
        i = 0
        while str*(i+1) in dna:
            i += 1
        return i

# This function looks for the persons dna fingerprint in the dna types
def match(dna_types, dna_fingerprint, row):
    for str in dna_types:
        if dna_fingerprint[str] != int(row[str]):
            return False
    return True

main()