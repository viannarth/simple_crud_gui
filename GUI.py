# Program to make a simple
# login screen


import tkinter as tk

root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# root.configure(bg='#000080')

root.title("Catálogo de Prestadores de Serviço em Tecnologia da Informação (TI)")

tk.Label(root, text="\n\nInterface do Catálogo", font=("Comfortaa", 50)).pack()
tk.Label(root, text="\nSelecione a opção desejada\n", font=("Arial", 20)).pack()


def submit():
    root.destroy()

sub1 = tk.Button(root, text='Cadastrar Prestador de serviço', command=submit)
sub2 = tk.Button(root, text='Excluir Prestador de serviço', command=submit)
sub3 = tk.Button(root, text='Consultar Prestadores de serviço', command=submit)
sub4 = tk.Button(root, text='Atualizar Prestador de serviço', command=submit)

# placing the label and entry in
# the required position using grid
# method
#
# sub1.grid(row=0, column=5)
# sub2.grid(row=1, column=5)
# sub3.grid(row=2, column=5)
# sub4.grid(row=3, column=5)

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

# performing an infinite loop
# for the window to display
root.mainloop()