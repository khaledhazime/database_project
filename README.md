# Projeto: Sistema de Banco de Dados para Faculdade

**Integrantes do grupo:**
- Nome: Khaled Hazime Guimarães
- Matrícula: 24.124.091-4

---

## Descrição do Projeto
Este projeto consiste na criação de um sistema de banco de dados relacional para gerenciar as operações de uma faculdade, abrangendo informações sobre alunos, professores, cursos, departamentos, disciplinas e a matriz curricular dos cursos. O sistema permitirá a extração de diversos relatórios úteis para a gestão acadêmica.

## Diagrama Relacional

```mermaid
erDiagram
    ALUNO {
        int matricula
        string nome
        string endereco
        string email
        date data_nascimento
        string telefone
    }
    PROFESSOR {
        int id
        string nome
        string endereco
        string email
        date data_nascimento
        string telefone
    }
    CURSO {
        int codigo
        string nome
        int departamento_id
    }
    DEPARTAMENTO {
        int id
        string nome
        int chefe_id
    }
    DISCIPLINA {
        int codigo
        string nome
        int curso_codigo
        int professor_id
    }
    MATRIZ_CURRICULAR {
        int id
        int curso_codigo
        int disciplina_codigo
        int semestre
        int ano
    }
    HISTORICO_ALUNO {
        int id
        int aluno_matricula
        int disciplina_codigo
        int semestre
        int ano
        float nota_final
    }
    GRUPO_TCC {
        int id
        int aluno_matricula
        int professor_id
    }

    ALUNO ||--o{ HISTORICO_ALUNO : possui
    DISCIPLINA ||--o{ HISTORICO_ALUNO : cursada
    PROFESSOR ||--o{ DISCIPLINA : ministra
    CURSO ||--o{ DISCIPLINA : possui
    CURSO ||--o{ MATRIZ_CURRICULAR : possui
    DISCIPLINA ||--o{ MATRIZ_CURRICULAR : composta
    DEPARTAMENTO ||--o{ CURSO : possui
    PROFESSOR ||--o{ DEPARTAMENTO : chefia
    ALUNO ||--o{ GRUPO_TCC : participa
    PROFESSOR ||--o{ GRUPO_TCC : orienta
```

## Instruções para Executar o Código
1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o MySQL ou outro SGBD compatível instalado.
3. Crie um banco de dados chamado `faculdade`.
4. Execute o script `create_tables.sql` para criar todas as tabelas necessárias.
5. Execute o script `insert_data.py` para gerar e inserir dados aleatórios nas tabelas.
6. Utilize as queries disponíveis no arquivo `queries.sql` para gerar os relatórios desejados.