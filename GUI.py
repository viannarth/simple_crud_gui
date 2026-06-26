import tkinter as tk
from tkinter import *

LARGEFONT = ("Verdana", 35)

def atualizar():
    print("passou")

def submeter(structure, value1, value2, value3, value4, value5, value6, function):

    id = value1.get()
    nome = value2.get()
    numero = value3.get()
    datanasc = value4.get()
    endereco = value5.get()
    contato = value6.get()


    # label = tk.Label(structure, text="Dados inválidos, não foi possível criar funcionário", bg="black", fg="white",
    #                  wraplength=100)
    # label.place(relx=0.5, rely=0.5, anchor="center")
    # structure.after(5000, label.destroy)

    function()

def createButton(structure, position : int, name : str, value1, value2, value3, value4, value5, value6, function):
    button = tk.Button(structure, text= name, command=submeter(structure, value1, value2, value3, value4, value5, value6, function))

    button.grid(row=position, column=1, padx=10, pady=10)


def Fill (structure, position:int):
    value1 = tk.StringVar()
    value2 = tk.StringVar()
    value3 = tk.StringVar()
    value4 = tk.StringVar()
    value5 = tk.StringVar()
    value6 = tk.StringVar()

    def submit(function):
        id = value1.get()
        nome = value2.get()
        numero = value3.get()
        datanasc = value4.get()
        endereco = value5.get()
        contato = value6.get()

        # function()

    tk.Label(structure, text="ID:", font=("Arial", 20)).grid(row=position, column=1)
    tk.Label(structure, text="Nome:", font=("Arial", 20)).grid(row=position+1, column=1)
    tk.Label(structure, text="CPF/CNPJ", font=("Arial", 20)).grid(row=position+2, column=1)
    tk.Label(structure, text="Data de Nascimento", font=("Arial", 20)).grid(row=position+3, column=1)
    tk.Label(structure, text="Endereço", font=("Arial", 20)).grid(row=position+4, column=1)
    tk.Label(structure, text="Contato", font=("Arial", 20)).grid(row=position+5, column=1)

    entry1 = tk.Entry(structure, textvariable=value1)
    entry2 = tk.Entry(structure, textvariable=value2)
    entry3 = tk.Entry(structure, textvariable=value3)
    entry4 = tk.Entry(structure, textvariable=value4)
    entry5 = tk.Entry(structure, textvariable=value5)
    entry6 = tk.Entry(structure, textvariable=value6)

    entry1.grid(row=position, column=2)
    entry2.grid(row=position+1, column=2)
    entry3.grid(row=position+2, column=2)
    entry4.grid(row=position+3, column=2)
    entry5.grid(row=position+4, column=2)
    entry6.grid(row=position+5, column=2)

    # button = tk.Button(structure, text='Criar Funcionario', command=submit(structure, atualizar))
    #
    # button.grid(row=9, column=1, padx=10, pady=10)

    button = tk.Button(structure, text='Criar Funcionario', command=submit(atualizar))

    button.grid(row=position+6, column=1, padx=10, pady=10)

    # buttonback = tk.Button(structure, text="Startpage",
    #                        command=lambda: controller.show_frame(StartPage))
    #
    # buttonback.config(height=5, width=40)

    # tk.Label(structure, text="").grid(row=7, column=0, padx=340, pady=200)
    # buttonback.grid(row=8, column=1, padx=10, pady=10)


########################################################################



