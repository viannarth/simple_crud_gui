from .controller import Controller


import tkinter as tk
from tkinter import *


LARGEFONT = ("Verdana", 35)

controller = Controller()

class App(tk.Tk):
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

        nome_val = tk.StringVar()
        cpf_cnpj_val = tk.StringVar()
        data_nascimento_val = tk.StringVar()
        contato_val = tk.StringVar()
        cep_val = tk.StringVar()
        rua_val = tk.StringVar()
        numero_val = tk.StringVar()
        complemento_val = tk.StringVar()
        bairro_val = tk.StringVar()
        cidade_val = tk.StringVar()
        uf_val = tk.StringVar()

        word = tk.StringVar()

        def verify_cpf_cnpj(var, index, mode):
            cpf_cnpj = cpf_cnpj_val.get()

            if not controller.validate_cpf_cnpj(cpf_cnpj):
                word.set("\tCPF/CNPJ inválido.")

            else:
                word.set("\tCPF/CNPJ válido.")

        def verify_data_nascimento(var, index, mode):
            data_nascimento = data_nascimento_val.get()

            if not controller.validate_data_nascimento(data_nascimento):
                word.set("\tData de nascimento inválida.")

            else:
                word.set("\tData de nascimento válida.")

        def verify_contato(var, index, mode):
            contato = contato_val.get()

            if not controller.validate_contato(contato):
                word.set("\tContato inválido.")

            else:
                word.set("\tContato válido.")

        def verify_cep(var, index, mode):
            cep = cep_val.get()

            if not controller.validate_cep(cep):
                word.set("\tCEP inválido.")
                return
            
            try: 
                address_data = controller.autocomplete_address(cep)
            except Exception as e:
                print("Could not verify CEP. Error:", e)
                word.set("\tNão foi possível verificar CEP.")
                return

            if address_data['valido'] == 'true':
                word.set("\tCEP válido.")
                address(address_data)

            else:
                word.set("\tCEP inválido.")
                rua_val.set("")
                numero_val.set("")
                complemento_val.set("")
                bairro_val.set("")
                cidade_val.set("")
                uf_val.set("")

        def address(address_data:dict[str, str]):
            tk.Label(self, text="Rua:", font=("Arial", 20)).grid(row=9, column=1)
            tk.Label(self, text="Número:", font=("Arial", 20)).grid(row=10, column=1)
            tk.Label(self, text="Complemento:", font=("Arial", 20)).grid(row=11, column=1)
            tk.Label(self, text="Bairro:", font=("Arial", 20)).grid(row=12, column=1)
            tk.Label(self, text="Cidade:", font=("Arial", 20)).grid(row=13, column=1)
            tk.Label(self, text="UF:", font=("Arial", 20)).grid(row=14, column=1)

            rua_val.set(address_data['rua'])
            complemento_val.set(address_data['complemento'])
            bairro_val.set(address_data['bairro'])
            cidade_val.set(address_data['cidade'])
            uf_val.set(address_data['uf'])

            entry7 = tk.Entry(self, textvariable=rua_val)
            entry8 = tk.Entry(self, textvariable=numero_val)
            entry9 = tk.Entry(self, textvariable=complemento_val)
            entry10 = tk.Entry(self, textvariable=bairro_val)
            entry11 = tk.Entry(self, textvariable=cidade_val)
            entry12 = tk.Entry(self, textvariable=uf_val)

            entry7.grid(row=9, column=2)
            entry8.grid(row=10, column=2)
            entry9.grid(row=11, column=2)
            entry10.grid(row=12, column=2)
            entry11.grid(row=13, column=2)
            entry12.grid(row=14, column=2)

        def submit():
            nome = nome_val.get()
            cpf_cnpj = cpf_cnpj_val.get()
            data_nascimento = data_nascimento_val.get()
            contato = contato_val.get()
            rua = rua_val.get()
            numero = numero_val.get()
            complemento = complemento_val.get()
            bairro = bairro_val.get()
            cidade = cidade_val.get()
            uf = uf_val.get()
            cep = cep_val.get()

            is_valid = True

            if nome == "" or not controller.validate_text(nome):
                is_valid = False
            if not controller.validate_cpf_cnpj(cpf_cnpj):
                is_valid = False
            if not controller.validate_data_nascimento(data_nascimento):
                is_valid = False
            if not controller.validate_contato(contato):
                is_valid = False
            if not controller.validate_cep(cep):
                is_valid = False
            if rua == "" or not controller.validate_text(rua):
                is_valid = False
            if numero == "" or not controller.validate_num(numero):
                is_valid = False
            if not controller.validate_text(complemento):
                is_valid = False
            if bairro == "" or not controller.validate_text(bairro):
                is_valid = False
            if cidade == "" or not controller.validate_text(cidade):
                is_valid = False
            if uf == "" or not controller.validate_text(uf):
                is_valid = False
            if not controller.validate_cep(cep):
                is_valid = False

            if not is_valid:
                label = tk.Label(self, text="Há algum campo inválido ou faltante.", bg="#d9d9d9", fg="#dc143c", wraplength=100)
                label.config(height=3, width=20)
                label.grid(row=20, column=1, padx=10, pady=10)
                self.after(5000, label.destroy)
                return
                   
            if complemento == "":
                complemento = None

            try:
                controller.insert_db(nome, data_nascimento, cpf_cnpj, contato, rua,
                numero, complemento, bairro, cidade, uf, cep)
            except Exception as e:
                print("Could not insert to database. Error:", e)
                label = tk.Label(self, text="Não foi possível adicionar ao banco de dados.", bg="#d9d9d9", fg="#dc143c", wraplength=100)
                label.config(height=3, width=20)
                label.grid(row=20, column=1, padx=10, pady=10)
                self.after(5000, label.destroy)
                return
            
            label = tk.Label(self, text="Funcionário criado com sucesso!", bg="#d9d9d9", fg="#dc143c", wraplength=100)
            label.config(height=3, width=20)
            label.grid(row=20, column=1, padx=10, pady=10)
            self.after(5000, label.destroy)

            nome_val.set("")
            cpf_cnpj_val.set("")
            data_nascimento_val.set("")
            contato_val.set("")
            cep_val.set("")
            rua_val.set("")
            numero_val.set("")
            complemento_val.set("")
            bairro_val.set("")
            cidade_val.set("")
            uf_val.set("")

        tk.Label(self, text="Nome:", font=("Arial", 20)).grid(row=4, column=1)
        tk.Label(self, text="CPF/CNPJ:", font=("Arial", 20)).grid(row=5, column=1)
        tk.Label(self, text="Data de Nascimento:", font=("Arial", 20)).grid(row=6, column=1)
        tk.Label(self, text="Contato:", font=("Arial", 20)).grid(row=7, column=1)
        tk.Label(self, text="CEP:", font=("Arial", 20)).grid(row=8, column=1)

        entry2 = tk.Entry(self, textvariable=nome_val)
        entry3 = tk.Entry(self, textvariable=cpf_cnpj_val)
        entry4 = tk.Entry(self, textvariable=data_nascimento_val)
        entry5 = tk.Entry(self, textvariable=contato_val)
        entry6 = tk.Entry(self, textvariable=cep_val)

        entry2.grid(row=4, column=2)
        entry3.grid(row=5, column=2)
        entry4.grid(row=6, column=2)
        entry5.grid(row=7, column=2)
        entry6.grid(row=8, column=2)

        cep_val.trace("w", verify_cep)
        data_nascimento_val.trace("w", verify_data_nascimento)
        contato_val.trace("w", verify_contato)
        cpf_cnpj_val.trace("w", verify_cpf_cnpj)

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

        id_val = tk.StringVar()

        def submit():
            id = id_val.get()

            if id == "" or not controller.validate_num(id):
                label = tk.Label(self, text="Digite um ID válido.", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)
                return

            id = int(id)

            try: 
                is_valid_id = controller.verify_id(id)
            except Exception as e:
                print("Could not verify ID in database. Error:", e)
                label = tk.Label(self, text="Erro. Não foi possível verificar ID.", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)
                return

            if not is_valid_id:
                label = tk.Label(self, text="ID inexistente na base de dados.", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)

            else:
                controller.delete_db(id)
                label = tk.Label(self, text="Funcionário excluído com sucesso!", bg="#d9d9d9", fg="#dc143c",
                                 wraplength=100)
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.after(5000, label.destroy)


        tk.Label(self, text="ID do funcionário a ser excluído:", font=("Arial", 20)).pack()

        entry = tk.Entry(self, textvariable=id_val).pack()

        button = tk.Button(self, text='Excluir Funcionário', command=submit).pack()

        buttonback = tk.Button(self, text="Página Inicial",
                               command=lambda: master.switch_frame(StartPage))

        buttonback.config(height=5, width=40)

        tk.Label(self, text="", height = 30).pack()

        buttonback.pack()


class ReadPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        try:
            rows = controller.read_db()
        except Exception as e:
            print("Could not read from the database. Error:", e)
            master.switch_frame(StartPage)
            return

        line = "-"
        line = 3*27*6*line

        header = ["ID", "Nome", "Data de Nascimento", "CPF/CNPJ", "Contato", "Endereço"]

        for j, column in enumerate(header):
            label = Entry(self, width=27, fg='blue', font=('Arial', 16, 'bold'), background="#7cfc00")
            label.grid(row=0, column=j)
            label.insert(END, column)

        i = 0
        for i, row in enumerate(rows):
            for j in range(len(header) - 1):
                label = Entry(self, width=27, fg='black',font=('Arial', 14), bg="#d9d9d9", borderwidth=0)
                label.grid(row=2*i+1, column=j)
                label.insert(END, row[j])

            address_str = ""
            for address_field in row[-7:]:
                if address_field is None:
                    continue

                address_str = "\n".join([address_str, address_field])


            text = tk.Text(self, height=8, width=40, background="#d9d9d9", borderwidth=0)
            text.grid(row=2*i+1, column=j+1, columnspan=1)
            text.insert(tk.END, address_str)

            tk.Label(self, text=line, height=1).grid(row=2*i + 2, column=0, columnspan=7)


        button = tk.Button(self, text="Página Inicial",
                             command=lambda: master.switch_frame(StartPage))

        button.config(height=5, width=20)

        button.grid(row=2*i+3, column=2, padx=0, pady=0, columnspan=2)


class UpdatePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        nome_val = tk.StringVar()
        cpf_cnpj_val = tk.StringVar()
        data_nascimento_val = tk.StringVar()
        contato_val = tk.StringVar()
        cep_val = tk.StringVar()
        rua_val = tk.StringVar()
        numero_val = tk.StringVar()
        complemento_val = tk.StringVar()
        bairro_val = tk.StringVar()
        cidade_val = tk.StringVar()
        uf_val = tk.StringVar()

        word = tk.StringVar()

        id_val = tk.StringVar()

        def verify_cpf_cnpj(var, index, mode):
            cpf_cnpj = cpf_cnpj_val.get()

            if not controller.validate_cpf_cnpj(cpf_cnpj):
                word.set("\tCPF/CNPJ inválido.")

            else:
                word.set("\tCPF/CNPJ válido.")

        def verify_data_nascimento(var, index, mode):
            data_nascimento = data_nascimento_val.get()

            if not controller.validate_data_nascimento(data_nascimento):
                word.set("\tData de nascimento inválida.")

            else:
                word.set("\tData de nascimento válida.")

        def verify_contato(var, index, mode):
            contato = contato_val.get()

            if not controller.validate_contato(contato):
                word.set("\tContato inválido.")

            else:
                word.set("\tContato válido.")

        def verify_cep(var, index, mode):
            cep = cep_val.get()

            if not controller.validate_cep(cep):
                word.set("\tCEP inválido.")
                return
            
            address_data = controller.autocomplete_address(cep)

            try: 
                address_data = controller.autocomplete_address(cep)
            except Exception as e:
                print("Could not verify CEP. Error:", e)
                word.set("\tNão foi possível verificar CEP.")
                return

            if address_data['valido'] == 'true':
                word.set("\tCEP válido.")
                address(address_data)

            else:
                word.set("\tCEP inválido.")
                rua_val.set("")
                numero_val.set("")
                complemento_val.set("")
                bairro_val.set("")
                cidade_val.set("")
                uf_val.set("")

        def check_id():
            id = id_val.get()

            if id == "" or not controller.validate_num(id):
                label = tk.Label(self, text="Digite um ID válido.", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.grid(row=21, column=1, padx=10, pady=30)
                self.after(5000, label.destroy)
                return

            id = int(id)

            try: 
                is_valid_id = controller.verify_id(id)
            except Exception as e:
                print("Could not verify ID in database. Error:", e)
                label = tk.Label(self, text="Erro: Não foi possível verificar ID.", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.grid(row=21, column=1, padx=10, pady=30)
                self.after(5000, label.destroy)
                return

            if not is_valid_id:
                label = tk.Label(self, text="ID inexistente na base de dados.", bg="#d9d9d9",
                                 fg="#dc143c", wraplength=100)
                label.grid(row=21, column=1, padx=10, pady=30)
                self.after(5000, label.destroy)

            else:
                preencher()

        def address(address_data:dict[str, str]):
            tk.Label(self, text="Rua:", font=("Arial", 20)).grid(row=9, column=1)
            tk.Label(self, text="Número:", font=("Arial", 20)).grid(row=10, column=1)
            tk.Label(self, text="Complemento:", font=("Arial", 20)).grid(row=11, column=1)
            tk.Label(self, text="Bairro:", font=("Arial", 20)).grid(row=12, column=1)
            tk.Label(self, text="Cidade:", font=("Arial", 20)).grid(row=13, column=1)
            tk.Label(self, text="UF:", font=("Arial", 20)).grid(row=14, column=1)

            rua_val.set(address_data['rua'])
            complemento_val.set(address_data['complemento'])
            bairro_val.set(address_data['bairro'])
            cidade_val.set(address_data['cidade'])
            uf_val.set(address_data['uf'])

            entry7 = tk.Entry(self, textvariable=rua_val)
            entry8 = tk.Entry(self, textvariable=numero_val)
            entry9 = tk.Entry(self, textvariable=complemento_val)
            entry10 = tk.Entry(self, textvariable=bairro_val)
            entry11 = tk.Entry(self, textvariable=cidade_val)
            entry12 = tk.Entry(self, textvariable=uf_val)

            entry7.grid(row=9, column=2)
            entry8.grid(row=10, column=2)
            entry9.grid(row=11, column=2)
            entry10.grid(row=12, column=2)
            entry11.grid(row=13, column=2)
            entry12.grid(row=14, column=2)
        
        def submit():
            id = int(id_val.get())
            nome = nome_val.get()
            cpf_cnpj = cpf_cnpj_val.get()
            data_nascimento = data_nascimento_val.get()
            contato = contato_val.get()
            rua = rua_val.get()
            numero = numero_val.get()
            complemento = complemento_val.get()
            bairro = bairro_val.get()
            cidade = cidade_val.get()
            uf = uf_val.get()
            cep = cep_val.get()

            is_valid = True

            if nome == "" or not controller.validate_text(nome):
                is_valid = False
            if not controller.validate_cpf_cnpj(cpf_cnpj):
                is_valid = False
            if not controller.validate_data_nascimento(data_nascimento):
                is_valid = False
            if not controller.validate_contato(contato):
                is_valid = False
            if not controller.validate_cep(cep):
                is_valid = False
            if rua == "" or not controller.validate_text(rua):
                is_valid = False
            if numero == "" or not controller.validate_num(numero):
                is_valid = False
            if not controller.validate_text(complemento):
                is_valid = False
            if bairro == "" or not controller.validate_text(bairro):
                is_valid = False
            if cidade == "" or not controller.validate_text(cidade):
                is_valid = False
            if uf == "" or not controller.validate_text(uf):
                is_valid = False
            if not controller.validate_cep(cep):
                is_valid = False

            if not is_valid:
                label = tk.Label(self, text="Há algum campo inválido ou faltante.", bg="#d9d9d9",
                             fg="#dc143c", wraplength=100)
                label.grid(row=20, column=1, padx=10, pady=30)
                self.after(5000, label.destroy)
                return
            
            if complemento == "":
                complemento = None

            try:
                controller.update_db(id, nome, data_nascimento, cpf_cnpj, contato,
                rua, numero, complemento, bairro, cidade, uf, cep)
            except Exception as e:
                print("Could not update the database. Error:", e)
                label = tk.Label(self, text="Não foi possível atualizar o banco de dados.", bg="#d9d9d9",
                                            fg="#dc143c", wraplength=100)
                label.grid(row=20, column=1, padx=10, pady=30)
                self.after(5000, label.destroy)

                return

            label = tk.Label(self, text="Funcionário atualizado com sucesso!", bg="#d9d9d9",
                             fg="#dc143c", wraplength=100)
            label.grid(row=20, column=1, padx=10, pady=30)
            self.after(5000, label.destroy)

            id_val.set("")
            nome_val.set("")
            cpf_cnpj_val.set("")
            data_nascimento_val.set("")
            contato_val.set("")
            cep_val.set("")
            rua_val.set("")
            numero_val.set("")
            complemento_val.set("")
            bairro_val.set("")
            cidade_val.set("")
            uf_val.set("")

        def preencher():
            id = int(id_val.get())

            try: 
                data_id = controller.read_id(id)
                nome_val.set(data_id[1])
                data_nascimento_val.set(data_id[2])
                cpf_cnpj_val.set(data_id[3])
                contato_val.set(data_id[4])
                cep_val.set(data_id[-1])
                numero_val.set(data_id[6])
                complemento_val.set(data_id[7])
            except Exception as e:
                print("Could not retrieve data with the ID from the database. Error:", e)
                nome_val.set("")
                data_nascimento_val.set("")
                cpf_cnpj_val.set("")
                contato_val.set("")
                cep_val.set("")
                numero_val.set("")
                complemento_val.set("")

            tk.Label(self, text="Nome:", font=("Arial", 20)).grid(row=4, column=1)
            tk.Label(self, text="Data de Nascimento:", font=("Arial", 20)).grid(row=5, column=1)
            tk.Label(self, text="CPF/CNPJ:", font=("Arial", 20)).grid(row=6, column=1)
            tk.Label(self, text="Contato:", font=("Arial", 20)).grid(row=7, column=1)
            tk.Label(self, text="CEP:", font=("Arial", 20)).grid(row=8, column=1)

            entry2 = tk.Entry(self, textvariable=nome_val)
            entry3 = tk.Entry(self, textvariable=cpf_cnpj_val)
            entry4 = tk.Entry(self, textvariable=data_nascimento_val)
            entry5 = tk.Entry(self, textvariable=contato_val)
            entry6 = tk.Entry(self, textvariable=cep_val)

            entry2.grid(row=4, column=2)
            entry3.grid(row=5, column=2)
            entry4.grid(row=6, column=2)
            entry5.grid(row=7, column=2)
            entry6.grid(row=8, column=2)

            tk.Button(self, text='Atualizar funcionario', command=submit).grid(row=17, column=1)

        cep_val.trace("w", verify_cep)
        data_nascimento_val.trace("w", verify_data_nascimento)
        contato_val.trace("w", verify_contato)
        cpf_cnpj_val.trace("w", verify_cpf_cnpj)

        tk.Label(self, text="ID do funcionário a ser atualizado:", font=("Arial", 20)).grid(row=0, column=1, padx=10, pady=20)

        tk.Label(self, textvariable= word, font=("Arial", 10)).grid(row=8, column=3)

        tk.Entry(self, textvariable=id_val).grid(row=1, column=1, padx=10, pady=20)

        tk.Button(self, text='Submeter funcionário a ser atualizado', command=check_id).grid(row=2, column=1,
                                                                                                    padx=10, pady=20)

        buttonback = tk.Button(self, text="Página Inicial",
                               command=lambda: master.switch_frame(StartPage))

        buttonback.config(height=5, width=40)

        buttonback.grid(row=18, column=1, padx=10, pady=10)


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()