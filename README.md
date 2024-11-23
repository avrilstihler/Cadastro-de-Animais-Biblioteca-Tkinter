Cadastro de Animais
Objetivo
Este código foi criado para cadastrar e exibir animais, incluindo informações de nome, idade, tipo (Cachorro ou Gato), e características específicas (Porte ou Raça). O programa é dividido em duas abas: Cadastro e Lista de Animais, e utiliza a biblioteca Tkinter para criar uma interface gráfica simples e intuitiva. O usuário pode cadastrar animais e visualizar a lista de forma organizada.

Estrutura e Funcionamento do Código
1. Classes Abstratas e Concretas
Classe Animal (Abstrata)
A classe Animal serve como a base para os outros tipos de animais. Ela contém atributos comuns a todos os animais, como o nome e a idade, e define métodos getter e setter para acessar e modificar esses atributos. O método mostrar() é abstrato, ou seja, cada classe filha (Cachorro e Gato) deve implementar esse método.

python
Copiar código
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
Classe Cachorro (Concreta)
A classe Cachorro herda de Animal e adiciona o atributo porte. O método mostrar() exibe as informações do animal de forma específica para cachorros, incluindo o porte.

python
Copiar código
class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte

    def mostrar(self):
        return f"Nome: {self.nome}\nTipo: Cachorro\nIdade: {self.idade} anos\nPorte: {self.porte}\n------------------------------"
Classe Gato (Concreta)
A classe Gato também herda de Animal e adiciona o atributo raça. O método mostrar() exibe as informações do animal de forma específica para gatos, incluindo a raça.

python
Copiar código
class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def mostrar(self):
        return f"Nome: {self.nome}\nTipo: Gato\nIdade: {self.idade} anos\nRaça: {self.raca}\n------------------------------"
2. Função main
A função main é onde o aplicativo Tkinter é configurado e a lógica de cadastro e exibição dos animais é gerida.

a. Função de Cadastro (cadastrar_animal)
O usuário preenche os campos de nome, idade e detalhe (que pode ser porte ou raça, dependendo do tipo de animal). Quando o botão Cadastrar é clicado, a função valida os campos e cria o objeto adequado (Cachorro ou Gato). O animal é então adicionado à lista de animais, e a função atualizar_lista é chamada para exibir a lista atualizada.

python
Copiar código
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

    animais.append(animal)  # Adiciona o animal à lista
    atualizar_lista()  # Atualiza a exibição na lista
    limpar_campos()  # Limpa os campos após o cadastro
    showinfo("Sucesso", f"{tipo} cadastrado com sucesso!")
b. Função de Atualização (atualizar_lista)
Esta função limpa a lista existente e exibe os animais cadastrados na interface gráfica. A função percorre todos os animais e chama o método mostrar() para exibir as informações formatadas.

python
Copiar código
def atualizar_lista():
    listbox.delete(0, END)  # Limpa a lista existente
    for animal in animais:
        listbox.insert(END, animal.mostrar())  # Adiciona cada animal à lista
c. Função de Limpeza (limpar_campos)
Após o cadastro de um animal, os campos de nome, idade e detalhe são limpos, permitindo o cadastro de outro animal sem a necessidade de apagar os dados manualmente.

python
Copiar código
def limpar_campos():
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_detalhe.delete(0, END)
3. Interface Gráfica (Tkinter)
A interface é dividida em duas abas usando o widget Notebook do Tkinter.

Aba de Cadastro:
Contém campos de texto para Nome, Idade e Porte/Raça.
Possui Radiobuttons para selecionar o tipo de animal (Cachorro ou Gato).
O botão Cadastrar chama a função cadastrar_animal para salvar os dados.
Aba de Lista de Animais:
Exibe os animais cadastrados em uma Text box.
Cada animal é mostrado em um formato estruturado, incluindo:
text
Copiar código
Nome: [Nome]
Tipo: [Tipo]
Idade: [Idade]
Porte/Raça: [Porte/Raça]
------------------------------
A lista é atualizada automaticamente sempre que um novo animal é cadastrado.

4. Widgets e Estilo
Label e Entry são usados para obter as informações do usuário.
Radiobuttons são usados para selecionar o tipo de animal (Cachorro ou Gato).
Button chama as funções para cadastrar o animal e atualizar a lista.
Text é utilizado para exibir a lista de animais cadastrados de forma formatada e legível.
O estilo visual foi configurado usando cores como roxo (#7E57C2) e cinza claro (#F5F5F5), proporcionando uma interface simples e agradável.
5. Comportamento do Aplicativo
Quando o usuário preenche o formulário e clica no botão Cadastrar, o animal é adicionado à lista e suas informações são exibidas na aba Lista de Animais.
A interface também permite a atualização da lista de animais, que é reinicializada e atualizada com as últimas informações cadastradas.
Mensagem de Erro: Caso o usuário deixe algum campo vazio ou insira dados inválidos, o programa exibirá uma mensagem de erro.
6. Persistência de Dados
Este programa não mantém persistência de dados após o fechamento da aplicação. Ou seja, ao reiniciar o programa, os dados cadastrados são perdidos.

Resumo
Este código implementa um sistema simples de cadastro de animais com a biblioteca Tkinter em Python. Ele permite que o usuário registre informações sobre cachorros e gatos e visualize esses dados em uma lista. As informações são exibidas de maneira organizada e a lista é atualizada sempre que um novo animal é cadastrado. O programa encerra quando a janela é fechada, e os dados são descartados ao reiniciar a aplicação.

Capturas de Tela
Tela de Cadastro de Animal (Adicione imagem da tela de cadastro)

Tela de Lista de Animais (Adicione imagem da tela com a lista de animais cadastrados)

Mensagens de Erro (Adicione imagem de mensagens de erro, caso os dados não sejam preenchidos corretamente)

Esse modelo de README já inclui explicações detalhadas sobre o funcionamento do código, o layout e a interação com o usuário, bem como os comportamentos esperados no caso de erros.