# class StartTable:
#
#     def __init__(self, root, list):
#
#         for j in range(len(list)):
#             self.e = Entry(root, width=10, fg='blue',
#                           font=('Arial', 16, 'bold'))
#
#             self.e.grid(row=0, column=j)
#             self.e.insert(END, value)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="\n\nInterface do Catálogo", font=("Comfortaa", 50)).pack()
        tk.Label(self, text="\nSelecione a opção desejada\n", font=("Arial", 20)).pack()

        sub1 = tk.Button(self, text='Cadastrar Prestador de serviço', command=lambda: controller.show_frame(Page1))
        sub2 = tk.Button(self, text='Excluir Prestador de serviço', command=lambda: controller.show_frame(Page2))
        sub3 = tk.Button(self, text='Consultar Prestadores de serviço', command=lambda: controller.show_frame(Page3))
        sub4 = tk.Button(self, text='Atualizar Prestador de serviço', command=lambda: controller.show_frame(Page4))

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


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        value1 = tk.StringVar()
        value2 = tk.StringVar()
        value3 = tk.StringVar()
        value4 = tk.StringVar()
        value5 = tk.StringVar()
        value6 = tk.StringVar()

        def submit():
            id = value1.get()
            nome = value2.get()
            numero = value3.get()
            datanasc= value4.get()
            endereco = value5.get()
            contato = value6.get()

            # print("Seu ID é : " + id)
            # print("Seu nome é : " + nome)
            # print("Seu numero é : " + numero)
            # print("Sua data de nascimento é : " + datanasc)
            # print("Seu endereco é : " + endereco)
            # print("Seu contato é: " + contato)

            label = tk.Label(self, text="Funcionário criado com sucesso!", bg="black", fg="white", wraplength=100)
            label.place(relx=0.5, rely=0.5, anchor="center")
            self.after(5000, label.destroy)

            value1.set("")
            value2.set("")
            value3.set("")
            value4.set("")
            value5.set("")
            value6.set("")

        tk.Label(self, text="").grid(row=0, column=0, padx=340, pady=10)

        tk.Label(self, text="ID:", font=("Arial", 20)).grid(row=0, column=1)
        tk.Label(self, text="Nome:", font=("Arial", 20)).grid(row=1, column=1)
        tk.Label(self, text="CPF/CNPJ", font=("Arial", 20)).grid(row=2, column=1)
        tk.Label(self, text="Data de Nascimento", font=("Arial", 20)).grid(row=3, column=1)
        tk.Label(self, text="Endereço", font=("Arial", 20)).grid(row=4, column=1)
        tk.Label(self, text="Contato", font=("Arial", 20)).grid(row=5, column=1)

        entry1 = tk.Entry(self, textvariable=value1)
        entry2 = tk.Entry(self, textvariable=value2)
        entry3 = tk.Entry(self, textvariable=value3)
        entry4 = tk.Entry(self, textvariable=value4)
        entry5 = tk.Entry(self, textvariable=value5)
        entry6 = tk.Entry(self, textvariable=value6)

        entry1.grid(row=0, column=2)
        entry2.grid(row=1, column=2)
        entry3.grid(row=2, column=2)
        entry4.grid(row=3, column=2)
        entry5.grid(row=4, column=2)
        entry6.grid(row=5, column=2)

        button = tk.Button(self, text='Criar Funcionario', command=submit)

        button.grid(row=6, column=2, padx=10, pady=10)

        buttonback = tk.Button(self, text="Startpage",
                           command=lambda: controller.show_frame(StartPage))

        buttonback.config(height=5, width=40)

        tk.Label(self, text="").grid(row=7, column=0, padx=340, pady=200)
        buttonback.grid(row=8, column=1, padx=10, pady=10)



# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ID = tk.StringVar()

        def submit():
            id = ID.get()

            if id == '0':
                label = tk.Label(self, text="Dados inválidos, não foi possível excluir funcionário", bg="black", fg="white",
                                 wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)

            else:
                label = tk.Label(self, text="Funcionário Excluído com Sucesso!", bg="black",
                                 fg="white",
                                 wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)


        tk.Label(self, text="Id do funcionário a ser excluído:", font=("Arial", 20)).pack()
        entry = tk.Entry(self, textvariable=ID).pack()

        button = tk.Button(self, text='Excluir Funcionario', command=submit).pack()

        buttonback = tk.Button(self, text="Startpage",
                               command=lambda: controller.show_frame(StartPage))

        buttonback.config(height=5, width=40)

        tk.Label(self, text="", height = 30).pack()


        buttonback.pack()


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # tk.Frame.__init__(self, parent)
        # label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        # label.grid(row=0, column=4, padx=10, pady=10)

        list = ["ID", "Nome", "CPF/CNPJ", "Data de Nascimento", "Endereço", "Contato"]

        for j in range(len(list)):
            label = Entry(self, width=27, fg='blue',
                          font=('Arial', 16, 'bold'))

            label.grid(row=0, column=j)
            label.insert(END, list[j])


        button = tk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        button.config(height=5, width=20)

        button.grid(row=2, column=3, padx=0, pady=0)




class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        value1 = tk.StringVar()
        value2 = tk.StringVar()
        value3 = tk.StringVar()
        value4 = tk.StringVar()
        value5 = tk.StringVar()
        value6 = tk.StringVar()

        ID = tk.StringVar()

        def check():
            if ID.get() == '0':
                label = tk.Label(self, text="Dados inválidos, não foi possível acessar funcionário", bg="black", fg="white",
                         wraplength=100)
                label.grid(row=11, column=1, padx=10, pady=30)
                self.after(5000, label.destroy)

            else:
                Preencher()

        def submit():
            id = value1.get()
            nome = value2.get()
            numero = value3.get()
            datanasc = value4.get()
            endereco = value5.get()
            contato = value6.get()

            # print("Seu ID é : " + id)
            # print("Seu nome é : " + nome)
            # print("Seu numero é : " + numero)
            # print("Sua data de nascimento é : " + datanasc)
            # print("Seu endereco é : " + endereco)
            # print("Seu contato é: " + contato)

            label = tk.Label(self, text="Dados inválidos, não foi possível atualizar funcionário", bg="black", fg="white",
                             wraplength=100)
            label.grid(row=11, column=1, padx=10, pady=30)
            self.after(5000, label.destroy)

            value1.set("")
            value2.set("")
            value3.set("")
            value4.set("")
            value5.set("")
            value6.set("")


        def Preencher():
            tk.Label(self, text="ID:", font=("Arial", 20)).grid(row=3, column=1)
            tk.Label(self, text="Nome:", font=("Arial", 20)).grid(row=4, column=1)
            tk.Label(self, text="CPF/CNPJ", font=("Arial", 20)).grid(row=5, column=1)
            tk.Label(self, text="Data de Nascimento", font=("Arial", 20)).grid(row=6, column=1)
            tk.Label(self, text="Endereço", font=("Arial", 20)).grid(row=7, column=1)
            tk.Label(self, text="Contato", font=("Arial", 20)).grid(row=8, column=1)

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

            button = tk.Button(self, text='Criar Funcionario', command=submit).grid(row=9, column=1)



        tk.Label(self, text="").grid(row=0, column=0, padx=340, pady=10)

        tk.Label(self, text="Id do funcionário a ser atualizado:", font=("Arial", 20)).grid(row=0, column=1, padx=10, pady=20)

        entry = tk.Entry(self, textvariable=ID).grid(row=1, column=1, padx=10, pady=20)

        button = tk.Button(self, text='Submeter Funcionário a ser atualizado', command=check).grid(row=2, column=1,
                                                                                                    padx=10, pady=20)

        buttonback = tk.Button(self, text="Startpage",
                               command=lambda: controller.show_frame(StartPage))

        buttonback.config(height=5, width=40)

        buttonback.grid(row=10, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()






# class Page(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 2", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)
#
#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="Page 1",
#                              command=lambda: controller.show_frame(Page1))
#
#         # putting the button in its place by
#         # using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)
#
#         # button to show frame 3 with text
#         # layout3
#         button2 = ttk.Button(self, text="Startpage",
#                              command=lambda: controller.show_frame(StartPage))
#
#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)





