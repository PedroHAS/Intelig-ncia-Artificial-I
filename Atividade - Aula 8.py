%pip install spacy

!python -m spacy download  pt_core_news_sm

import spacy

nlp = spacy.load("pt_core_news_sm")

texto = "Quando Giovana Leite de Araújo, de 27 anos, fala que tem mais de 20 irmãos, todos ficam surpresos. O espanto só não é maior do que quando ela revela que foi trocada na maternidade quando tinha apenas horas de vida. Moradora de Curitiba, ela descobriu que não era filha biológica de seus pais quando tinha seis anos, depois que um representante do Conselho Tutelar foi em sua casa em Cascavel. Isso aconteceu porque outra família que teve bebê no mesmo dia e lugar procurava uma criança que foi trocada."

doc = nlp(texto)

for entidade in doc.ents:
  print(entidade.text, entidade.label_)