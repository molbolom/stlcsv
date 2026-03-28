


#######
#
#  keywords
#
#   [ kwA, None, [ [ kwA.A, funcA.A ], ] ],
#   [ kwB, funcB ],
#   [ 


class KeyFunctions:

    keywords = []

#
#   exec_keyword( key list )
#
#   Functions need to be set with def function_name( LIST )
#

    @classmethod
    def exec_keyword(self, kws):
        f = self.get_keyword(kws)
        if kws[0] == f[1][0]:
            print(f"Keyword \"{kws[0]}\" not found.")
            return()
            
        if f[0][1] == None:
            print(f"Can not execute \"{f[0][0]}({f[1]})\".")
            return()


        f[0][1](f[1])


#
#   new_keyword( key word list, function name )
#

    @classmethod
    def new_keyword(self, kws, function):
        
        L = self.get_keyword(kws)

        if L[0] == self.keywords:
            L[0].append([kws[0], None, []])
            L = self.get_keyword(kws)

        while L[1] != []:
            L[0][2].append([L[1][0], None, []])
            L = self.get_keyword(kws)

        L[0][1] = function

#
#   get_keyword( kw list ) Search through the list to find the keyword
#                          and return it.
#                Do_Add = True    Will append any new keywords to the list.
#


    @classmethod 
    def get_keyword(self, kws):
        searchkw = self.keywords

        retkw = searchkw
        p = -1 

        if searchkw == []:
            return([self.keywords, kws]) 

        for x in range(len(kws)):
            for key in searchkw:
                if key[0] == kws[x]:
                    searchkw = key[2]
                    retkw = key
                    p = x
                    break
            if p != x:
                break
                


        return([retkw, kws[p+1:]])


class test_funcs:

    @staticmethod
    def FuncA( L ):
        print(f"FuncA with arguments {L}.")

    @staticmethod
    def FuncB( L ):
        print(f"FuncB with arguments {L}.")
    
    @staticmethod
    def FuncC( L ):
        print(f"FuncC with arguments {L}.")
        
    
    @staticmethod
    def FuncD( L ):
        print(f"FuncD with arguments {L}.")
        
    
    @staticmethod
    def FuncE( L ):
        print(f"FuncE with arguments {L}.")
        
    
    @staticmethod
    def FuncF( L ):
        print(f"FuncF with arguments {L}.")
        
    @staticmethod
    def FuncG( L ):
        print(f"FuncG with arguments {L}.")



KeyFunctions.new_keyword(["FuncA"], test_funcs.FuncA)
KeyFunctions.new_keyword(["FuncB"], test_funcs.FuncB)
KeyFunctions.new_keyword(["FuncC"], test_funcs.FuncC)
KeyFunctions.new_keyword(["FuncD"], test_funcs.FuncD)
KeyFunctions.new_keyword(["FuncE"], test_funcs.FuncE)
KeyFunctions.new_keyword(["FuncF"], test_funcs.FuncF)
KeyFunctions.new_keyword(["FuncG"], test_funcs.FuncG)


while True:
    C = input("Input: ")
    if C == "quit":
        break

    KeyFunctions.exec_keyword(C.split())

