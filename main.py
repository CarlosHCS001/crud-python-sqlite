from tkinter import *


class Gui():
    """Classe da Interface Grafica"""
    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self, window):
        self.window = window
        window.configure(bg='#f0f0f1')

        # Definição das variáveis
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # labels (podem ficar sem self.)
        lblnome = Label(window, text="Nome")
        lblsobrenome = Label(window, text="Sobrenome")
        lblemail = Label(window, text="Email")
        lblcpf = Label(window, text="CPF")

        # entries - COM self.
        self.entNome = Entry(window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(window, textvariable=self.txtCPF, width=self.width_entry)

        # Listbox e Scrollbar - COM self.
        self.listClientes = Listbox(window, width=100)
        self.scrollClientes = Scrollbar(window)

        # buttons - COM self.
        self.btnViewAll = Button(window, text="Ver todos")
        self.btnBuscar = Button(window, text="Buscar")
        self.btnInserir = Button(window, text="Inserir")
        self.btnUpdate = Button(window, text="Atualizar Selecionados")
        self.btnDell = Button(window, text="Deletar Selecionados")
        self.btnClose = Button(window, text="Fechar")

        # Posicionamento com Grid - ADICIONAR DE VOLTA!
        lblnome.grid(row=0, column=0)
        lblsobrenome.grid(row=1, column=0)
        lblemail.grid(row=2, column=0)
        lblcpf.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDell.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        # Configurar scrollbar - COM self.
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Aplicar estilos
        for child in window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        self.window.mainloop()


# Inicializar (PODE COMENTAR ESSA PARTE SE VAI RODAR PELO aplicacao.py)
if __name__ == '__main__':
    window = Tk()
    app = Gui(window)
    window.title("CRUD")
    window.geometry("700x400")
    app.run()