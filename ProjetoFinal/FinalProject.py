import pandas as pd 
import sqlite3 as sq
import tkinter as tk
import matplotlib.pyplot as plt


def INICIAL(): #cria a interface de preenchimento e envia dados para o SQLite e depois exporta para o arquivo Excel
    dataBase = sq.connect('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/ProjetoFinal/projetoFinal.db')
    db = dataBase.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS produtosEstoque(ID INTEGER, Nome TEXT, Quantidade INTEGER, Preço FLOAT)")
    dataBase.commit()


    def preenchimento():
        dataBase = sq.connect('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/ProjetoFinal/projetoFinal.db')
        db = dataBase.cursor()
        db.execute("INSERT INTO produtosEstoque VALUES(:ID, :Nome, :Quantidade, :Preço)", 
                {
                    'ID':respID.get(),
                    'Nome':respNome.get(),
                    'Quantidade':respQnt.get(),
                    'Preço':respPreco.get()

                })
        
        #Deleção de nomes do campo após nomes inseridos
        respID.delete(0, 'end') #deletar do primeiro caractere ate o final
        respNome.delete(0, 'end')
        respQnt.delete(0, 'end')
        respPreco.delete(0, 'end')

        dataBase.commit()
        dataBase.close()


    def exportar():
        dataBase = sq.connect('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/ProjetoFinal/projetoFinal.db')
        db = dataBase.cursor()
        db.execute("SELECT *, oid FROM produtosEstoque")

        produtosCadastrados = db.fetchall()
        produtosCadastrados = pd.DataFrame(produtosCadastrados, columns = ['ID', 'Nome', 'Quantidade', 'Preço', 'idSQLite'])
        produtosCadastrados.to_excel('finalProdutosCad.xlsx')
        
        print(produtosCadastrados)
        dataBase.commit()
        dataBase.close()

    def grafico():
        graphs = pd.read_excel('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/finalProdutosCad.xlsx')
        '''graphs.hist(column='Preço', bins = 100)
        plt.show()'''
        plt.scatter(graphs['Preço'], graphs['Quantidade'], color='blue') #gera grafico de dispersao
        plt.title('Preço vs Quantidade')
        plt.xlabel('Preço')
        plt.ylabel('Quantidade')
        plt.grid(True)
        plt.show()


    #cria janela
    janela = tk.Tk()
    janela.title('Cadastro de Produtos - Estoque')

    #cria etiquetas - nomeia linha a ser preenchida
    Id = tk.Label(janela, text = 'ID', width = 18)
    Id.grid(row = 0, column = 0, padx = 50, pady = 20)

    Nome = tk.Label(janela, text = 'Nome', width = 18)
    Nome.grid(row = 1, column = 0, padx = 50, pady = 20)

    Quantidade = tk.Label(janela, text = 'Quantidade', width = 18)
    Quantidade.grid(row = 2, column = 0, padx = 50, pady = 20)

    Preço = tk.Label(janela, text = 'Preço', width = 18)
    Preço.grid(row = 3, column = 0, padx = 50, pady = 20)

    #cria blocos de Input
    respID = tk.Entry(janela, text = 'ID', width = 30)
    respID.grid(row = 0, column = 1, padx = 15, pady = 15)

    respNome = tk.Entry(janela, text = 'Nome', width = 30)
    respNome.grid(row = 1, column = 1, padx = 15, pady = 15)

    respQnt = tk.Entry(janela, text = 'Quantidade', width = 30)
    respQnt.grid(row = 2, column = 1, padx = 15, pady = 15)

    respPreco = tk.Entry(janela, text = 'Preço', width = 30)
    respPreco.grid(row = 3, column = 1, padx = 15, pady = 15)

    #criar botões - Cadastrar e Exportar e Gráfico
    botaoCadastro = tk.Button(janela, text = 'Cadastrar Produto', command = preenchimento)
    botaoCadastro.grid(row = 4, column = 0, padx = 10, pady = 0, columnspan = 1, ipadx = 100)

    botaoExportar = tk.Button(janela, text = 'Exportar para Excel', command = exportar)
    botaoExportar.grid(row = 4, column = 1, padx = 10, pady = 0, columnspan = 1, ipadx = 100)

    botaoGraf = tk.Button(janela, text = 'Gerar Gráfico', command = grafico)
    botaoGraf.grid(row = 5, column = 0, padx = 10, pady = 5, columnspan = 2, ipadx = 100)


    #mantém a janela aberta
    janela.mainloop()


x = INICIAL()