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

3. lower() -> converte toda a string em minuscula.

4. upper() -> converte toda a string em maiuscula.

5. isdigit() -> Verifica se o valor contem numero.

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

## Funções em Python
`def` -> Define que uma função será declarada;
`propriedade` -> [valor] em memória que irá receber um argumento.
argumento-> Valor irá preencher o espaço da propriedade.

## Estruturas de Dados 
`list ou lista` -> Amazena valores avulsos e podem ser heterogênea ou homogênea, Ou seja, pode quardar valores de um memso tipo ou de diferentes tipos.
Ex: list = [] // Lista vazia
list - ["William", 25, 1.82]

`dict ou dicionario`-> Armazena conjuntos de valores (chave:valor). As chaves e valores podem ser heterogênea ou homogênea.
1. Para obter o valor de um conjunto em dict, você acessa pela chave.
Ex: dados_usuario = {} // Dicionário Vazio
dados_usuario = {"nome: "William", "cpf': 111456985-65, "idade": 25"}
dados_usuario´["nome"] => Devolve o valor, que "William".

## POO
1. python,todo molde é declarado atraves de uma classe => class
2. Qualquer caracteristica dentro de uma classe é chamade de atributo e são declaradas com variaveis.
3. As ações dentro de uma classe são chamadas de metodos e são declradas como [unções].

4. [sef] -> signifia ee mesmo, o atributo de classe atual.

5. [constructor] -> É a estrutura de comoa  classe será "copiada"


# precisamos criar um molde de uma pessoa. -> class
# caracteristicas -> atributos -> variaveis
# ações -> métodos -> funções
# metodo é uma função que esta dentro de uma classe

## Cases em python
Snake_case -> nome_aluno -> Nome de variaveis, metodos (funções) e arquivos.

cammelCase -> nomeAluno -> Nome variaveis, metodos (funções). Mais atual

PascalCase -> NomeAluno -> Classes

kebab-case -> nome-aluno -> não utiliamos em python.