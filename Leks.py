from Tables import *


class ScanLeks:
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
                    aList.append(word)
                if leksema == ':':
                    leksema1 = self.get_next_sumvol(file)
                    if leksema1 == '=':
                        leksema += leksema1
                    else:
                        tell = file.tell()
                        file.seek(tell-1)
                if leksema != '':
                    aList.append(leksema)
                return word
            word += str(leksema)
            leksema = self.get_next_sumvol(file)
            if leksema == "":
                return None
        if word != '':
            aList.append(word)
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
                    leksema = aList[i]
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
                        leksema1 = aList[i+1]
                        if leksema1 == "*":
                            k = i + 2
                            for z in range(k, j):
                                if aList[z] == "*":
                                    if aList[z+1] == ")":
                                        break
                            if z != (j - 1):
                                z += 1
                            else:
                                bList.append("Comment Error")
                        else:
                            # bList[i] = "Comment Eror"
                            bList.append("Comment Eror")
                    elif leksema[k] in letters:
                        if leksema in indeteficator_table:
                            bList.append((leksema, indeteficator_table[leksema]))
                        else:
                            indeteficator_table[leksema] = indet
                            bList.append((leksema, indeteficator_table[leksema]))
                            indet += 1
                    elif leksema[0] in digits:
                        if leksema in cons_table:
                            # bList[i] = cons_table[leksema]
                            bList.append((leksema, cons_table[leksema]))
                        else:
                            cons_table[leksema] = const
                            bList.append((leksema, cons_table[leksema]))
                            const += 1
                    else:
                        bList.append("Syntax Eror")
                        print(leksema)

    def print_table(self):
        self.scan()
        print(aList)
        print(bList)
        # for i in range(len(bList)):
        #     print(aList[i], " : ", bList[i])

ScanLeks().print_table()