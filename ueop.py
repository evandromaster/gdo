import pandas as pd
import numpy as np
import gc, csv

def classifica_ueop(df_crimes):
    conds=[
    df_crimes['Município'].isin(['ABAETE','BIQUINHAS','BOM DESPACHO','CEDRO DO ABAETE','CORREGO DANTA',
		'DORES DO INDAIA','ESTRELA DO INDAIA','JAPARAIBA','LAGOA DA PRATA','LUZ','MARTINHO CAMPOS','MOEMA',
		'MORADA NOVA DE MINAS','PAINEIRAS','PEDRA DO INDAIA','POMPEU','QUARTEL GERAL','SANTO ANTONIO DO MONTE',
		'SERRA DA SAUDADE']),
    df_crimes['Município'].isin(['CARMO DO CAJURU','CLAUDIO','DIVINOPOLIS','ITATIAIUCU','ITAUNA','SAO GONCALO DO PARA']),
    df_crimes['Município'].isin(['ARAUJOS','CONCEICAO DO PARA','LEANDRO FERREIRA','NOVA SERRANA','PERDIGAO','PITANGUI']),
    df_crimes['Município'].isin(['ARCOS','BAMBUI','CAMACHO','CORREGO FUNDO','FORMIGA','IGUATAMA','ITAPECERICA','MEDEIROS','PAINS','PIMENTA','SAO SEBASTIAO DO OESTE','TAPIRAI']),
    df_crimes['Município'].isin(['IGARATINGA','MARAVILHAS','ONCA DO PITANGUI','PAPAGAIOS','PARA DE MINAS','PEQUI','SAO JOSE DA VARGINHA']),
]
res=['07º BPM','23º BPM','60º BPM','63º BPM','19ª CIA PM IND']
df_crimes['UEOP'] = np.select(conds,res,default='other')




