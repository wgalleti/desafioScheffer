# Desafio técnico vaga Scheffer

Nesse desafio estará sendo analisado mais do que qualidade de objetividade de código, então, use a criatividade.

## Problema

Como nosso negócio é agro, o desafio não poderia ser diferente.

Vou propror um problema onde precisamos organizar e distribuir o fluxo de algodão colhido entre cinco fazendas dentro de duas algodoeiras e estimar o termino do beneficamento desses fardos.

### Dados das Fazendas

| Fazenda   | Fardões | Rolinhos |
| --------- | ------: | -------: |
| Fazenda 1 |   1.500 |   12.000 |
| Fazenda 2 |   3.000 |   17.000 |
| Fazenda 3 |     500 |    2.500 |
| Fazenda 4 |   5.000 |      300 |
| Fazenda 5 |   1.500 |   20.000 |

### Dados da Algodoeira

| Algodoeira   | Produção diária de Fardinhos |
| ------------ | ---------------------------: |
| Algodoeira 1 |                        1.200 |
| Algodoeira 2 |                          900 |

### Dados complementares

Uma informação importante é que quando uma fazenda colhe o algodão ela monta um fardão ou rolinho. Um fardão, pesa aproximadamente **11.000,00 Kgs** de algodão em caroço e um rolinho, pesa aproximadamente **2.700,00 Kgs** de algodão em caroço.

| Tipo    |      Peso |
| ------- | --------: |
| Fardão  | 11.000,00 |
| Rolinho |  2.700,00 |

> No agro, defimos como fardão e rolinho o algodão cru, ou algodão em caroço. Fardinho, é o algodão após ser beneficiado ou seja algodão em pluma.

Vamos levar em consideração que cada **Fardão** beneficiado ira gerar 22 fardihnos de pluma, e cada **Rolinho** beneficiado ira gerar 5 fardinhos de pluma

| Tipo    | Fardinhos produzidos |
| ------- | -------------------: |
| Fardão  |                   22 |
| Rolinho |                    5 |

### Objetivo do desafio

Criar uma aplicação web, onde eu possa informar as quantidades (parciais ou totais) de fardões ou rolinhos que serão beneficados em determinada algodoeira e calcular a data em que o mesmo irá terminar (calculando em dias, a partir da data de hoje), levando em consideração o limite de produção diária de cada beneficiadora.

## Extas

Serão levados em contas.

- Separação de responsabilidades (Backend, frontend, componentes)
- Documentação de uso (inclusa com desenvolvimento)
- Logs de execução
- Simplicidade

> Uma dica importante, se fossemos fazer internamente isso, iriamos utilizar o backend com python e django e o frontend com Vuejs. Se seguir essa stack conta um ponto a mais!

## Solução

https://scheffer.wgalleti.dev/
