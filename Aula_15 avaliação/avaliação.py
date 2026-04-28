print("Sistema de Gerenciamento de Notas de Alunos ")


total_alunos = int(input("Por favor informe quantos alunos deseja cadastrar."))

historico = []
contador_alunos = 0


while True:
   if contador_alunos == total_alunos:
      break
   
   nome = input("Por favor digite o nome do aluno: ")

   nota1 = float(input("Por favor digite a nota 1 (de 0 a 10): "))
   nota2 = float(input("Por favor digite a nota 2 (de 0 a 10): "))
   nota3 = float(input("Por favor digite a nota 3 (de 0 a 10): "))

   media = (nota1 + nota2 + nota3) / 3

   if media >= 7:
      situacao = "Aprovado"
    
   elif media >= 5: 
      situacao = "Recuperação"
    
   else:
      situacao = "Reprovado"

   dados_aluno = [nome,nota1,nota2,nota3,media,situacao]
   historico.append(dados_aluno)

   contador_alunos = contador_alunos + 1

print("\nBoletim da turma")
i = 0
while True:
   
   if i == total_alunos:
      break
      
   aluno_atual = historico[i]

   print("Nome:", aluno_atual[0])
   print("Média:", round(aluno_atual[4], 1))
   print("Situação:", aluno_atual[5])
   

   i = i + 1



   


   

    
   










