from main import *
from tkinter import messagebox

import Backend as core

app = None
selected = None

def clear_fields():
    app.entNome.delete(0, END)
    app.entSobrenome.delete(0, END)
    app.entEmail.delete(0, END)
    app.entCPF.delete(0, END)

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)


def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)


def insert_command():
    # Validar campos obrigatórios
    if not app.txtNome.get().strip():
        messagebox.showwarning("Aviso", "O campo Nome é obrigatório!")
        return

    if not app.txtCPF.get().strip():
        messagebox.showwarning("Aviso", "O campo CPF é obrigatório!")
        return

    # Validar CPF (11 dígitos)
    cpf = app.txtCPF.get().replace(".", "").replace("-", "").strip()
    if len(cpf) != 11 or not cpf.isdigit():
        messagebox.showerror("Erro", "CPF inválido! Digite exatamente 11 dígitos numéricos.")
        return

    # Validar email (se preenchido)
    email = app.txtEmail.get().strip()
    if email and "@" not in email:
        messagebox.showerror("Erro", "Email inválido! Deve conter @")
        return

    # Inserir no banco
    try:
        core.insert(app.txtNome.get(), app.txtSobrenome.get(), email, cpf)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        clear_fields()
        view_command()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {str(e)}")


def update_command():

    if not selected:
        messagebox.showwarning("Aviso", "Selecione um cliente na lista primeiro!")
        return

    # Mesmas validações do insert
    if not app.txtNome.get().strip():
        messagebox.showwarning("Aviso", "O campo Nome é obrigatório!")
        return

    if not app.txtCPF.get().strip():
        messagebox.showwarning("Aviso", "O campo CPF é obrigatório!")
        return

    cpf = app.txtCPF.get().replace(".", "").replace("-", "").strip()
    if len(cpf) != 11 or not cpf.isdigit():
        messagebox.showerror("Erro", "CPF inválido! Digite exatamente 11 dígitos numéricos.")
        return

    email = app.txtEmail.get().strip()
    if email and "@" not in email:
        messagebox.showerror("Erro", "Email inválido! Deve conter @")
        return

    # Atualizar
    try:
        core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), email, cpf)
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        view_command()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar cliente: {str(e)}")


def del_command():

    if not selected:
        messagebox.showwarning("Aviso", "Selecione um cliente na lista primeiro!")
        return

    # Confirmação antes de deletar
    resposta = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja realmente deletar o cliente:\n{selected[1]} {selected[2]}?"
    )

    if resposta:
        try:
            id = selected[0]
            core.delete(id)
            messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
            clear_fields()
            view_command()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar cliente: {str(e)}")


def getSelectRow(event):
    global selected

    # Verificar se algo foi selecionado
    if not app.listClientes.curselection():
        return

    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)

    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])

    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])

    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])

    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])

    return selected


if __name__ == "__main__":
    core.initDB()

    window = Tk()
    app = Gui(window)

    window.title("CRUD - Sistema de Cadastro")
    window.geometry("700x400")

    app.listClientes.bind('<<ListboxSelect>>', getSelectRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDell.configure(command=del_command)
    app.btnClose.configure(command=window.destroy)

    window.mainloop()