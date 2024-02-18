import tkinter as tk
import time
from tkinter import ttk


lista_de_horarios = (1,2,5,24,72)
data_user = []



def validar_horario(valor):
    
    return valor in lista_de_horarios 
 
def coleta_de_dados():
    
    global data_user
    data_user = data_informada.get() 

def bota_cadastrar():
    coleta_de_dados()
    janela.destroy()
janela = tk.Tk()
janela.title("CONTROLE DE NOTAS")


mensagem = tk.Label(text="SELECIONE O PERÍODO DESEJADO")
mensagem.grid(row=1,column=1,padx=10,pady=10,sticky='nswe',columnspan=1)
data_informada = ttk.Combobox(janela,values=lista_de_horarios, validate="all", validatecommand=(janela.register(validar_horario),'%P'))
data_informada.grid(row=1,column=2,padx=10,pady=10,sticky='nswe',columnspan=1)



botao_cadastrar = tk.Button(text="GERAR RELATÓRIO",command=bota_cadastrar)
botao_cadastrar.grid(row=4,column=1,padx=10,pady=10,sticky='nswe',columnspan=3)

janela.mainloop()


    
    