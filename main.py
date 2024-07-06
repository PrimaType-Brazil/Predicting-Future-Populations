import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/primates_dataset.csv')

print(df.to_string)

# Remover linhas que contenham valores vazios em qualquer coluna
df.dropna(inplace=True)

# Garantir que a coluna 'population' seja do tipo inteiro
df['population'] = df['population'].astype(int)

# Garantir que a coluna 'year' seja do tipo inteiro
df['year'] = df['year'].astype(int)

# Obter a lista de espécies únicas
species_list = df['species_name'].unique()

# Criar um gráfico para cada espécie
for species in species_list:
    species_data = df[df['species_name'] == species]
    plt.figure(figsize=(10, 6))
    plt.plot(species_data['year'], species_data['population'], marker='o', linestyle='-')
    
    plt.title(f'População de {species} ao longo do tempo')
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.grid(True)
    plt.xticks(species_data['year'])  # Adicionar ticks no eixo x para cada ano
    plt.yticks(species_data['population'])  # Adicionar ticks no eixo y para cada valor de população
    plt.tight_layout()
    
    # Salvar o gráfico como imagem ou exibir
    plt.savefig(f'img/{species}_population_over_time.png')  # Salvar como imagem
    #plt.show()  # Exibir o gráfico

