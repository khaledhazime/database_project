import mysql.connector
from faker import Faker
import random

# Configuração de conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="faculdade"
)

cursor = db.cursor()

# Inicializa Faker
faker = Faker()

# Função para gerar números de telefone no formato correto
def gerar_telefone():
    return faker.phone_number()[:20]  # Ajustado para evitar problemas de truncamento

# Gerar e inserir dados para a tabela ALUNO
def insert_alunos(n):
    alunos = []
    for _ in range(n):
        matricula = faker.unique.random_int(min=10000, max=99999)
        nome = faker.name()
        endereco = faker.address()
        email = faker.email()
        data_nascimento = faker.date_of_birth(minimum_age=18, maximum_age=25)
        telefone = gerar_telefone()

        alunos.append((matricula, nome, endereco, email, data_nascimento, telefone))
        cursor.execute(
            "INSERT INTO ALUNO (matricula, nome, endereco, email, data_nascimento, telefone) VALUES (%s, %s, %s, %s, %s, %s)",
            (matricula, nome, endereco, email, data_nascimento, telefone)
        )
    db.commit()
    return alunos

# Gerar e inserir dados para a tabela PROFESSOR
def insert_professores(n):
    professores = []
    for _ in range(n):
        id = faker.unique.random_int(min=1000, max=9999)
        nome = faker.name()
        endereco = faker.address()
        email = faker.email()
        data_nascimento = faker.date_of_birth(minimum_age=30, maximum_age=65)
        telefone = gerar_telefone()

        professores.append((id, nome, endereco, email, data_nascimento, telefone))
        cursor.execute(
            "INSERT INTO PROFESSOR (id, nome, endereco, email, data_nascimento, telefone) VALUES (%s, %s, %s, %s, %s, %s)",
            (id, nome, endereco, email, data_nascimento, telefone)
        )
    db.commit()
    return professores

# Gerar e inserir dados para a tabela DEPARTAMENTO
def insert_departamentos(n, professores):
    departamentos = []
    for _ in range(n):
        id = faker.unique.random_int(min=1, max=100)
        nome = faker.word()
        chefe_id = random.choice(professores)[0]

        departamentos.append((id, nome, chefe_id))
        cursor.execute(
            "INSERT INTO DEPARTAMENTO (id, nome, chefe_id) VALUES (%s, %s, %s)",
            (id, nome, chefe_id)
        )
    db.commit()
    return departamentos

# Gerar e inserir dados para a tabela CURSO
def insert_cursos(n, departamentos):
    cursos = []
    for _ in range(n):
        codigo = faker.unique.random_int(min=100, max=999)
        nome = faker.word()
        departamento_id = random.choice(departamentos)[0]

        cursos.append((codigo, nome, departamento_id))
        cursor.execute(
            "INSERT INTO CURSO (codigo, nome, departamento_id) VALUES (%s, %s, %s)",
            (codigo, nome, departamento_id)
        )
    db.commit()
    return cursos

# Gerar e inserir dados para a tabela DISCIPLINA
def insert_disciplinas(n, cursos, professores):
    disciplinas = []
    for _ in range(n):
        codigo = faker.unique.random_int(min=1000, max=9999)
        nome = faker.word()
        curso_codigo = random.choice(cursos)[0]
        professor_id = random.choice(professores)[0]

        disciplinas.append((codigo, nome, curso_codigo, professor_id))
        cursor.execute(
            "INSERT INTO DISCIPLINA (codigo, nome, curso_codigo, professor_id) VALUES (%s, %s, %s, %s)",
            (codigo, nome, curso_codigo, professor_id)
        )
    db.commit()
    return disciplinas

# Gerar e inserir dados para a tabela MATRIZ_CURRICULAR
def insert_matriz_curricular(cursos, disciplinas_por_curso):
    matrizes = []
    id_counter = 1
    for curso_codigo in cursos:
        for disciplina_codigo in disciplinas_por_curso[curso_codigo]:
            semestre = faker.random_int(min=1, max=8)
            ano = faker.random_int(min=2018, max=2023)
            matrizes.append((id_counter, curso_codigo, disciplina_codigo, semestre, ano))
            cursor.execute(
                "INSERT INTO MATRIZ_CURRICULAR (id, curso_codigo, disciplina_codigo, semestre, ano) VALUES (%s, %s, %s, %s, %s)",
                (id_counter, curso_codigo, disciplina_codigo, semestre, ano)
            )
            id_counter += 1
    db.commit()
    return matrizes

# Gerar e inserir dados para a tabela HISTORICO_ALUNO
def insert_historico_aluno(alunos, disciplinas):
    historico = []
    id_counter = 1
    for aluno in alunos:
        aluno_matricula = aluno[0]
        disciplinas_cursadas = random.sample(disciplinas, k=random.randint(1, len(disciplinas)))
        for disciplina in disciplinas_cursadas:
            disciplina_codigo = disciplina[0]
            semestre = faker.random_int(min=1, max=8)
            ano = faker.random_int(min=2018, max=2023)
            nota_final = faker.random_int(min=0, max=10)
            historico.append((id_counter, aluno_matricula, disciplina_codigo, semestre, ano, nota_final))
            cursor.execute(
                "INSERT INTO HISTORICO_ALUNO (id, aluno_matricula, disciplina_codigo, semestre, ano, nota_final) VALUES (%s, %s, %s, %s, %s, %s)",
                (id_counter, aluno_matricula, disciplina_codigo, semestre, ano, nota_final)
            )
            id_counter += 1
    db.commit()
    return historico

# Gerar e inserir dados para a tabela GRUPO_TCC
def insert_grupo_tcc(alunos, professores):
    grupos = []
    for aluno in alunos:
        aluno_matricula = aluno[0]
        id = faker.unique.random_int(min=1, max=1000)
        professor_id = random.choice(professores)[0]

        grupos.append((id, aluno_matricula, professor_id))
        cursor.execute(
            "INSERT INTO GRUPO_TCC (id, aluno_matricula, professor_id) VALUES (%s, %s, %s)",
            (id, aluno_matricula, professor_id)
        )
    db.commit()
    return grupos

# Chamando as funções para inserir dados
alunos = insert_alunos(100)
professores = insert_professores(20)
departamentos = insert_departamentos(5, professores)
cursos = insert_cursos(10, departamentos)
disciplinas = insert_disciplinas(50, cursos, professores)

# Mapeando disciplinas para cursos
disciplinas_por_curso = {curso[0]: [] for curso in cursos}
for disciplina in disciplinas:
    curso_codigo = disciplina[2]  # Associando disciplina ao curso correto
    disciplinas_por_curso[curso_codigo].append(disciplina[0])

matrizes = insert_matriz_curricular([curso[0] for curso in cursos], disciplinas_por_curso)
historico = insert_historico_aluno(alunos, disciplinas)
grupos = insert_grupo_tcc(alunos, professores)

# Fechando conexão
cursor.close()
db.close()