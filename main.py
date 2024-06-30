import pandas as pd
import matplotlib.pyplot as plt

# Criar um DataFrame a partir de um arquivo CSV
df = pd.read_csv('./data/primates_dataset.csv')

# Visualizar o DataFrame
print(df)

# Definir a ordem desejada das categorias de status de saúde
status_order = ['Healthy', 'Near Threatened', 'Vulnerable', 'Endangered', 'Critically Endangered']

df['health_status'] = pd.Categorical(df['health_status'], categories=status_order, ordered=True)

# Classificar o DataFrame pela coluna 'health_status'
df = df.sort_values('health_status')

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['health_status'], df['population'], color='blue')

plt.title('População vs Status de Saúde')
plt.xlabel('Status de Saúde')
plt.ylabel('População')

# Mostrar o gráfico
plt.show()
