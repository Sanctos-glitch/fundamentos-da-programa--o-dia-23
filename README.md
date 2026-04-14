# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

## input
Lembrando que o input é usado quando você quer mostrar certa coisa no TERMINAL.

## Tipos de dados em python
1. string
2. number inteiro
3. number float
4. boolean (que é true or false)

## Operadores matemáticos - básicos 
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão

## Operadores lógicos 
and -> e -> se duas condições forem verdadeiras, o resultado é verdadeiro.
or -> ou -> se pelo menos uma condição for verdadeira, o resultado é verdadeiro.
not -> Ele altera o valor booleano da condição.

## Métodos em python
1. print () -> Exibe informações no terminal(isso vai ser oq vai mostrar de fato as coisas determinadas no input lá no terminal, basicamente usando o print você executa as operações.)O que faz: Exibe textos, números ou o resultado de variáveis. 

2. input() -> Captura uma informação para levar ao terminal. (se vc quiser que algum comando relativo a perguntas de respostas funcionem, as perguntas vão orbigatoriamente levar isso pra aparecerem no terminal afim de serem respondidas no mesmo.) O que faz: Captura o que o usuário digitou e sempre entrega isso como uma string (str).

## Formas em python 
f(variavel) -> insere uma variavel dentro da string

# Estrutura de repetição
``if (se)`` -> Verifica se o uma condição é true (versadeira). Se for, ele executa o cídogo. 
``elif (senão se)`` -> é usado para testar várias condições. Ele só executa se todas as condições anteriores foram falsas.
``else`` (senão) -> executa o código se a condição for false (falsa).

# Laços de repetição
é um recurso de programação que permite executar um comjunto de comando varias vezes. Também são chamados de loop, laços de repetição ou iteração.

``FOR``-> Utilizamos quando sabemos quantas vezes queremos repetir algo 
sintax:
for variavel in range (inicio,fim)
    comandos
[range()] -> Método que aceita geração de números.
[inicio]-> é incusivo é o primeiro número a ser usado.
[fim]-> É exclusivo. O número utilizado é o anterior a esse

## Escopo das Variáveis
``Escopo Local`` -> A variavel só é acessada dentro da estrutura que ela foi criada.
``Escopo Global`` -> A variavel pode ser acessada por todo mundo.

## Varações das variaveis 
Variavel em memória -> É declarada quando você não prtene utilizar essa variavel em outros cenários. 
Variavel contadora ->  É utilizada para uma lógica onde a repetição ira ser alterada.

`WHILE` -> É utilizada quando não sabemos quantas veze so progrma vai repetir. Ele repete quando uam codnição for verdadeira.
Sintaxe:
while condição:
comandos



## Conversão de tipos em python
1. int () -> A gente vai incluir qual variável/dado que queremos converter para número inteiro.
2. float() ->  A gente vai incluir qual variável/dado que queremos converter para número decimal. 
3. str() ->  A gente vai incluir qual variável/dado que queremos converter para texto .

## boas práticas
1. Qualquer variável em python utiliza o padrão de case snake_case ou recentemente o cammelCase. 
2.  Se vpcê observar alguma estrutura tipo nome(), 90% de chance de ser uma função.
3. Python não tem constante, porém utilizamos o padrão case UPPERCASE, para simular aquela variavel não pode ser alterada.

