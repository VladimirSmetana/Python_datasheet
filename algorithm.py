import pandas as pd

# Вывести всю таблицу
data = pd.read_csv('table.csv', sep='\t')
print(data)

print('- FILTERING -')

# Выести строки без цены
df_filtered = data[data['price'].isna()]
print(df_filtered)

# Вывести только индексы
df_filtered = df_filtered[['Index']]
print(df_filtered)

print('- FILLING -')

# Заполнение пустых значений в столбце 'price'
for index, row in df_filtered.iterrows():
    # Находим верхнее и нижнее значение для текущей строки
    lower_value = data['price'].loc[:index].max()
    upper_value = data['price'].loc[index:].min()
    
    # Рассчитываем среднее значение
    if pd.notna(lower_value) and pd.notna(upper_value):
        average_value = (lower_value + upper_value) / 2
        data.at[index, 'price'] = average_value

# Вывод обновленной таблицы
print(data)