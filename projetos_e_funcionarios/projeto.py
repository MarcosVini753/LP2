from funcionario import Funcionario
from funcionario_projeto import FuncionarioProjeto

class Projeto:

    def __init__(self, id:int, nome:str, descrição:str):
        self.id = id
        self.nome = nome
        self.descrição = descrição
        self.funcionarios = list()
    
    def adicionar_funcionario(self, func:Funcionario, papel:str, inicio:str):
        funcProj = FuncionarioProjeto(func, self, papel, inicio)
        self.funcionarios.append(funcProj)
        func.projetos.append(funcProj)
    
    def listar_funcionarios(self):
        print("Funcionários do projeto ", self.__str__(), end="")
        if(not len(self.funcionarios)):
            print("Projeto sem funcionários")
            return
        for item in self.funcionarios:
            print(item.funcionario)
    
    def remover_funcionario(self, func:Funcionario):
        for item in self.funcionarios:
            if item.funcionario == func:
                item.funcionario.projetos.remove(item)
                self.funcionarios.remove(item)
                return True
        else: return False

    def __str__(self):
        return f'{self.id} - {self.nome} - {self.descrição}\n'