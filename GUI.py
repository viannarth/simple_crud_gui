from controller import Controller

import tkinter as tk
from tkinter import *


LARGEFONT = ("Verdana", 35)

controller = Controller()

class tkinterApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="\n\nInterface do Catálogo", font=("Comfortaa", 50)).pack()
        tk.Label(self, text="\nSelecione a opção desejada\n", font=("Arial", 20)).pack()

        sub1 = tk.Button(self, text="Cadastrar Prestador de Serviço", command=lambda: master.switch_frame(InsertPage))
        sub2 = tk.Button(self, text='Excluir Prestador de serviço', command=lambda: master.switch_frame(DeletePage))
        sub3 = tk.Button(self, text='Consultar Prestadores de serviço', command=lambda: master.switch_frame(ReadPage))
        sub4 = tk.Button(self, text='Atualizar Prestador de serviço', command=lambda: master.switch_frame(UpdatePage))

        sub1['height'] = 5
        sub2['height'] = 5
        sub3['height'] = 5
        sub4['height'] = 5

        sub1['width'] = 60
        sub2['width'] = 60
        sub3['width'] = 60
        sub4['width'] = 60

        sub1.pack()
        sub2.pack()
        sub3.pack()
        sub4.pack()


class InsertPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        value1 = tk.StringVar()
        value2 = tk.StringVar()
        value3 = tk.StringVar()
        value4 = tk.StringVar()
        value5 = tk.StringVar()
        value6 = tk.StringVar()
        value7 = tk.StringVar()
        value8 = tk.StringVar()
        value9 = tk.StringVar()
        value10 = tk.StringVar()
        value11 = tk.StringVar()
        value12 = tk.StringVar()

        word = tk.StringVar()

        def verify(var, index, mode):
            if value6.get() == "103D":
                word.set("      Endereço certo ")
                adress()

            else:
                word.set("      Endereço errado")
                value7.set("")
                value8.set("")
                value9.set("")
                value10.set("")
                value11.set("")
                value12.set("")

        def adress():
            tk.Label(self, text="Rua:", font=("Arial", 20)).grid(row=9, column=1)
            tk.Label(self, text="Número:", font=("Arial", 20)).grid(row=10, column=1)
            tk.Label(self, text="Complemento:", font=("Arial", 20)).grid(row=11, column=1)
            tk.Label(self, text="Bairro:", font=("Arial", 20)).grid(row=12, column=1)
            tk.Label(self, text="Cidade:", font=("Arial", 20)).grid(row=13, column=1)
            tk.Label(self, text="UF:", font=("Arial", 20)).grid(row=14, column=1)

            entry7 = tk.Entry(self, textvariable=value7)
            entry8 = tk.Entry(self, textvariable=value8)
            entry9 = tk.Entry(self, textvariable=value9)
            entry10 = tk.Entry(self, textvariable=value10)
            entry11 = tk.Entry(self, textvariable=value11)
            entry12 = tk.Entry(self, textvariable=value12)

            entry7.grid(row=9, column=2)
            entry8.grid(row=10, column=2)
            entry9.grid(row=11, column=2)
            entry10.grid(row=12, column=2)
            entry11.grid(row=13, column=2)
            entry12.grid(row=14, column=2)

            value7.set("Rua H8C")

        def submit():
            id = value1.get()
            nome = value2.get()
            numero = value3.get()
            datanasc= value4.get()
            endereco = value5.get()
            contato = value6.get()

            label = tk.Label(self, text="Funcionário criado com sucesso!", bg="#d9d9d9", fg="#dc143c", wraplength=100)
            label.config(height=3, width=20)
            label.grid(row=20, column=1, padx=10, pady=10)
            self.after(5000, label.destroy)

            value1.set("")
            value2.set("")
            value3.set("")
            value4.set("")
            value5.set("")
            value6.set("")
            value7.set("")
            value8.set("")
            value9.set("")
            value10.set("")
            value11.set("")
            value12.set("")

        tk.Label(self, text="ID:", font=("Arial", 20)).grid(row=3, column=1)
        tk.Label(self, text="Nome:", font=("Arial", 20)).grid(row=4, column=1)
        tk.Label(self, text="CPF/CNPJ:", font=("Arial", 20)).grid(row=5, column=1)
        tk.Label(self, text="Data de Nascimento:", font=("Arial", 20)).grid(row=6, column=1)
        tk.Label(self, text="Contato:", font=("Arial", 20)).grid(row=7, column=1)
        tk.Label(self, text="CEP:", font=("Arial", 20)).grid(row=8, column=1)

        entry1 = tk.Entry(self, textvariable=value1)
        entry2 = tk.Entry(self, textvariable=value2)
        entry3 = tk.Entry(self, textvariable=value3)
        entry4 = tk.Entry(self, textvariable=value4)
        entry5 = tk.Entry(self, textvariable=value5)
        entry6 = tk.Entry(self, textvariable=value6)

        entry1.grid(row=3, column=2)
        entry2.grid(row=4, column=2)
        entry3.grid(row=5, column=2)
        entry4.grid(row=6, column=2)
        entry5.grid(row=7, column=2)
        entry6.grid(row=8, column=2)

        value6.trace("w", verify)

        tk.Label(self, textvariable=word, font=("Arial", 10)).grid(row=8, column=3)

        button = tk.Button(self, text='Criar Funcionario', command=submit)

        button.grid(row=18, column=2, padx=10, pady=10)

        buttonback = tk.Button(self, text="Página Inicial",
                           command=lambda: master.switch_frame(StartPage))

        buttonback.config(height=5, width=40)

        buttonback.grid(row=19, column=1, padx=10, pady=10)


class DeletePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        ID = tk.StringVar()

        def submit():
            id = ID.get()

            if id == '0':
                label = tk.Label(self, text="Dados inválidos, não foi possível excluir funcionário", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)

            else:
                label = tk.Label(self, text="Funcionário Excluído com Sucesso!", bg="#d9d9d9", fg="#dc143c",
                                 wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)


        tk.Label(self, text="Id do funcionário a ser excluído:", font=("Arial", 20)).pack()

        entry = tk.Entry(self, textvariable=ID).pack()

        button = tk.Button(self, text='Excluir Funcionario', command=submit).pack()

        buttonback = tk.Button(self, text="Página Inicial",
                               command=lambda: master.switch_frame(StartPage))

        buttonback.config(height=5, width=40)

        tk.Label(self, text="", height = 30).pack()

        buttonback.pack()


class ReadPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        list = ["ID", "Nome", "CPF/CNPJ", "Data de Nascimento", "Endereço", "Contato"]

        for j in range(len(list)):
            label = Entry(self, width=27, fg='blue',
                          font=('Arial', 16, 'bold'))

            label.grid(row=0, column=j)
            label.insert(END, list[j])


        button = tk.Button(self, text="Página Inicial",
                             command=lambda: master.switch_frame(StartPage))

        button.config(height=5, width=20)

        button.grid(row=2, column=3, padx=0, pady=0)


class UpdatePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        value1 = tk.StringVar()
        value2 = tk.StringVar()
        value3 = tk.StringVar()
        value4 = tk.StringVar()
        value5 = tk.StringVar()
        value6 = tk.StringVar()
        value7 = tk.StringVar()
        value8 = tk.StringVar()
        value9 = tk.StringVar()
        value10 = tk.StringVar()
        value11 = tk.StringVar()
        value12 = tk.StringVar()

        word = tk.StringVar()

        ID = tk.StringVar()

        def verify(var, index, mode):
            if value6.get() == "103D":
                word.set("      Endereço válido  ")
                adress()
            else:
                word.set("      Endereço inválido")
                value7.set("")
                value8.set("")
                value9.set("")
                value10.set("")
                value11.set("")
                value12.set("")

        def check():
            if ID.get() == '0':
                label = tk.Label(self, text="Dados inválidos, não foi possível acessar funcionário", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.grid(row=21, column=1, padx=10, pady=30)
                self.after(5000, label.destroy)

            else:
                Preencher()

        def adress():
            label1 = tk.Label(self, text="Rua:", font=("Arial", 20)).grid(row=9, column=1)
            tk.Label(self, text="Número:", font=("Arial", 20)).grid(row=10, column=1)
            tk.Label(self, text="Complemento:", font=("Arial", 20)).grid(row=11, column=1)
            tk.Label(self, text="Bairro:", font=("Arial", 20)).grid(row=12, column=1)
            tk.Label(self, text="Cidade:", font=("Arial", 20)).grid(row=13, column=1)
            tk.Label(self, text="UF:", font=("Arial", 20)).grid(row=14, column=1)

            entry7 = tk.Entry(self, textvariable=value7)
            entry8 = tk.Entry(self, textvariable=value8)
            entry9 = tk.Entry(self, textvariable=value9)
            entry10 = tk.Entry(self, textvariable=value10)
            entry11 = tk.Entry(self, textvariable=value11)
            entry12 = tk.Entry(self, textvariable=value12)

            entry7.grid(row=9, column=2)
            entry8.grid(row=10, column=2)
            entry9.grid(row=11, column=2)
            entry10.grid(row=12, column=2)
            entry11.grid(row=13, column=2)
            entry12.grid(row=14, column=2)

            value7.set("Rua H8C")

        def submit():
            id = value1.get()
            nome = value2.get()
            numero = value3.get()
            datanasc = value4.get()
            endereco = value5.get()
            contato = value6.get()

            label = tk.Label(self, text="Dados inválidos, não foi possível atualizar funcionário", bg="#d9d9d9",
                             fg="#dc143c", wraplength=100)
            label.grid(row=20, column=1, padx=10, pady=30)
            self.after(5000, label.destroy)

            value1.set("")
            value2.set("")
            value3.set("")
            value4.set("")
            value5.set("")
            value6.set("")
            value7.set("")
            value8.set("")
            value9.set("")
            value10.set("")
            value11.set("")
            value12.set("")

        def Preencher():
            tk.Label(self, text="ID:", font=("Arial", 20)).grid(row=3, column=1)
            tk.Label(self, text="Nome:", font=("Arial", 20)).grid(row=4, column=1)
            tk.Label(self, text="CPF/CNPJ:", font=("Arial", 20)).grid(row=5, column=1)
            tk.Label(self, text="Data de Nascimento:", font=("Arial", 20)).grid(row=6, column=1)
            tk.Label(self, text="Contato:", font=("Arial", 20)).grid(row=7, column=1)
            tk.Label(self, text="CEP:", font=("Arial", 20)).grid(row=8, column=1)

            entry1 = tk.Entry(self, textvariable=value1)
            entry2 = tk.Entry(self, textvariable=value2)
            entry3 = tk.Entry(self, textvariable=value3)
            entry4 = tk.Entry(self, textvariable=value4)
            entry5 = tk.Entry(self, textvariable=value5)
            entry6 = tk.Entry(self, textvariable=value6)

            entry1.grid(row=3, column=2)
            entry2.grid(row=4, column=2)
            entry3.grid(row=5, column=2)
            entry4.grid(row=6, column=2)
            entry5.grid(row=7, column=2)
            entry6.grid(row=8, column=2)

            button = tk.Button(self, text='Criar Funcionario', command=submit).grid(row=17, column=1)

        value6.trace("w", verify)

        tk.Label(self, text="Id do funcionário a ser atualizado:", font=("Arial", 20)).grid(row=0, column=1, padx=10, pady=20)

        tk.Label(self, textvariable= word, font=("Arial", 10)).grid(row=8, column=3)

        entry = tk.Entry(self, textvariable=ID).grid(row=1, column=1, padx=10, pady=20)

        button = tk.Button(self, text='Submeter Funcionário a ser atualizado', command=check).grid(row=2, column=1,
                                                                                                    padx=10, pady=20)

        buttonback = tk.Button(self, text="Página Inicial",
                               command=lambda: master.switch_frame(StartPage))

        buttonback.config(height=5, width=40)

        buttonback.grid(row=18, column=1, padx=10, pady=10)


def main():
    app = tkinterApp()
    app.mainloop()

if __name__ == "__main__":
    main()