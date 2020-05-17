from datetime import datetime as dt
from math import trunc, floor

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def calculate_cost(start, end):
    inicio_diurno = 6
    fim_diurno = 22
    taxa_encargo = 0.36
    taxa_ligacao = 0.09

    start = dt.fromtimestamp(start)
    end = dt.fromtimestamp(end)

    if start.hour >= 22 or end.hour < 6:
        return taxa_encargo

    if start.hour >= fim_diurno:
        end = dt(end.year, end.month, end.day, fim_diurno)

    if start.hour < inicio_diurno:
        start = dt(start.year, start.month, start.day, inicio_diurno)

    duracao = ((end - start).seconds / 60)
    duracao = floor(duracao)

    estimated_cost = (duracao * taxa_ligacao) + taxa_encargo
    return estimated_cost


def classify_by_phone_number(records):
    resultados = []

    for record in records:
        flag = False

        for result in resultados:

            if result['source'] == record['source']:
                flag = True

                antigo = result['total']
                start = record['start']
                end = record['end']

                custo = calculate_cost(start, end)
                novo_total = round(antigo + custo, 2)

                result["total"] = novo_total

        if not flag:
            start = record['start']
            end = record['end']
            custo = round(calculate_cost(start, end),2)
            resultados.append({"source": record['source'], "total": custo})

    resultados = sorted(resultados, key=lambda r:r['total'], reverse=True)
    return resultados


print(classify_by_phone_number(records))
