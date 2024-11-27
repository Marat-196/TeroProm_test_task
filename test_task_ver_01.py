import pandas as pd

df_1 = pd.read_excel('data/Список товаров.xlsx')
df_2 = pd.read_excel('data\Дерево категорий.xlsx')
for i in range(len(df_1)):
    df_1['Наименование'].loc[i] = df_1['Наименование'].str.split('.').loc[i][0]
df_1['tag'] = None
for i in range(len(df_1)):
    df_1['tag'].loc[i] = df_1['Наименование'].str.split()[i][0][:-1]

df_1['type'] = None

for i in range(len(df_1)):
    df_1['type'].loc[i] = ' '.join(
        str(df_2[df_2['Тип товара'].str.contains(df_1['tag'].loc[i], case=False)]['Тип товара'][:1]).split('\n')[
            0].split()[1:])

df_1['positive'] = df_1['Тип товара'] == df_1['type']

df_1.to_excel('completed_test_task_01.xlsx')
# with open('completed_test_task_01.xlsx', 'w') as f:
#     f.write(df_1)
