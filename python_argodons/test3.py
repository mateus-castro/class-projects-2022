# estudo de JSON
import json

no_import={
    "nome": "mastro",
    "idade": "19"
}
print(no_import["nome"])


# ???????????????????????????????????/
with_import={
    "fruta": "maca",
    "preco": "19"
}

with_import_json=json.dumps(with_import)

print(with_import_json[1])