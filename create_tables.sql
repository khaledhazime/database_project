-- Tabela de Alunos
CREATE TABLE ALUNO (
    matricula INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    email VARCHAR(100),
    data_nascimento DATE,
    telefone VARCHAR(20)
);

-- Tabela de Professores
CREATE TABLE PROFESSOR (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    email VARCHAR(100),
    data_nascimento DATE,
    telefone VARCHAR(20)
);

-- Tabela de Departamentos
CREATE TABLE DEPARTAMENTO (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    chefe_id INT,
    FOREIGN KEY (chefe_id) REFERENCES PROFESSOR(id)
);

-- Tabela de Cursos
CREATE TABLE CURSO (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTO(id)
);

-- Tabela de Disciplinas
CREATE TABLE DISCIPLINA (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    curso_codigo INT,
    professor_id INT,
    FOREIGN KEY (curso_codigo) REFERENCES CURSO(codigo),
    FOREIGN KEY (professor_id) REFERENCES PROFESSOR(id)
);

-- Tabela de Matriz Curricular
CREATE TABLE MATRIZ_CURRICULAR (
    id INT PRIMARY KEY,
    curso_codigo INT,
    disciplina_codigo INT,
    semestre INT,
    ano INT,
    FOREIGN KEY (curso_codigo) REFERENCES CURSO(codigo),
    FOREIGN KEY (disciplina_codigo) REFERENCES DISCIPLINA(codigo)
);

-- Tabela de Histórico dos Alunos
CREATE TABLE HISTORICO_ALUNO (
    id INT PRIMARY KEY,
    aluno_matricula INT,
    disciplina_codigo INT,
    semestre INT,
    ano INT,
    nota_final FLOAT,
    FOREIGN KEY (aluno_matricula) REFERENCES ALUNO(matricula),
    FOREIGN KEY (disciplina_codigo) REFERENCES DISCIPLINA(codigo)
);

-- Tabela de Grupos de TCC
CREATE TABLE GRUPO_TCC (
    id INT PRIMARY KEY,
    aluno_matricula INT,
    professor_id INT,
    FOREIGN KEY (aluno_matricula) REFERENCES ALUNO(matricula),
    FOREIGN KEY (professor_id) REFERENCES PROFESSOR(id)
);