-- faca um left que mostre os filmes/shows/series de 2006 com seus diretores
SELECT * FROM filmes LEFT JOIN diretores ON filmes.cod_diretor = diretores.cod_diretor WHERE filmes.ano_lancamento = 2006;

-- Faca um left que mostre os filmes/shows/series que não possuem diretores
SELECT * FROM filmes LEFT JOIN diretores ON filmes.cod_diretor = diretores.cod_diretor WHERE filmes.cod_diretor IS NULL;

-- Faca um left que mostre todos os diretores que não possuem filmes
SELECT diretores.* FROM diretores LEFT JOIN filmes ON diretores.cod_diretor = filmes.cod_diretor WHERE filmes.cod_diretor IS NULL;