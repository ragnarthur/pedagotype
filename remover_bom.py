# Caminho do arquivo JSON
file_path = '/home/arthuronrails/pedagotype/pedagotype/vercel.json'

# Leitura do arquivo com utf-8-sig para remover o BOM
with open(file_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Reescreve o arquivo sem o BOM
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("BOM removido com sucesso do arquivo vercel.json")
