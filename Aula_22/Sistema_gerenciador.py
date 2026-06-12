#Exercício 1

def calcular_media(nota1: float, nota2: float, nota3: float):

    for nota in [nota1, nota2, nota3]:
        if nota < 0 or nota > 10: 
            return -1.0
    
    return round((nota1 * 2 + nota2 * 3 + nota3 * 5) / 10, 1)

media = calcular_media(7.0, 8.0, 9.0)
print(f"Média: {media}")

media2 = calcular_media(5.0, 6.0, 4.0)
print(f"Média: {media2}")

invalida = calcular_media(5.0, 11.0, 8.0)
print(f"Média: {invalida}")

# exercicio 2

def verificar_situacao(media, verificar_honra=True):
    if media >= 7.0: 
        situacao = "Aprovado"

    elif media >= 5.0 and media < 7.0:
        situacao = "Recuperação"

    else:
        situacao = "Reprovado"

    mensagem_honra = ""

    if verificar_honra == True and media >= 9.0:
        mensagem_honra = "Menção Honrosa"

    return situacao, mensagem_honra
    
sit, honra = verificar_situacao(9.2)
print(f"{sit} {honra}")

sit2, honra2 = verificar_situacao(6.1)
print(f"{sit2} {honra2}")

sit3, honra3 = verificar_situacao(3.8, verificar_honra=False)
print(f"{sit3} {honra3}")

#exercicio 3

def emitir_boletim(nome: str, turma: str, nota1: float, nota2: float, nota3: float):

    media = calcular_media(nota1, nota2, nota3)
    situacao, honra = verificar_situacao(media)

    print("========================")
    print("🏫 COLÉGIO BYTE — BOLETIM")
    print("========================")
    print(f"Aluno   : {nome}")
    print(f"Turma   : {turma}")
    print(f"1º Bim  : {nota1}   2º Bim: {nota2}   3º Bim: {nota3}")
    print(f"1º Bim  : {nota1}   2º Bim: {nota2}   3º Bim: {nota3}")
    print("========================")
    print(f"Média   : {media}")
    print(f"Situação: {sit}  {honra}")
    print("========================")

emitir_boletim("Ana Lima", "3ºA", 9.0, 9.5, 9.8)
print()
emitir_boletim("Bruno Ramos", "3ºA", 5.0, 6.0, 5.5)

#exercicio 4

def calcular_media_turma(medias: list[float]) -> float:
    if len(medias) == 0:
        return 0.0
    
    soma = sum(medias)
    total = len(medias)

    return round(soma / total, 1)

def contar_situacoes(medias: list[float]) -> tuple[int, int, int]:
    aprovados = 0 
    recuperacao = 0
    reprovados = 0

    for m in medias:
        if m >=7.0:
            aprovados +=1
        
        elif m >= 5.0:
            recuperacao += 1
        
        else:
            reprovados += 1

    return aprovados, recuperacao, reprovados

def relatorio_turma(nome_turma: str, medias: list[float]) -> None:
    print(f"╔══════════════════════════════════╗")
    print(f"║   📊 RELATÓRIO DA TURMA — 3ºA   ║")
    print(f"╠══════════════════════════════════╣")

    if len(medias) == 0:
        print(" Nenhum aluno avaliado ainda.")
        return

    media_geral = calcular_media_turma(medias)
    maior = max(medias)
    menor = min(medias)
    aprov, rec, reprov = contar_situacoes(medias)
        
    print(f" Alunos avaliados : {len(medias)}")
    print(f" Média da turma   : {media_geral}")
    print(f" Maior média      : {maior}")
    print(f" Menor média      : {menor}")
    print(f"────────────────────────────────")
    print(f" Aprovados        : {aprov}")
    print(f" Recuperação      : {rec}")
    print(f" Reprovados       : {reprov}")


    medias_3a = [9.7, 7.2, 5.7, 8.1, 4.3, 6.5, 9.1, 3.8]
    relatorio_turma("3ºA", medias_3a)

    print()

    relatorio_turma("3ºB", [])

    #exercicio 5

def calcular_media_final(media_anterior: float, nota_final: float) -> float:

    nova_media = (media_anterior + nota_final) / 2
    return round(nova_media, 1)

def precisa_recuperacao(media: float) -> bool:

    if media >= 5.0 and media < 7.0:
        return True
    else:
        return False
    
def emitir_boletim_final(nome: str, turma: str, nota1: float,  nota2: float, nota3: float):

    media_ini = calcular_media(nota1, nota2, nota3)

    em_recuperacao = precisa_recuperacao(media_ini)

    if em_recuperacao and nota_final is not None:

        media_definitiva = calcular_media_final(media_ini, nota_final)

        if media_definitiva >= 5.0:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

    else:
        media_definitiva = media_ini

        situacao, honra = verificar_situacao(media_ini)

    # Aluno em recuperação que fez a prova final
    emitir_boletim_final(
        nome="Bruno Ramos",
        turma="3ºA",
        nota1=5.0,
        nota2=6.0,
        nota3=5.5,
    
    )
    print()
    # Aluno aprovado direto, sem recuperação
    emitir_boletim_final(
        nome="Ana Lima",
        turma="3ºA",
        nota1=9.0,
        nota2=9.5,
        nota3=9.8
    )












