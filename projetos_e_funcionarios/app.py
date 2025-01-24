from projeto import Projeto
from funcionario import Funcionario

#testando o sistema
proj1 = Projeto(1, "Projeto 1", "Projeto de teste")
func1 = Funcionario(1, "João", "Analista")
func2 = Funcionario(2, "Maria", "Desenvolvedora")

proj1.adicionar_funcionario(func1, "Analista", "01/01/2020")
proj1.adicionar_funcionario(func2, "Desenvolvedora", "01/01/2020")

proj1.listar_funcionarios()
func1.listar_projetos()

proj1.remover_funcionario(func1)

proj1.listar_funcionarios()
func1.listar_projetos()