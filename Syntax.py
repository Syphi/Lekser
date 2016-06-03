from Leks import *
from Vizualizate import *

class SyntaxScan:
    syntax_tree = Tree("<Procedure>")

    def doscan(self):
        ScanLeks().scan()
        self.program_scan()
        visualize(self.syntax_tree, 0)

    def program_scan(self):
        leks = bList.pop(0)[1]
        if 501 == leks:
            self.syntax_tree.add(leks)
            self.syntax_tree.add(self.identifier_scan())
            self.syntax_tree.add(self.tocka_zapata())
            self.syntax_tree.add(self.block_scan())
            self.syntax_tree.add(self.tocka())
        else:
            raise SystemExit(0)

    def identifier_scan(self):
        NumberLeks = bList.pop(0)[1]
        if NumberLeks in indeteficator_table.values():
            return NumberLeks
        else:
            raise SystemExit(1)

    def tocka_zapata(self):
        leks = bList.pop(0)[1]
        if leks == 59:
            return leks
        else:
            raise SystemExit(2)

    def tocka(self):
        leks = bList.pop(0)[1]
        if leks == 46:
            return leks
        else:
            raise SystemExit(3)

    def dwe_tocki(self):
        leks = bList.pop(0)[1]
        if leks == 58:
            return leks
        else:
            raise SystemExit(3)

    def dwe_tocki_ravno(self):
        leks = bList.pop(0)[1]
        if leks == '301':
            return leks
        else:
            raise SystemExit(4)

    def BEGIN(self):
        leks = bList.pop(0)[1]
        if leks == 502:
            return leks
        else:
            raise SystemExit(5)

    def END(self):
        leks = bList.pop(0)[1]
        if leks == 503:
            return leks
        else:
            raise SystemExit(6)

    def FOR(self):
        leks = bList.pop(0)[1]
        if leks == 509:
            return leks
        else:
            raise SystemExit(7)

    def ENDFOR(self):
        leks = bList.pop(0)[1]
        if leks == 510:
            return leks
        else:
            raise SystemExit(8)

    def TO(self):
        leks = bList.pop(0)[1]
        if leks == 511:
            return leks
        else:
            raise SystemExit(9)

    def DO(self):
        leks = bList.pop(0)[1]
        # print(leks)
        if leks == 512:
            return leks
        else:
            raise SystemExit(10)

    def block_scan(self):
        block_list = Tree("<Block>")
        leks = bList[0][1]
        if 504 == leks:
            block_list.add(self.variable_declaration_scan())
            block_list.add(self.BEGIN())
            block_list.add(self.statmant_list_scan())
            block_list.add(self.END())
            return block_list
        else:
            raise SystemExit(11)

    def variable_declaration_scan(self):
        variable_list = Tree("<Variable-Declaration>")
        leks = bList.pop(0)[1]
        if leks == 504:
            variable_list.add(leks)
            variable_list.add(self.declaration_list_scan())
        return variable_list
        # else:
        #     print(0)

    def declaration_list_scan(self):
        declaration_list = Tree("<Declaration-List>")
        leks = bList[0][1]
        if leks in indeteficator_table.values():
            declaration_list.add(self.declaration_scan())
            self.declaration_list_scan()
        return declaration_list

    def declaration_scan(self):
        daclaration = Tree("<Declaration>")
        daclaration.add(self.identifier_scan())
        daclaration.add(self.dwe_tocki())
        leks1 = self.first_atribute_scan()
        if (leks1 == 506) or (leks1 == 507):
            daclaration.add(leks1)
        else:
            daclaration.add(leks1)
            daclaration.add(self.second_atribute_scan())
        return daclaration


    def first_atribute_scan(self):
        leks = bList.pop(0)[1]
        if (leks == 505) or (leks == 508):
            return leks
        elif (leks == 506) or (leks == 507):
            return leks
        else:
            raise SystemExit(12)

    def second_atribute_scan(self):
        leks = bList.pop(0)[1]
        if (leks == 506) or (leks == 507):
            return leks
        else:
            raise SystemExit(13)

    def statmant_list_scan(self):
        statment_list = Tree("<Statment-List>")
        leks = bList[0][1]
        if leks == 509:
            statment_list.add(self.statment_scan())
            statment_list.add(self.statmant_list_scan())
        else:
            return statment_list




    def statment_scan(self):
        statment = Tree("<Statment>")
        statment.add(self.FOR())
        statment.add(self.identifier_scan())
        statment.add(self.dwe_tocki_ravno())
        statment.add(self.loop_declaration_scan())
        statment.add(self.ENDFOR())
        # statment.add(510)
        statment.add(self.tocka_zapata())
        return statment



    def loop_declaration_scan(self):
        loop_declation = Tree("<Loop-declaration>")
        loop_declation.add(self.expretion_scan())
        loop_declation.add(self.TO())
        loop_declation.add(self.expretion_scan())
        loop_declation.add(self.DO())
        # loop_declation.add(512)
        loop_declation.add(self.statmant_list_scan())
        return loop_declation



    def expretion_scan(self):
        expretion_list = Tree("<Expretion-List>")
        expretion_list.add(self.multiplier_scan())
        expretion_list.add(self.multiplier_list_scan())
        return expretion_list

    def multiplier_scan(self):
        multiplier_list = Tree("<Multiplier>")
        leks = bList.pop(0)[1]
        if (leks in indeteficator_table.values()) or (leks in cons_table.values()):
            multiplier_list.add(leks)
            return multiplier_list
        else:
            raise SystemExit(14)

    def multiplier_list_scan(self):
        multiplier_list = Tree("<Multiplier-List>")
        leks = bList[0][1]
        if leks == 42 or leks == 47 or leks == 38 or leks == "299":
            multiplier_list.add(self.multiplication_instraction_scan())
            multiplier_list.add(self.multiplier_scan())
            multiplier_list.add(self.multiplier_list_scan())
        return multiplier_list

    def multiplication_instraction_scan(self):
        multiplier_inst_list = Tree("<Multiplication-Instraction>")
        leks = bList.pop(0)[1]
        if leks == 42 or leks == 47 or leks == 38 or leks == "299":
            multiplier_inst_list.add(leks)
            return multiplier_inst_list
        else:
            print(leks)
            raise SystemExit(15)


    # def var_indetifier_scan(self):
    #     declaration_var_list = []
    #     declaration_var_list.append(self.identifier_scan())
    #     declaration_var_list.append(self.dwe_tocki())
    #     declaration_var_list.append(self.atribute_scan())
    #     declaration_var_list.append()
    #
    # def atribute_scan(self):
    #     atribute_list = []
    #     leks = bList.pop(0)[1]
    #     if leks in arg_words_table.values():
    #         atribute_list.append(leks)
    #         return atribute_list()
    #     else:
    #         print(0)


SyntaxScan().doscan()