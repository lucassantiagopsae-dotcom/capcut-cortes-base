# CapCut Cortes Base

Skill neutra para corte tecnico/editorial no CapCut.

Ela guarda apenas a camada base de corte, sem regras especificas de cliente ou campanha:

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
```

## Instalar pelo GitHub

Depois que o repo estiver no GitHub:

```powershell
npx skills add https://github.com/SEU_USUARIO/capcut-cortes-base --skill capcut-cortes-base
```

## Atualizar

Quando um novo aprendizado de corte aparecer, atualize:

1. `capcut-cortes-base/SKILL.md` se for regra geral;
2. `capcut-cortes-base/references/` se for detalhe tecnico;
3. `capcut-cortes-base/evals/evals.json` se valer a pena testar o comportamento.

Se o aprendizado for de um projeto especifico, deixe na skill especifica daquele projeto e nao nesta base.
