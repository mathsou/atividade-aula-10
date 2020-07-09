import PySimpleGUI as gui
import mysql.connector

conn =  mysql.connector.connect(host = 'localhost', database = 'exercicio10', user ='root', password = '')

def gravar(nome, email, telefone):
    cursor = conn.cursor()
    query = "INSERT INTO usuario (nome, email, telefone) VALUES ("
    query+= " '" + str(nome) + "' , '" + str(email) + "' , '" + str(telefone) + "')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

class Usuario:
    def __init__(self, nome,email, telefone):
        self.__nome = self.setNome(nome)
        self.__email = self.setEmail(email)
        self.__telefone = self.setTelefone(telefone)

    def setNome(self, nome):
        if nome.isalpha():
            return nome
        return None

    def setEmail(self, email):
        if '@' in email:
            email1, email2 = email.split('@')
            if '.' in email2:
                return email
        return None
    
    def setTelefone(self, telefone):
        try:
            telefone = int(telefone)
            return telefone
        except:
            return None
    
    def getNome(self):
        return self.__nome
    
    def getEmail(self):
        return self.__email

    def getTelefone(self):
        return self.__telefone
    


class Tela:
    def __init__(self):
        layout = [
            [gui.Text('Nome'), gui.Input()],
            [gui.Text('email'), gui.Input()],
            [gui.Text('telefone'), gui.Input()],
            [gui.Button("Enviar")]
            ]
        self.tela = gui.Window("Usuário").layout(layout)

    def erro(self, erro):
        layoutErro = [[gui.Text(erro)], [gui.Button("Ok")]]
        telaErro = gui.Window("Usuário").layout(layoutErro)
        telaErro.Read()

    def show(self):
        self.button, self.values = self.tela.Read()
        if self.button in (None, 'Enviar'): 
            usuario = Usuario(self.values[0], self.values[1], self.values[2])
            if usuario.getNome():
                if usuario.getEmail():
                    if usuario.getTelefone():
                        gravar(usuario.getNome(), usuario.getEmail(), usuario.getTelefone())
                    else:
                        self.erro("Telefone inválido, apenas números")
                else:
                    self.erro("email inválido")
            else:
                self.erro("nome inválido, apenas letras")

tela = Tela()
tela.show()