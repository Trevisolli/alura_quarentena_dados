import pandas as pd
import matplotlib.pyplot as plt

# 1) Importa o repositório de dados dos filmes (CSV)
filmes = pd.read_csv("C:\\Cursos\\03 - PythonAlura\\movies.csv")
# 1.1) Estrutura do arquivo: Index(['movieId', 'title', 'genres'], dtype='object')
print(filmes.columns)
# Index(['movieId', 'title', 'genres'], dtype='object')
print(filmes.dtypes)
# movieId     int64
# title      object
# genres     object
# dtype: object

# 2) Como cada filme possui mais de uma categoria, na coluna "genero", faz o "split" dessa coluna,
#    transformando-a em linhas, para poder manipular e gerar os totalizadores necessários
categorias_stage = pd.DataFrame(filmes.genres.str.split('|').tolist(), index=filmes.movieId).stack().to_frame()
# 2.1) Atribui título à coluna
categorias_stage.columns = ["genre"]

# 3) Agrupa a série "categorias_stage" por genero
total_por_genero = categorias_stage.groupby("genre")["genre"].count()

# 4) Ordena por quantidade de filmes com a categoria, decrescente.
# 4.1) Filmes - Por quantidade de Categorias
total_por_genero_ordenado = total_por_genero.sort_values(ascending=False)
print("------------------------------------------------------------------------")
print("Listagem Decrescente da quantidade de Filmes, por Gênero [Decrescente]: ")
print("------------------------------------------------------------------------")

# 5) Imprime o Resultado do Desafio
print(total_por_genero_ordenado)

# 6) Amostra do resultado

#Listagem Decrescente da quantidade de Filmes, por Gênero [Decrescente]:
#------------------------------------------------------------------------
#genre
#Drama                 4361
#Comedy                3756
#Thriller              1894
#Action                1828
#Romance               1596
#Adventure             1263
#Crime                 1199
#... continua ...


# 7) Total de Gêneros
print("\n")
generos_distintos = (total_por_genero_ordenado.index)
print("\nGêneros Distintos: ",  generos_distintos)
total_de_generos_distintos = len(generos_distintos)
print("\nTotal de Gêneros Distintos: ",  total_de_generos_distintos)
#Plota Gêneros
plt.plot(generos_distintos)