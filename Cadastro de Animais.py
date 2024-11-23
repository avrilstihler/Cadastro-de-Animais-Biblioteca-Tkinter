from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from abc import ABC, abstractmethod

# Classe abstrata Animal
class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    @abstractmethod
    def mostrar(self):
        pass

# Classe concreta Cachorro
class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte

    def mostrar(self):
        return f"Nome: {self.nome}\nTipo: Cachorro\nIdade: {self.idade}\nPorte: {self.porte}\n{'-'*30}"

# Classe concreta Gato
class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def mostrar(self):
        return f"Nome: {self.nome}\nTipo: Gato\nIdade: {self.idade}\nRaça: {self.raca}\n{'-'*30}"

# Função principal
def main():
    # Lista para armazenar os animais cadastrados
    animais = []

    # Função para cadastrar o animal
    def cadastrar_animal():
        nome = entry_nome.get()
        idade = entry_idade.get()
        detalhe = entry_detalhe.get()
        tipo = tipo_animal.get()

        if not nome or not idade or not detalhe:
            showinfo("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            idade = int(idade)
        except ValueError:
            showinfo("Erro", "A idade deve ser um número!")
            return

        if tipo == "Cachorro":
            animal = Cachorro(nome, idade, detalhe)
        elif tipo == "Gato":
            animal = Gato(nome, idade, detalhe)
        else:
            showinfo("Erro", "Selecione o tipo de animal!")
            return

        animais.append(animal)
        atualizar_lista()
        limpar_campos()
        showinfo("Sucesso", f"{tipo} cadastrado com sucesso!")

    # Função para atualizar a lista
    def atualizar_lista():
        text_box.delete(1.0, END)  # Limpa o Text box
        for animal in animais:
            text_box.insert(END, animal.mostrar() + "\n")  # Adiciona cada animal com quebra de linha

    # Função para limpar os campos
    def limpar_campos():
        entry_nome.delete(0, END)
        entry_idade.delete(0, END)
        entry_detalhe.delete(0, END)
        tipo_animal.set("")

    # Configuração da janela principal
    root = Tk()
    root.title("Cadastro de Animais")
    root.geometry("400x380")  # Janela mais compacta
    root.resizable(False, False)

    # Criação de abas
    notebook = ttk.Notebook(root)
    tab_cadastro = Frame(notebook)
    tab_lista = Frame(notebook)
    notebook.add(tab_cadastro, text="Cadastro")
    notebook.add(tab_lista, text="Lista de Animais")
    notebook.pack(expand=True, fill=BOTH)

    # --- Aba Cadastro ---
    frame_cadastro = Frame(tab_cadastro, padx=15, pady=15)
    frame_cadastro.pack(fill=BOTH, expand=True)

    Label(frame_cadastro, text="Nome:", font=("Helvetica", 11)).grid(row=0, column=0, sticky=W, pady=5)
    entry_nome = Entry(frame_cadastro, font=("Helvetica", 11), width=25)
    entry_nome.grid(row=0, column=1, pady=5)

    Label(frame_cadastro, text="Idade:", font=("Helvetica", 11)).grid(row=1, column=0, sticky=W, pady=5)
    entry_idade = Entry(frame_cadastro, font=("Helvetica", 11), width=25)
    entry_idade.grid(row=1, column=1, pady=5)

    Label(frame_cadastro, text="Tipo de Animal:", font=("Helvetica", 11)).grid(row=2, column=0, sticky=W, pady=5)
    tipo_animal = StringVar(value="")
    Radiobutton(frame_cadastro, text="Cachorro", variable=tipo_animal, value="Cachorro", font=("Helvetica", 11)).grid(row=2, column=1, sticky=W)
    Radiobutton(frame_cadastro, text="Gato", variable=tipo_animal, value="Gato", font=("Helvetica", 11)).grid(row=3, column=1, sticky=W)

    Label(frame_cadastro, text="Porte/Raça:", font=("Helvetica", 11)).grid(row=4, column=0, sticky=W, pady=5)
    entry_detalhe = Entry(frame_cadastro, font=("Helvetica", 11), width=25)
    entry_detalhe.grid(row=4, column=1, pady=5)

    Button(frame_cadastro, text="Cadastrar", font=("Helvetica", 11), bg="#7E57C2", fg="white", command=cadastrar_animal).grid(row=5, column=0, columnspan=2, pady=15)

    # --- Aba Lista ---
    frame_lista = Frame(tab_lista, padx=15, pady=15)
    frame_lista.pack(fill=BOTH, expand=True)

    Label(frame_lista, text="Animais Cadastrados:", font=("Helvetica", 12, "bold")).pack(anchor=W, pady=5)
    
    # Usando um Text widget para exibir a lista de animais
    text_box = Text(frame_lista, font=("Helvetica", 11), height=10, width=50, wrap=WORD, padx=5, pady=5, bd=1, relief=SOLID, bg="#F5F5F5", fg="#7E57C2")
    text_box.pack(fill=BOTH, expand=True)

    # Botão de atualizar
    Button(frame_lista, text="Atualizar", font=("Helvetica", 11), bg="#7E57C2", fg="white", command=atualizar_lista).pack(pady=10)

    # Executar o aplicativo
    root.mainloop()

if __name__ == "__main__":
    main()
