# Edicao de Video com IA

Entrada geral: **`edicao-video-ia`**, antes chamada `edicao-audiovisual`.
Ela seleciona modulos de tecnica e estilo conforme o briefing, sem impor editor,
formato ou marca. O repositorio conserva o nome `capcut-cortes-base` para manter
seu historico e os enderecos existentes.

## Como se Organiza

Uma skill principal coordena os modulos internos e le apenas o necessario.
Modulos nao sao agentes nem skills com invocacao automatica: sao instrucoes
especializadas explicitamente ligadas pela entrada principal. Skills independentes
podem coexistir no repositorio; o motor `capcut-cortes-base` continua separado.

A estrutura usa referencias e carregamento progressivo descritos na
[documentacao oficial de skills](https://learn.chatgpt.com/docs/build-skills).
Um plugin e uma opcao futura para distribuir varias skills independentes, nao
uma dependencia desta biblioteca modular.

A skill de cortes guarda apenas a camada base, sem regras especificas de cliente ou campanha:

- sem duracao fixa;
- sem formato vertical obrigatorio;
- sem titulo;
- sem legenda;
- sem publicacao;
- sem identidade visual;
- sem regra de campanha.

O objetivo e servir como uma base reutilizavel para qualquer projeto, cliente ou formato.

## Motor de Cortes

Use `capcut-cortes-base` quando precisar:

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
edicao-video-ia/
  SKILL.md
  agents/openai.yaml
  references/
    tecnicas/
      referencia-e-montagem.md
      direcao-musical.md
      motion-e-hierarquia.md
    estilos/
      depoimentos-abertura-live.md
      talking-head.md
    casos/
      rockethub.md
    fluxos/
      entrega-e-qa.md
      evoluir-biblioteca.md
  evals/evals.json
```

## Instalar pelo GitHub

Instale a camada desejada, ou ambas:

```powershell
npx skills add https://github.com/lucassantiagopsae-dotcom/capcut-cortes-base --skill capcut-cortes-base
npx skills add https://github.com/lucassantiagopsae-dotcom/capcut-cortes-base --skill edicao-video-ia
```

Ao migrar do nome antigo, preserve eventuais mudancas locais e retire a copia
antiga da descoberta ativa para evitar duas versoes divergentes. A skill geral
funciona sozinha; a skill de cortes e um complemento para trabalho no CapCut.

Exemplos de uso:

- `Use $edicao-video-ia para editar estes depoimentos de abertura de live.`
- `Use $edicao-video-ia para destacar conceitos neste talking head.`
- `Registre na $edicao-video-ia o estilo que acabamos de aprovar neste projeto.`

## Ensinar Novos Estilos

Siga [Evoluir a biblioteca](edicao-video-ia/references/fluxos/evoluir-biblioteca.md):
classifique o aprendizado, atualize ou crie o modulo pertinente, conecte-o a
entrada geral e acrescente um cenario de regressao. Um novo estilo nao exige
reescrever as tecnicas compartilhadas. Nao crie estilos vazios ou ficticios.

Persistencia significa salvar conhecimento nos arquivos; conversar ou renderizar
um video nao treina automaticamente o modelo nem atualiza a skill sozinho.

## Atualizar o Motor de Cortes

Quando um novo aprendizado de corte aparecer, atualize:

1. `capcut-cortes-base/SKILL.md` se for regra geral;
2. `capcut-cortes-base/references/` se for detalhe tecnico;
3. `capcut-cortes-base/evals/evals.json` se valer a pena testar o comportamento.

Para trilha, animacao ou entrega audiovisual, atualize a referencia correspondente
em `edicao-video-ia/references/` e acrescente um cenario de regressao quando
necessario. Mantenha o `SKILL.md` como entrada curta, com leitura sob demanda.

O caso RocketHub fica separado do estilo de depoimentos e das tecnicas gerais.
Nao transforme sua paleta, duracao ou densidade de efeitos em
regra global. Nao inclua midias privadas, credenciais ou materiais licenciados no
repositorio. Os cenarios em `evals/` precisam ser executados para constituir
evidencia de comportamento; sua existencia sozinha nao valida uma edicao.
