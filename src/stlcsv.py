


import csv
import os
import numpy
import matplotlib.pyplot as plotter
from operator import itemgetter, attrgetter


class stlcsv:

            # An array of the names of the fields. This is to make the
            # program userful for multiple purposes at a later date.
    fieldnames = [ "width", "height", "contig", "noncontig" ]

            # The file that data will be read and written to.
    filename = ""

            # The temporary storage of data that is read or will be 
            # written from.
    data = []

            # loopy specific variable.
    boardxy = [0,0]

            # prompt        : The input prompt string.
    prompt = "input $ "
            # prompt_count  : The number of lines that are read before
            # the title text is printed out.
    prompt_count = 8

            # delem, the character that separates width x height.
            # This is used only to make it easier to change so 
            # a person can enter it easier from the prompt.
    delem = "/"


#   Plot types for plot_data

    SCATTER_PLOT = 0b1

    plot_data = []

################
#
#       ErrorMessage(txt)  User function for outputting error codes.
#
################

    @staticmethod
    def ErrorMessage(txt):
        print("[  error ] ", txt)


################
#
#       write_data(header = False / True)
#       write .data to file. If header = True, then only
#           write the headers to the file.
#
################

    @classmethod
    def write_data(self, header = False):

        if self.filename == "":
            return(False)

        try:
            with open(self.filename, "a", newline="") as scf:
                if header == True:
                    writer = csv.DictWriter(scf, quoting = csv.QUOTE_NONNUMERIC, fieldnames=self.fieldnames)
                    writer.writeheader()
                else:
                    writer = csv.DictWriter(scf, quoting = csv.QUOTE_NONNUMERIC, fieldnames = self.fieldnames)
                    for d in self.data:
                        writer.writerow(d)
            self.data = []
            return(True)
        except:
            return(False)


################
#
#   read_data ( [[ "fieldA", d1, d2, d3... ], [ "fieldb", d1,...], [...] ] )
#
#               storedata = True      Store the data in the data variable.
#                           False     Don't store the data.
#               list_games = True     List the games in the file. All other 
#                                     arguments are ignored.
#
################

    @classmethod
    def read_data(self, fielddata, storedata = True, list_games = False):
       
        if self.filename == "":
            self.ErrorMessage("No file to read.")
            return(0)

        if (storedata == True) or (list_games == True):
            self.data = []

        x = 0
        try:
            with open(self.filename, "r", newline="") as scf:
                reader = csv.DictReader(scf, quoting=csv.QUOTE_NONNUMERIC)

                if list_games == True:
                    D = []

                    for row in reader:
                        c = False
                        for y in range(len(D)):
                            if (row[self.fieldnames[0]] == D[y][self.fieldnames[0]]) and (row[self.fieldnames[1]] == D[y][self.fieldnames[1]]):
                                c = True
                                break 
                        if c == False:
                            x+=1
                            D.append(row)

                    print(f"\nGame data stored in {self.filename}.")
                    for d in D:
                        print(f"{int(d[self.fieldnames[0]])}x{int(d[self.fieldnames[1]])}") 

                    return(x)       # Returns the number of games in file.

                if fielddata == []:
                    for row in reader:
                        if storedata == True:
                            self.data.append(row)
                        x+=1
                else: 
                    for row in reader:
                        for f in fielddata:
                            c = False
                            for n in f[1:]:
                                if row[f[0]] == n:
                                    c = True
                                    break
                            if c == False:
                                break
                        if c == True:
                            if storedata == True:
                                self.data.append(row)
                            x+=1
        except:
            self.ErrorMessage("Something went wrong.")

        return(x)
        

################
#
#       print_settings() print the current settings.
#
################
    
    @classmethod
    def print_settings(self):
        print("File name        : ", self.filename)
        print("Records stored   : ", len(self.data))
        print("Plot data        : ", len(self.plot_data))
        print("Board dimensions : ", f"{self.boardxy[0]}x{self.boardxy[1]}")
        print("Game delemiter   : ", self.delem)
        print(f"Prompt           : \"{self.prompt}\"")
        print(f"Prompt count     : {self.prompt_count}")
        for x in range(len(self.fieldnames)):
            if x == 0:
                print(f"Fields           :: {self.fieldnames[x]}")
            else:
                print(f"                 :: {self.fieldnames[x]}")

