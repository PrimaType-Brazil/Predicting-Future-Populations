import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/primates_dataset.csv')

print(df.to_string)

df.dropna(inplace=True)

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
    plt.xticks(species_data['year']) 
    plt.yticks(species_data['population'])
    plt.tight_layout()
    
    plt.savefig(f'img/{species}_population_over_time.png')  # Salvar como imagem
    #plt.show()  

