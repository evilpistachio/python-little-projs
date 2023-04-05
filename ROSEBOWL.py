#program outputs names of Rose Bowl winners who have won
#4 or more times from rose_bowl.txt file


def main():





       def openFile():
           with open("rose_bowl.txt", 'r') as p:
                     for line in p:
                         key = line.strip()
                         if key in teamWins:
                             teamWins = teamWins[key] + 1
                         else:
                             teamWins[key] = 1


        def giveWins(key, teamWins):
            for key in teamWins:
    
                if teamWins[key] >= 4
                    print(key,teamWins[key])


        teamWins = {}
        openFile()

        giveWins(key, teamWins)

main()
