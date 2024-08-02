estados = ['Rio Grande do norte','Rio Grande do Sul','Rio de janeiro','São Paulo','Goias','Minas Gerais','Piauí','Ceará ','Acre','Maranão','Tocantins','Mato Grosso do Sul','Distrito Federal','Santa Catariona','Parana','Amapá','Pará','Bahia','Sergipe','Espirito santo','Roraima', 'Rondonia','Pernambuco','Paraiba','Amazonas','Mato Grosso','Alagoas']

print(f'Quantida de estados no Brasil são:{len(estados)}. \n')

for i in range(len(estados)):
    print(f'{i+1}º Estado: {estados[i]}.')