from Tables import *

class ScanLeks:
    numder_of_stroka = 1

    def get_next_sumvol(self, file):
        char = file.read(1)
        return char

    def get_next_word(self, file):
        global aList
        word = ""
        leksema = ""
        while leksema not in whitespaces:
            if leksema in dm:
                if word != '':
                    aList.append((word, self.numder_of_stroka))
                if leksema == ':':
                    leksema1 = self.get_next_sumvol(file)
                    if leksema1 == '=':
                        leksema += leksema1
                    else:
                        tell = file.tell()
                        file.seek(tell-1)
                if leksema != '':
                    aList.append((leksema, self.numder_of_stroka))
                return word
            if leksema == '(':
                aList.append((leksema, self.numder_of_stroka))
                return leksema
            word += str(leksema)
            leksema = self.get_next_sumvol(file)
            if leksema == '\n':
                self.numder_of_stroka += 1
            if leksema == "":
                return None
        if word != '':
            aList.append((word, self.numder_of_stroka))
        return word

    def scan(self):
        indet = 1001
        const = 601
        z = -1
        with open('project.txt', 'r') as file:
            while True:
                l = self.get_next_word(file)
                if l is None:
                    break
            j = len(aList)
            for i in range(j):
                if i > z:
                    leksema = aList[i][0]
                    k = 0
                    if leksema in arg_words_table:
                        # bList[i] = arg_words_table[leksema]
                        bList.append((leksema, arg_words_table[leksema]))
                    elif leksema in dm:
                        if leksema == "MOD":
                            # bList[i] = 299
                            bList.append((leksema, "299"))
                        else:
                            # bList[i] = ascii(leksema)
                            bList.append((leksema, ord(leksema)))
                    elif leksema == ":=":
                        # bList[i] = 301
                        bList.append((leksema, "301"))
                    elif leksema == "(":
                        leksema1 = aList[i+1][0]
                        if leksema1 == "*":
                            k = i + 2
                            for z in range(k, j):
                                if aList[z][0] == "*":
                                    if aList[z+1][0] == ")":
                                        break
                            if z != (j - 1):
                                z += 1
                            else:
                                bList.append(("Comment Error", aList[i][1]))
                                break
                        else:
                            # bList[i] = "Comment Eror"
                            bList.append(("Comment Error", aList[i][1]))
                            break
                    elif leksema[k] in letters:
                        if leksema in indeteficator_table:
                            bList.append((leksema, indeteficator_table[leksema]))
                        else:
                            indeteficator_table[leksema] = indet
                            bList.append((leksema, indeteficator_table[leksema]))
                            indet += 1
                    elif leksema[0] in digits:
                        flag = True
                        h = 0
                        for h in range(len(leksema)):
                            if leksema[h] not in digits:
                                flag = False
                        if flag == True:
                            if leksema in cons_table:
                                # bList[i] = cons_table[leksema]
                                bList.append((leksema, cons_table[leksema]))
                            else:
                                cons_table[leksema] = const
                                bList.append((leksema, cons_table[leksema]))
                                const += 1
                        else:
                            bList.append(("Const Error", aList[i][1]))
                            break
                    else:
                        bList.append(("Lexical Error", aList[i][1]))
                        print(leksema)
                        break


    def print_table(self):
        self.scan()
        # print(aList)
        # print(bList)
        for i in range(len(bList)):
            print(bList[i])
        print('\n Arg Word Table :')
        for y in arg_words_table:
            print(y, ' = ', arg_words_table[y])
        print('\n Indet Table :')
        for y in indeteficator_table:
            print(y, ' = ', indeteficator_table[y])
        print('\n Cons Table :')
        for y in cons_table:
            print(y, ' = ', cons_table[y])

#
ScanLeks().print_table()