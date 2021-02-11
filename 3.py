import yaml

data = {
    '1': ['a', 'b', 'c'],
    '2': 125,
    '3': {
        '100€': '8941₽',
        '100£': '10182₽'
    }
}

with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as yaml_file:
    check_file = yaml.load(yaml_file)

    if check_file == data:
        print('Ура, все получилось')
