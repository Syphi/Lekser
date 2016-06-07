from Syntax import *

class GeneratorASM:
    countr = 1

    def __init__(self):
        self.file = open("Code.txt",'w')
        self.LowBound = 0
        self.HightBound = 0
        self.iterator = ''

    def __del__(self):
        self.file.close()


    def generate(self, tree, label = 1 ):
        rule = tree.name
        if rule == "<Procedure>":
            self.generate(tree.nodes[3])
        elif rule == "<Block>":
            self.generate(tree.nodes[0])
            self.generate(tree.nodes[2])
        elif rule == "<Variable-Declaration>":
            self.file.write("DATA SEGMENT")
            self.file.write("\n")
            self.generate(tree.nodes[1])
            self.file.write("\n")
            self.file.write("DATA ENDS\n")
        elif rule == "<Declaration-List>":
            if len(tree.nodes) != 0:
                self.generate(tree.nodes[0])
                self.generate(tree.nodes[1])
        elif rule == "<Declaration>":
            self.file.write(str(tree.nodes[0]))
            self.file.write(' DD ')
        elif rule == "<Statment-List>":
            if len(tree.nodes) !=0:
                self.generate(tree.nodes[0])
                self.generate(tree.nodes[1])
        elif rule == "<Statment>":
            self.iterator = tree.nodes[1]
            self.generate(tree.nodes[3])
        elif rule == "<Loop-declaration>":
            self.file.write("   MOV    AX,")
            self.generate(tree.nodes[0])
            self.file.write("\n")
            self.file.write("   MOV ")
            self.file.write(str(self.iterator))
            self.file.write(" , AX\n")
            self.file.write("   MOV    AX,")
            self.generate(tree.nodes[2])
            self.file.write("\n")
            self.file.write("   CMP    AX,i\n")
            self.file.write("   JL     ?L\n")
            self.file.write(str(self.countr + 1))
            self.file.write("\n")
            self.file.write("   MOV    DX,1\n")
            self.file.write("   MOV    .S+0,DX\n")
            self.file.write("   SUB    AX,i\n")
            self.file.write("   CWD\n")
            self.file.write("   DIV    .S+0\n")
            self.file.write("   INC    AX\n")
            self.file.write("   MOV    CX,AX\n")
            self.file.write("?L" )
            self.file.write(str(self.countr+1))
            self.file.write(":   NOP")
            self.file.write("\n")
            self.countr += 2
            self.generate(tree.nodes[4])
            self.countr -= 2
            self.file.write("   MOV    AX,i\n")
            self.file.write("   ADD    AX,.S+0\n")
            self.file.write("   MOV    i,AX\n")
            self.file.write("   LOOP    ?L\n" )
            self.file.write(str(self.countr+1))
            self.file.write("?L")
            self.file.write(str(self.countr))
            self.file.write(":   NOP")
            self.file.write("\n")
        elif rule == "<Expretion>":
            if len(tree.nodes) != 0:
                number = int(self.get_key(tree.nodes[0]))
                mlist = tree.nodes[1]
                while len(mlist.nodes) != 0:
                    number2 = int(self.get_key(mlist.nodes[1]))
                    instraction = mlist.nodes[0]
                    if instraction == 299:
                        number %= number2
                    elif instraction ==42:
                        number *= number2
                    elif instraction ==47:
                        number /= number2
                    elif instraction ==38:
                        number &= number2
                    mlist = mlist.nodes[2]
                self.file.write(str(number))

    def get_key(self, value):
        for key in cons_table.keys():
            if cons_table[key] == value:
                return key

    def zapysk(self):
        ScanLeks().print_table()
        SyntaxScan().doscan()
        self.generate(SyntaxScan.syntax_tree)





GeneratorASM().zapysk()




