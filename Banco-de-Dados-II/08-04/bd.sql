INSERT INTO `filmes` (
	titulo_original,
	titulo,
	duracao,
	ano_lancamento,
	cod_diretor,
	cod_genero
	) 
VALUES (
	'Piranhas do Caribe',
	'A maldição da jeba negra.',
	NULL,
	'2018',
	1,
	3
);
-- vingadores eu te meto
INSERT INTO `filmes` (
    titulo_original,
    titulo,
    duracao,
    ano_lancamento,
    cod_diretor,
    cod_genero
    )
VALUES (
    'Vingadores: Eu te mamo',
    'Vingadores: Eu te meto',
    NULL,
    '2022',
    5,
    6
);
-- Motoqueiro Xavasca
INSERT INTO `filmes` (
    titulo_original,
    titulo,
    duracao,
    ano_lancamento,
    cod_diretor,
    cod_genero
    )
VALUES (
    'Motoqueiro Xavasca',
    'Motoqueiro na Xavasca',
    NULL,
    '2016',
    22,
    2
);

-- filmes que foram lançados entre 2000 e 2005
SELECT * FROM filmes WHERE ano_lancamento BETWEEN 2000 AND 2005;

-- filmes que NÃO foram lançados entre 2000 e 2005
SELECT * FROM filmes WHERE ano_lancamento NOT BETWEEN 2000 AND 2005;

-- Exibe o titulo e o filme e o nome do respectivo diretor e respectivo genero
SELECT filmes.titulo, diretores.nome_diretor, generos.nome_genero
FROM filmes
INNER JOIN diretores ON filmes.cod_diretor = diretores.cod_diretor
INNER JOIN generos ON filmes.cod_genero = generos.cod_genero
ORDER BY filmes.titulo ASC;

-- Exibe o titulo do filme e o nome do respectivo director somente dos filmes de suspense
SELECT t.titulo, d.nome_director, g.nome_genero
    FROM filmes t, director d, generos g
    WHERE t.cod_director = d.cod_director
    AND t.cod_genero = g.cod_genero
    AND g.nome_genero = 'Suspense';

-- Exibe o filmes ordenados pelo ano de lançamento (mais antigo para mais novo)
SELECT * FROM filmes ORDER BY ano_lancamento;

-- Exibe o filmes ordenados pelo ano de lançamento (mais antigo para mais novo) removendo campos nulos ou vazios
SELECT * FROM filmes WHERE ano_lancamento IS NOT NULL ORDER BY ano_lancamento != '';

-- Exibe o filmes de suspense ou drama
SELECT f.titulo, g.nome_genero
    FROM filmes f, generos g
    WHERE f.cod_genero = g.cod_genero
    AND g.nome_genero IN ('Suspense', 'Drama');



