# Importando o módulo json para manipulação de dados JSON
import json

# Função para ler dados de um arquivo JSON
def read_json(file_name):
  with open(file_name, 'r') as file:
      data = json.load(file) # Carregando os dados do arquivo JSON
  return data # Retornando os dados carregados

# Função para escrever dados em um arquivo JSON
def write_json(file_name, data):
  with open(file_name, 'w') as file:
      json.dump(data, file) # Convertendo os dados Python em JSON e escrevendo no arquivo

# Função para criar um novo objeto em um arquivo JSON
def create(file_name, new_object):
   data = read_json(file_name) # Lendo os dados existentes do arquivo JSON
   data.append(new_object) # Adicionando o novo objeto aos dados
   write_json(file_name, data) # Escrevendo os dados atualizados de volta no arquivo JSON

# Função para ler dados de um arquivo JSON
def read(file_name):
   return read_json(file_name) # Lendo os dados do arquivo JSON

# Função para atualizar um objeto existente em um arquivo JSON
def update(file_name, index, updated_object):
   data = read_json(file_name) # Lendo os dados existentes do arquivo JSON
   data[index] = updated_object # Substituindo o objeto no índice especificado pelo objeto atualizado
   write_json(file_name, data) # Escrevendo os dados atualizados de volta no arquivo JSON

# Função para deletar um objeto de um arquivo JSON
def delete(file_name, index):
   data = read_json(file_name) # Lendo os dados existentes do arquivo JSON
   del data[index] # Deletando o objeto no índice especificado
   write_json(file_name, data) # Escrevendo os dados atualizados de volta no arquivo JSON

# Função para buscar objetos em um arquivo JSON que correspondem a um campo e valor específicos
def search(file_name, field, value):
  data = read_json(file_name) # Lendo os dados do arquivo JSON
  results = [] # Lista para armazenar os resultados da busca
  for obj in data:
      if obj[field] == value: # Se o objeto tem o campo e valor especificados
          results.append(obj) # Adiciona o objeto à lista de resultados
  return results # Retorna a lista de resultados

# Dados de exemplo para serem usados nos testes
data = [
  {"name": "John", "age": 30, "city": "Ouro Preto"},
  {"name": "Jane", "age": 40, "city": "Campinas"},
  {"name": "Mike", "age": 50, "city": "Curitiba"}
]

# Testando a função write_json
write_json('data.json', data) # Escrevendo os dados no arquivo 'data.json'

# Testando a função read
print(read('data.json')) # Imprimindo os dados lidos do arquivo 'data.json'

# Testando a função create
create('data.json', {"name": "Tom", "age": 60, "city": "São Paulo"}) # Adicionando um novo objeto ao arquivo 'data.json'

# Testando a função read novamente
print(read('data.json')) # Imprimindo os dados atualizados lidos do arquivo 'data.json'

# Testando a função update
update('data.json', 1, {"name": "Janet", "age": 54, "city": "Belo Horizonte" })
