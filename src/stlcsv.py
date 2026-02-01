

import curses
import os



class stlcsv:


    @staticmethod
    def print_help():

        print("Commands: ")
        print("   set                          Print settings.")
        print("       file                     Set file name.")
        print("       fielda[n] fieldb[n]...   Set field to number.")
        print("       game WxH                 Set the board width x height.")
        print("                                Same as 'set width[W] height[H]'")
        print("   print")
        print("         data                   Print the current data stored.")
        print("   get                          Command to retrieve data.")
        print("       fielda[a1,a2,...] fieldb[b1,...] ...  Get data from file where all the fields contain")
        print("                                             data between [].")
        print("   plot                         Plot the data.")
        print("        scatter fielda fieldb ...   Plot via a scatter plot.")
        print("        line fielda fieldb ...      Line plot.")
        print("        bar fielda fieldb ...       Bar plot.")
        print("")
