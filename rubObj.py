class PhoneBook:

    def __init__(self, file_name, sep):
        self.file_name = file_name
        self.sep = sep
    
    def Load(self):
        name_phone = []
        f = open(self.file_name, 'r')
        for line in f:
            name_phone.append(line.rstrip())
        f.close()
        return name_phone

    def Search(self, str, name_phone):
        if str == '':
            print('\nNon hai inserito nulla!\n')
        else:
            print()
            for i in name_phone:
                if str.lower() in i.lower():
                    cols = i.split(self.sep)
                    print(cols[0] + ' ' + cols[1])
            print()

    def Add(self, add_name, add_number, name_phone):
        name_phone.append(add_name + self.sep + add_number)

    def Remove(self, remove_name, name_phone):
        check = 0
        for i in name_phone:
            cols = i.split(self.sep)
            if (remove_name.lower() == cols[0].lower()) or (remove_name.lower() == cols[1].lower()):
                name_phone.remove(i)
                check = 1
                print('\nContatto rimosso!\n')
                break
        if check == 0:
                print('\nContatto non trovato!\n')

    def Replace(self, toSearch, toReplace, name_phone):
        check = 0
        for i in range(len(name_phone)):
            cols = name_phone[i].split(self.sep)
            if toSearch.lower() == cols[0].lower():
                name_phone[i] = toReplace + self.sep + cols[1]
                check = 1
                break
            elif toSearch.lower() == cols[1].lower():
                name_phone[i] = cols[0] + self.sep + toReplace
                check = 1
                break
        if check == 0:
            print('\nContatto non trovato!\n')
        else:
            print('\nContatto modificato!\n')

    def Quit(self, name_phone):
        f = open(self.file_name,'w')
        for i in name_phone:
            f.write('%s\n' % (i))
        f.close()

# main
pb = PhoneBook('rubrica.txt', ' -> ')
pbList = pb.Load()
print('\nRUBRICA TELEFONICA\n1: Cerca\n2: Aggiungi\n3: Rimuovi\n4: Sostituisci\n5: Esci\n')
while(True):
    try:
        toDo = int(input())
    except:
        print('Non hai inserito un numero!\n')
        break
    if toDo == 1:
        searchStr = input('Inserisci la stringa da cercare:  ')
        pb.Search(searchStr, pbList)
    elif toDo == 2:
        addName = input('Inserisci il nome:  ')
        addNumber = input('Inserisci il numero:  ')
        pb.Add(addName, addNumber, pbList)
        print()
    elif toDo == 3:
        removeName = input('Inserisci il nome o il numero:  ')
        pb.Remove(removeName, pbList)
    elif toDo == 4:
        oldContact = input('Inserisci il nome o il numero da cambiare:  ')
        newContact = input('Inserisci il nuovo nome o numero:  ')
        pb.Replace(oldContact, newContact, pbList)
    elif toDo == 5:
        pb.Quit(pbList)
        print('Bye!\n')
        break
    else:
        print('Nessuna funzione associata a questo numero!\n')
