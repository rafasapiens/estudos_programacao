from tkinter import *
from tkinter import ttk
import sqlite3

class Ppra():
    pp_name = 'PPRA2.db'
    print('Chegou até aqui')
    def __init__(self,wind):
        self.wind=wind
        self.wind.title('PPRA 1.0')
        
        self.tree=ttk.Treeview(height=5, columns=('c2', '3', '4','5', '6', '7', '8' ))
        self.tree.grid(row=1, column=0, columnspan=10)
        self.tree.heading('#0',  text='RAZÃO SOCIAL:', anchor=W)
        self.tree.heading('c2', text='CNPJ:', anchor=W)
        self.tree.heading('3',  text='ENDEREÇO:', anchor=W)
        self.tree.heading('4',  text='NUMERO:', anchor=W)
        self.tree.heading('5',  text='CEP:', anchor=W)
        self.tree.heading('6',  text='CEP:', anchor=W)
        self.tree.heading('7',  text='CEP:', anchor=W)
        self.tree.heading('8',  text='CEP:', anchor=W)
        
        self.viewing_records()
        print('Até aqui foi')
        
    #conexão com o banco de dados    
    def run_query (self, query, parameters=() ):
        with sqlite3.connect (self.pp_name) as conn:
            cursor = conn.cursor ()
            query_result = cursor.execute (query,  parameters)
            conn.commit ()
        print('banco conectado com sucesso')
        return query_result
    
    #visualizar dados do banco
    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
         #a query chamada é SELECT *(tudo) da tabela 'dados' ordenado pelo 'id' decrescente  
        query = 'SELECT * FROM dados ORDER BY id DESC'
        db_rows= self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 'end', text=row[1], values=(row[2], row[3], row[4], row[5], row[6], row[7], row[8] ))
                
            print('View do banco foi')
           
if __name__== '__main__':
    wind=Tk()
    application = Ppra(wind)
    wind.mainloop()
