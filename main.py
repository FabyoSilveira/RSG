class Materia:
    def __init__(self, _nome, _credito, _conceito):
        self.nome = _nome
        self.credito = _credito
        self.conceito = _conceito

condicao = 1
materias = []

while condicao: 
    
    condicao = input('Deseja cadastrar uma materia? SIM ou NAO\n')
    
    if condicao =='NAO' or condicao =='nao':
      break

    nome = input('Nome da sua materia: ')
    credito = eval(input('Horas da materia: '))
    conceito = input('Conceito alcancado: ')
    
    if conceito == "A" or conceito == "a":
      
        conceito = 5

    elif conceito == "B" or conceito == "b":

        conceito = 4

    elif conceito == "C" or conceito == "c":

        conceito = 3

    elif conceito == "D" or conceito == "d":

        conceito = 2

    elif conceito == "E" or conceito == "e":

        conceito = 1

    elif conceito == "F" or conceito == "f":

        conceito = 1

    else:
        print('Conceito invalido, programa passivel de resultados inconsistentes\n')
    
    if credito == 30:

        credito = 1

    elif credito == 60:

        credito = 2

    elif credito == 90:

        credito = 3

    else:
        print('Numero de creditos invalido, programa passivel de resultados inconsistentes\n')
    
    #instanciacao da classe(criacao de um objeto materia)
    _materia = Materia(nome, credito, conceito)
    #fim da instanciacao

    #adicionando o objeto no vetor de objetos materia
    materias.append(_materia)

#fim do while de cadastro


while condicao:
  
  i = 0;
  opcao = eval(input('Oque deseja fazer?\n 1 - Calcular RSG das materias\n 2 - Visualizar materias e pesos cadastrados\n 3 - Sair\n'))

  if opcao == 1:
    
    denominadorFormula = 0
    divisorFormula = 0
    while i < len(materias):
      conceito = materias[i].conceito
      credito = materias[i].credito
      multiplicacao = conceito*credito
      
      denominadorFormula += multiplicacao
      divisorFormula += credito
      i += 1

    rsg = denominadorFormula/divisorFormula
    print('Seu RSG final é', rsg)
    print('\n')

  if opcao == 2:
    
    while i < len(materias):
      print(materias[i].nome, '- Peso Credito:', materias[i].credito, ', Peso Conceito: ', materias[i].conceito)
      i += 1

  if opcao == 3:
    break

#fim do while de exibição