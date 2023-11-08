from tkinter import *
import random

lista_de_cores = ["red","green","pink", "gray", "purple"]

def trocar_cor():
    valor = random.randint(0,len(lista_de_cores)-1)
    cor_agora = lista_de_cores[valor]
    print(cor_agora)
    botao1.config(background=cor_agora)
    
    
janela = Tk()
janela.title("Criando meu primeiro GUI em tkinter")
janela.minsize(width=500, height=300)


#label
minha_label = Label(text="Eu sou uma label" , font=("Popins", 24, "bold"))
'''minha_label.config(text="new text")'''
minha_label.grid(row=0, column=0)

#button
botao1 = Button(text="Aperte ME", background="red", command=trocar_cor)
botao1.grid(row=1, column=0)















janela.mainloop()

