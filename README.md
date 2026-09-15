# Cortes Base e Edicao Audiovisual

Repositorio com duas skills complementares: `capcut-cortes-base` para corte
tecnico/editorial no CapCut e `edicao-audiovisual` para coordenar montagem,
trilha e motion graphics sem impor editor.

A skill de cortes guarda apenas a camada base, sem regras especificas de cliente ou campanha:

- sem duracao fixa;
- sem formato vertical obrigatorio;
- sem titulo;
- sem legenda;
- sem publicacao;
- sem identidade visual;
- sem regra de campanha.

O objetivo e servir como uma base reutilizavel para qualquer projeto, cliente ou formato.

## Nome da skill

`capcut-cortes-base`

## Quando usar

Use quando precisar:

- cortar e limpar fala no CapCut;
- remover pausas, gaguejos e falsos arranques;
- analisar waveform e gaps;
- ajustar entrada mordida ou fim de palavra cortado;
- montar microcortes em escadinha;
- fazer overlap fonetico;
- aplicar fade-in/fade-out curto;
- preservar draft editavel sem impor layout.

## Estrutura

```text
capcut-cortes-base/
  SKILL.md
  references/
  scripts/
  evals/
edicao-audiovisual/
  SKILL.md
  agents/openai.yaml
  references/
    referencia-e-montagem.md
    direcao-musical.md
    motion-e-hierarquia.md
    depoimentos-abertura-live.md
    entrega-e-qa.md
  evals/evals.json
```

## Instalar pelo GitHub

Instale a camada desejada, ou ambas:

```powershell
npx skills add https://github.com/lucassantiagopsae-dotcom/capcut-cortes-base --skill capcut-cortes-base
npx skills add https://github.com/lucassantiagopsae-dotcom/capcut-cortes-base --skill edicao-audiovisual
```

## Atualizar

Quando um novo aprendizado de corte aparecer, atualize:

1. `capcut-cortes-base/SKILL.md` se for regra geral;
2. `capcut-cortes-base/references/` se for detalhe tecnico;
3. `capcut-cortes-base/evals/evals.json` se valer a pena testar o comportamento.

Para trilha, animacao ou entrega audiovisual, atualize a referencia correspondente
em `edicao-audiovisual/references/` e acrescente um cenario de regressao quando
necessario. Mantenha o `SKILL.md` como entrada curta, com leitura sob demanda.

O guia de depoimentos contem o caso RocketHub identificado como exemplo, separado
dos fundamentos. Nao transforme sua paleta, duracao ou densidade de efeitos em
regra global. Nao inclua midias privadas, credenciais ou materiais licenciados no
repositorio. Os cenarios em `evals/` precisam ser executados para constituir
evidencia de comportamento; sua existencia sozinha nao valida uma edicao.
