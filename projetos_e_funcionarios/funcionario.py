class Funcionario:
    def __init__(self, id:int, nome:str, cargo:str):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.projetos = list()
    
    def listar_projetos(self):
        print("Projetos do funcionário ", self.__str__(),end="")
        
        if(not len(self.projetos)):
            print("Funcionário sem projetos")
            return
            
        for item in self.projetos:
            print(item.projeto)        
    
    def __str__(self):
        return f'{self.id} - {self.nome} - {self.cargo}\n'