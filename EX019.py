#Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça
#um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice
class1= input('Informe o nome do aluno:')
class2= input('Informe outro aluno:')
class3= input('Informe mais um aluno:')
class4= input('Informe o ultimo aluno:')
esco= choice([class1,class2,class3,class4])
print(f'O aluno escolhido é: {esco}')
