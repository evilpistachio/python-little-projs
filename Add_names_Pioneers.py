#Caitlin Farley , HW7, program will add names to exisiting Pioneers file

def main():

    outfile = open('Pioneers.txt', 'a')
    outfile.write('Corrado Bohm,theorized the concept of structured programming\n')
    outfile.write('Kathleen Booth,invented the first assembly language\n')
    outfile.write('John McCarthy,invented LISP\n')
    outfile.write('Maurice Willkes,built the first practical stored program computer\n')
    outfile.close()

main()
    
