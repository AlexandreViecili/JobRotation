import json

with open('dados_faturamento.json') as f:
    dados = json.load(f)

faturamentoDiario = dados['faturamento_diario']
menorFat = min(faturamentoDiario)
maiorFat = max(faturamentoDiario)

diasComFat = [faturamento for faturamento in faturamentoDiario if faturamento > 0]
mediaMensal = sum(diasComFat) / len(diasComFat)
diasAcimaMedia = len([faturamento for faturamento in faturamentoDiario if faturamento > mediaMensal])

print(f"Menor faturamento diário: R$ {menorFat:.2f}")
print(f"Maior faturamento diário: R$ {maiorFat:.2f}")
print(f"Dias com faturamento acima da média mensal: {diasAcimaMedia}")
