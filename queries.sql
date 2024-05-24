-- 1. Histórico escolar de qualquer aluno, retornando o código e nome da disciplina, semestre e ano que a disciplina foi cursada e nota final
SELECT 
    h.aluno_matricula, 
    a.nome AS aluno_nome, 
    h.disciplina_codigo, 
    d.nome AS disciplina_nome, 
    h.semestre, 
    h.ano, 
    h.nota_final
FROM 
    HISTORICO_ALUNO h
JOIN 
    ALUNO a ON h.aluno_matricula = a.matricula
JOIN 
    DISCIPLINA d ON h.disciplina_codigo = d.codigo
WHERE 
    h.aluno_matricula = 10082; -- Substitua 12345 pela matrícula do aluno desejado

-- 2. Histórico de disciplinas ministradas por qualquer professor, com semestre e ano
SELECT 
    p.id AS professor_id, 
    p.nome AS professor_nome, 
    d.codigo AS disciplina_codigo, 
    d.nome AS disciplina_nome, 
    m.semestre, 
    m.ano
FROM 
    DISCIPLINA d
JOIN 
    PROFESSOR p ON d.professor_id = p.id
JOIN 
    MATRIZ_CURRICULAR m ON d.codigo = m.disciplina_codigo
WHERE 
    p.id = 1068; -- Substitua 1001 pelo ID do professor desejado

-- 3. Listar alunos que já se formaram em um determinado semestre de um ano
SELECT 
    a.matricula, 
    a.nome
FROM 
    ALUNO a
WHERE 
    NOT EXISTS (
        SELECT 
            1
        FROM 
            MATRIZ_CURRICULAR mc
        LEFT JOIN 
            HISTORICO_ALUNO ha ON mc.disciplina_codigo = ha.disciplina_codigo AND ha.aluno_matricula = a.matricula
        WHERE 
            ha.nota_final IS NULL OR ha.nota_final < 5
            AND mc.semestre = 6
            AND mc.ano = 2023 -- Substitua o semestre e o ano desejado
    );

-- 4. Listar todos os professores que são chefes de departamento, junto com o nome do departamento
SELECT 
    p.id AS professor_id, 
    p.nome AS professor_nome, 
    d.id AS departamento_id, 
    d.nome AS departamento_nome
FROM 
    PROFESSOR p
JOIN 
    DEPARTAMENTO d ON p.id = d.chefe_id;

-- 5. Saber quais alunos formaram um grupo de TCC e qual professor foi o orientador
SELECT 
    g.id AS grupo_id, 
    a.matricula AS aluno_matricula, 
    a.nome AS aluno_nome, 
    p.id AS professor_id, 
    p.nome AS professor_nome
FROM 
    GRUPO_TCC g
JOIN 
    ALUNO a ON g.aluno_matricula = a.matricula
JOIN 
    PROFESSOR p ON g.professor_id = p.id;