################
#
#       print_data()   Print the temporary data that will be printed out.
#
################

    @classmethod
    def print_data(self):
        print(f"Stored data count is {len(self.data)}.")
        for d in self.data:
            print(f"{int(d[self.fieldnames[0]])}x{int(d[self.fieldnames[1]])}   {int(d[self.fieldnames[2]])} :: {int(d[self.fieldnames[3]])}")


    @classmethod
    def plot(self, method = 0b1):

        if self.plot_data != []:
            C = numpy.array([ i for i in range(len(self.plot_data)) ])

            plotter.scatter(C, self.plot_data)

            plotter.show()
            return()

        D = [[],[],[]]
        for d in self.data:
            D[0].append(d["contig"])
            D[1].append(d["noncontig"])
     
        D[2] = [ D[0][i]-D[1][i] for i in range(len(D[0])) ]

        C = numpy.array([ i for i in range(len(D[0])) ])

        plotter.scatter(C, D[0], color='r', s = 50)
        plotter.scatter(C, D[1], color='g', s = 50)
        plotter.scatter(C, D[2], color='b', s = 10)
        plotter.xticks(rotation = 25)

        plotter.show()



    @staticmethod
    def print_help():
        print("Commands:\n\n",
              "set                          Change settings.\n",
              "                             Print current settings.\n",
              "    file filename            Set the file name that will be read/written to.\n",
              "    game WxH                 Set the current played game's dimensions width x height.\n",
              "    prompt [string]          Set the command prompt (An extra space is added to the prompt string)\n",
              "    prompt_count x           Set how many prompts are printed before the title text is printed.\n",
              "    delem c                  Set the delemiter to c when adding the longest contiguous series of boxes\n",
              "                                 and the number of noncontiguous boxes. (Default is /).\n",
              "del                          Delete last game played.\n",
              "help                         This help.\n",
              "quit                         Quit the program.\n",
              "plot                         Plot the current stored data.\n",
              "     eval [python string for plot_data]    Set the data that will be plotted.\n",
              "sort                         Sort via the third element.\n",
              "     fieldname               Sort via field name.\n",
              "read [[fa, a], [fb,a,b]... ] Read data from file with fields equal to integers.\n",
              "print                        Print data for viewing.\n",
              "      data                   Print the complete stored data\n",
              "      games                  Prints the total games stored int the file.\n",
              "write                        Write data to file and empty data.\n",
              "start | clear                Clears data for starting a new game.\n")

    @classmethod
    def game_input(self, txt, command_capture = True):

        s = input(txt)
        s = s.strip()

        if s == "":
            return(None)
        C = s.strip().split(self.delem)
        if (len(C) == 2) and C[0].isdigit() and C[1].isdigit():
            return([int(C[0]), int(C[1])])

        if command_capture == False:
            return(None)

        if s[:3] == "set":
            s = s[4:]

            if s[:4] == "game":
                s = s[5:]
                c = s.find("x")
                if c > 0:                   # If no x, return -1.
                    sx = s[:c].strip()
                    sy = s[c+1:].strip()
                    if sx.isdigit() and sy.isdigit():
                        self.boardxy[0] = int(sx)
                        self.boardxy[1] = int(sy)
            elif s[:4] == "file":
                s = s[5:].strip()
                if s[-4:] == ".csv":
                    self.filename = s

                if not os.path.exists(self.filename):
                    if self.write_data(header = True) == False:
                        self.ErrorMessage("Can not read or write to file.")                        
            elif s[:6] == "prompt":
                s = s[7:]
                if s != "":
                    self.prompt = s+" "
            elif s[:5] == "delem":
                s = s[6:]
                if len(s) == 1:
                    self.delem=s
                    
            else:
                self.print_settings()
        elif s[:3] == "del":                # Remove last row from data.
            self.data.pop()         
        elif s[:4] == "read":
            s = s[5:]
            if s[0] == "[": 
                try:
                    D = eval(s)
                    self.read_data(D)
                except:
                    self.ErrorMessage(f"Error with field input. [{s}]")

        elif s[:4] == "help":
            self.print_help()
        elif s[:4] == "quit":
            quit()
        elif s[:4] == "plot":
            s = s[5:]
            if s[:4] == "eval":
                s = s[5:]
                try:
                    s = s.replace("PLOTDATA", "stlcsv.plot_data")
                    s = s.replace("DATA", "stlcsv.data")
                    self.plot_data = eval(s)
                except:
                    self.ErrorMessage(f"Error in string \"{s}\"")

            else:
                self.plot()

        elif s[:4] == "sort":
            s = s[5:]
            if s == "":
                self.data.sort(key =itemgetter("contig"))
            else:
                c = False
                for f in self.fieldnames:
                    if f == s:
                        c = True
                        break
                if c == True:
                    self.data.sort(key = itemgetter(s))
        elif s[:4] == "exec":
            s = s[5:]
            try:

                s = s.replace("PLOTDATA", "stlcsv.plot_data")
                s = s.replace("DATA", "stlcsv.data")
                exec(s)
            except:
                self.ErrorMessage(f"Error in string \"{s}\"")
            
        elif s[:5] == "print":
            s = s[6:]
            if s == "data":
                self.print_data()
            elif s == "games":
                self.read_data([], list_games = True)
        elif s[:5] == "write":
            if self.write_data() == False:
                self.ErrorMessage("Can not read or write to file.")
        elif (s == "start") or (s == "clear"):
            self.data = []
        elif s[:11] == "prompt_count":
            s = s[12:]
            if s.isdigit():
                self.prompt_count = int(s)

        return(None)


    @classmethod
    def Do_Game(self):
        x = self.prompt_count
        while True:
            if x == self.prompt_count:
                print("\nInsert the longest contiguous series of boxes and the count of noncontiguous boxes. ", f"L{self.delem}N")
                print(" or insert commands.\n")

            if x == self.prompt_count:
                x = 0
            bx = self.game_input(self.prompt)
          
            if bx == None:
                continue
            x+=1
            if (self.boardxy[0] < 5) and (self.boardxy[1] < 5):
                continue
            self.data.append({self.fieldnames[0]:self.boardxy[0],
                               self.fieldnames[1]:self.boardxy[1],
                               self.fieldnames[2]:bx[0],
                               self.fieldnames[3]:bx[1]})

stlcsv.Do_Game()
