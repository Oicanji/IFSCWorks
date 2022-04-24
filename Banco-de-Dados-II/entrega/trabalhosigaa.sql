-- Tarefa Sigaa - Banco de Dados II
-- Prof: Miguel Zarth
-- Aluno: Ignacio Sepulveda
-- Postado em https://github.com/Oicanji/IFSCWorks

-- 1. Exibir os filmes que possuam a palavra “amor” ou “love” no título ou título original.
SELECT * FROM filmes WHERE titulo LIKE '%amor%' OR titulo_original LIKE '%love%';

-- 2. Exibir os filmes cujo título é igual ao título original.
SELECT * FROM filmes WHERE titulo = titulo_original;

-- 3. Exibir o título e a a duração do filme mais longo.
SELECT titulo, duracao FROM filmes ORDER BY duracao DESC LIMIT 1;

-- 4. Exibir os filmes feitos pelo diretor Christopher Nolan.
SELECT * FROM filmes WHERE cod_diretor = (SELECT cod_diretor FROM diretores WHERE nome_diretor = 'Christopher Nolan');

-- 5. Exibir o título e o ano de lançamento dos 3 filmes mais recentes feitos pelo ator Brad Pitt.
SELECT titulo, ano_lancamento FROM filmes f, atores a, elenco e WHERE a.nome_ator="Brad Pitt" AND a.cod_ator=e.cod_ator AND e.cod_filme=f.cod_filme ORDER BY ano_lancamento DESC LIMIT 3;


-- 6. Exibir filmes curtos, entre 60 e 80 minutos.
SELECT * FROM filmes WHERE duracao BETWEEN 60 AND 80;

-- 7. Exibir os atores (sem repetição) de qualquer filme da série Harry Potter.
SELECT DISTINCT atores.nome_ator
FROM atores
INNER JOIN elenco ON elenco.cod_ator = atores.cod_ator
INNER JOIN filmes ON filmes.cod_filme = filmes.cod_filme
WHERE filmes.titulo_original LIKE '%Harry Potter%' or filmes.titulo LIKE '%Harry Potter%';


-- 8. Exibir os registros da tabela filmes que não contenham um diretor.
SELECT * FROM filmes WHERE cod_diretor IS NULL;

-- 9. Exibir a lista de diretores (sem repetição) que dirigiram algum filme entre 1990 e 1995 (incluindo 1990 e 1995).
SELECT DISTINCT diretores.nome_diretor FROM diretores, filmes WHERE diretores.cod_diretor = filmes.cod_diretor AND filmes.ano_lancamento BETWEEN 1990 AND 1995;

-- 10. Exibir os filmes de suspense feitos pelo ator Al Pacino.
SELECT * FROM filmes f, generos g, atores a, elenco e WHERE g.nome_genero="Suspense" and a.nome_ator="Al Pacino" and e.cod_ator=a.cod_ator and e.cod_filme=f.cod_filme;