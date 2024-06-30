import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame
df = pd.read_csv('./data/primates_dataset.csv')

# Visualizando o DataFrame
print(df)

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['health_status'], df['population'], color='blue')

plt.title('População vs Status de Saúde')
plt.xlabel('Status de Saúde')
plt.ylabel('População')

# Mostrar o gráfico
plt.show()