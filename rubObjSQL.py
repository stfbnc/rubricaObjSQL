from sqlite3 import connect

class PhoneBook:

    def __init__(self, file_name):
        self.file_name = file_name
    
    def DBconnection(self):
        conn = connect(self.file_name)
        curs = conn.cursor()
        curs.execute('CREATE TABLE IF NOT EXISTS CONTACTS ('+
                     'NAME       VARCHAR NOT NULL,'+
                     'CONTACT_ID INTEGER PRIMARY KEY AUTOINCREMENT,'+
                     'PHONE      VARCHAR NOT NULL'+
                     ');')
        return conn, curs
    
    def Search(self, str, curs):
        if str == '':
            print('\nNon hai inserito nulla!\n')
        else:
            curs.execute('SELECT * FROM CONTACTS WHERE NAME LIKE \'%' + str + '%\' OR PHONE LIKE \'%' + str + '%\'')
            print()
            for (name, id, phone) in curs.fetchall():
                print(name + ' ' + phone)
            print()

    def Add(self, add_name, add_number, curs):
        curs.execute('INSERT INTO CONTACTS (NAME, PHONE) VALUES (\'' + add_name + '\', \'' + add_number + '\')')
    
    def Remove(self, remove_name, curs):
        curs.execute('DELETE FROM CONTACTS WHERE NAME = \'' + remove_name + '\' OR PHONE = \'' + remove_name + '\'')
        if curs.rowcount > 0:
            print('\nContatto rimosso!\n')
        else:
            print('\nContatto non trovato!\n')

    def Replace(self, toSearch, toReplace, curs):
        curs.execute('SELECT NAME FROM CONTACTS WHERE NAME = \'' + toSearch + '\'')
        if len(curs.fetchall()) > 0:
            curs.execute('UPDATE CONTACTS SET NAME = \'' + toReplace + '\' WHERE NAME = \'' + toSearch + '\'')
            print('\nContatto modificato!\n')
        else:
            curs.execute('SELECT PHONE FROM CONTACTS WHERE PHONE = \'' + toSearch + '\'')
            if len(curs.fetchall()) > 0:
                curs.execute('UPDATE CONTACTS SET PHONE = \'' + toReplace + '\' WHERE PHONE = \'' + toSearch + '\'')
                print('\nContatto modificato!\n')
            else:
                print('\nContatto non trovato!\n')

    def closeConn(self, conn):
        conn.commit()
        conn.close()

# main
pb = PhoneBook('contacts.db')
cnt, crs = pb.DBconnection()
print('\nRUBRICA TELEFONICA\n1: Cerca\n2: Aggiungi\n3: Rimuovi\n4: Sostituisci\n5: Esci\n')
while(True):
    try:
        toDo = int(input())
        if toDo == 1:
            searchStr = input('Inserisci la stringa da cercare:  ')
            pb.Search(searchStr, crs)
        elif toDo == 2:
            addName = input('Inserisci il nome:  ')
            addNumber = input('Inserisci il numero:  ')
            pb.Add(addName, addNumber, crs)
            print()
        elif toDo == 3:
            removeName = input('Inserisci il nome o il numero:  ')
            pb.Remove(removeName, crs)
        elif toDo == 4:
            oldContact = input('Inserisci il nome o il numero da cambiare:  ')
            newContact = input('Inserisci il nuovo nome o numero:  ')
            pb.Replace(oldContact, newContact, crs)
        elif toDo == 5:
            pb.closeConn(cnt)
            print('Bye!\n')
            break
        else:
            print('Nessuna funzione associata a questo numero!\n')
    except:
        print('Non hai inserito un numero!\n')
