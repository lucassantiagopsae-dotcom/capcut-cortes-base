---
name: edicao-video-ia
description: "Use para mapear ganchos, garimpar lives, montar/refinar cortes, legendar videos, criar titulos ou copy de postagem e incorporar aprendizados editoriais. Reune metodos gerais e Lucas Felix/Rugido, com CapCut e Criado como caminhos de edicao e FFmpeg como motor de render ou MP4 avulso. Nao imponha marca, formato, editor ou publicacao."
---

# Edicao de Video com IA

Transforme o material e o feedback em decisoes de montagem verificaveis. Nao
confunda aumentar a quantidade de efeitos com melhorar a narrativa. Preserve a
fala, a credibilidade e as camadas ja aprovadas fora do pedido atual.

## Escolher o Escopo

Identifique fontes, intervalos solicitados, versao aprovada, formato, destino,
identidade visual e entrega desejada. Consulte os arquivos antes de assumir que
o nome de um video identifica corretamente todas as pessoas que aparecem nele.

Separe quatro decisoes: objetivo editorial, metodo/cliente, editor de execucao
e entrega. CapCut e Criado sao dois caminhos validos de edicao, sem hierarquia
ou ordem temporal entre eles. FFmpeg e motor de processamento/renderizacao e
tambem pode gerar um MP4 diretamente quando nao se pede projeto editavel.
Nao aplique automaticamente a outro trabalho o estilo do
ultimo caso. Um pedido de contraste no icone nao autoriza criar um painel para
toda a composicao. Um pedido de musica nao autoriza recortar novamente a fala.

## Selecionar Modulos

Esta e a entrada geral. Os arquivos abaixo sao modulos internos, nao agentes nem
subskills automaticamente invocadas. Leia explicitamente apenas os necessarios.
Se o estilo nao estiver catalogado, derive a linguagem do briefing/referencia;
nao force o video para um estilo existente nem invente um preset aprovado.

Em pedido apenas tecnico, escolha diretamente a tecnica e o fluxo de entrega.
Quando houver direcao editorial, escolha tambem o estilo. Em pedido misto,
combine modulos compativeis e resolva conflitos pelo briefing atual.
Exemplos de combinacao: H001-H032 no CapCut pede metodo Lucas, historico
CapCut e fluxo CapCut; corte Lucas no Criado pede metodo Lucas e fluxo Criado;
legenda na tela mais copy de postagem pede audio final e metodo Lucas, mantendo
as duas entregas distintas.

### Estilos

- Montagem de prova social antes de live:
  [Depoimentos de abertura](references/estilos/depoimentos-abertura-live.md).
- Pessoa falando para camera com enfases e apoio visual:
  [Talking head com destaques](references/estilos/talking-head.md).
- Recorte de live/aula que precisa defender uma ideia com contexto e fechamento:
  [Cortes de live por tese](references/estilos/cortes-live-por-tese.md).

### Tecnicas Compartilhadas

- Limpeza, compactacao, cadencia, pontes e reajuste de clipes com overlap:
  [Limpeza e cadencia](references/tecnicas/limpeza-e-cadencia.md).
- Analise de referencia, limites de trechos e cortes naturais:
  [Referencia e montagem](references/tecnicas/referencia-e-montagem.md).
- Gravacoes simultaneas, sincronismo e escolha da camera pelo olhar:
  [Multicamera por direcao do olhar](references/tecnicas/multicamera-por-olhar.md).
- Escolha emocional da musica, transicoes e mixagem:
  [Direcao musical](references/tecnicas/direcao-musical.md).
- Textos de impacto, icones, animacao e enquadramento:
  [Motion e hierarquia](references/tecnicas/motion-e-hierarquia.md).
- Titulos visuais com quebra equilibrada, faixa tipografica e caixa maxima:
  [Titulos visuais balanceados](references/tecnicas/titulos-visuais-balanceados.md).
- Exportacao, preservacao do aprovado, editabilidade e evidencias de revisao:
  [Entrega e QA](references/fluxos/entrega-e-qa.md).

### Execucao e Editabilidade

- Garimpar ganchos em bruto, ranquear e mapear corpos antes da montagem:
  [Atlas e curadoria](references/fluxos/gancho-atlas-e-curadoria.md).
- Em bruto Lucas/Rugido, aplicar gates e calibracao da revisao humana:
  [Atlas Rugido avancado](references/fluxos/atlas-rugido-avancado.md).
- Em live longa, auditar cobertura, diversidade e cortes excedentes:
  [Curadoria de live longa](references/fluxos/curadoria-live-detalhada.md).
- Criar, corrigir ou exportar draft CapCut, incluindo compostos e espelhos:
  [CapCut editavel](references/fluxos/capcut-editavel.md).
- Projeto parametrico no Criado ou render derivado por FFmpeg:
  [Criado e FFmpeg editavel](references/fluxos/criado-ffmpeg-editavel.md).
- Ao operar projeto Criado via MCP/API ou validar um piloto:
  [Operacao no Criado](references/fluxos/criado-operacao-mcp.md).
- Legenda sincronizada ao audio realmente montado:
  [Legendas do audio final](references/fluxos/legendas-audio-final.md).
- Ao escrever texto para publicar, distinto da legenda na tela:
  [Copy e titulo de plataforma](references/fluxos/copy-publicacao.md).
- Analise local de baixa energia: `scripts/analisar_waveform_silencios.py`;
  leia uso e limites em [Limpeza e cadencia](references/tecnicas/limpeza-e-cadencia.md).

### Casos e Evolucao

- Somente ao trabalhar na RocketHub ou consultar aquele exemplo:
  [Caso RocketHub](references/casos/rockethub.md).
- Somente ao trabalhar na DD Prime ou consultar o anuncio imobiliario aprovado:
  [Caso DD Prime](references/casos/dd-prime-recrutamento-imobiliario.md).
- Exemplo aprovado de convite em duas cameras, pausas e sobreposicao fonetica:
  [Convite em duas cameras](references/casos/convite-duas-cameras.md).
- Exemplo aprovado de overlap adaptativo por juncao em um lote de reels:
  [Refinamento Ryan](references/casos/refinamento-ryan-overlap-adaptativo.md).
- Para Lucas Felix/Rugido em qualquer editor: [Metodo Lucas Felix](references/casos/rugido-lucas-felix.md).
- Apenas na execucao Rugido no CapCut ou ao consultar H001-H032:
  [Historico CapCut Rugido](references/casos/rugido-cortes-capcut.md).
- Quando o usuario pedir para ensinar um estilo ou incorporar feedback:
  [Evoluir a biblioteca](references/fluxos/evoluir-biblioteca.md).

As fontes foram condensadas por responsabilidade, sem exigir as skills antigas
instaladas para o fluxo editorial. Elas continuam preservadas como evidencia
e procedimentos detalhados, nao como regra concorrente. Para manutencao,
consulte [Inventario e integracao](references/fluxos/integracao-cortes.md).
Ferramentas/editor precisam estar disponiveis para executar, nao apenas documentados.

## Fluxo de Trabalho

1. Inspecione o trecho solicitado e os materiais locais existentes. Diferencie
   o que foi visto, ouvido, transcrito e apenas medido tecnicamente.
2. Se a tarefa for garimpar bruto, produza primeiro o atlas com fonte, tempos,
   tese e possibilidade real de construir cada corte. Quando o pedido for so
   mapear, pare para aprovacao; quando os ganchos ja estiverem aprovados ou o
   usuario pedir montagem direta, avance sem fingir uma aprovacao intermediaria.
   Montagem direta dispensa essa parada, nao os gates de autonomia, fidelidade,
   tese construivel e causalidade honesta; gancho nao votado nao vira aprovado.
3. Registre unidades de sentido, corpo e fechamento de cada corte, sem inventar
   resultados nem alterar a ordem fornecida sem autorizacao. Antes de um lote,
   compare tese e intervalos-fonte para evitar varias pecas quase identicas.
4. Estabilize a fala quando o escopo incluir cortes. Preserve ataque, cauda,
   respiracao expressiva e contexto. Atualize o mapa temporal apos o refino.
5. Quando houver musica no escopo, planeje-a sobre essa timeline: intencao, fonte, entradas, saidas,
   transicoes e automacao de volume. Nao escolha so pelo genero musical.
6. Planeje visuais por ideia: o que ajudam a entender, quando entram, por quanto
   tempo ficam e onde cabem sem cobrir a pessoa. Destaque nao e legenda continua.
7. Em mudanca ampla de linguagem, confira amostras representativas em movimento
   antes do render completo; depois procure o mesmo problema em todos os takes.
8. Exporte uma nova versao preservando fontes e aprovado. Confira o arquivo final,
   nao apenas as imagens geradas antes da composicao.

Esse fluxo nao obriga refazer etapas ja aprovadas. Em ajuste apenas visual,
reutilize cortes e audio final; em ajuste de trilha, mantenha o video aprovado.

## Contrato de Entrega

Preview, MP4 e projeto editavel sao entregas distintas. Preserve o editor escolhido;
nao migre para CapCut, Criado ou Remotion por preferencia propria. Quando o usuario
adiar o editavel, mantenha os dados necessarios, mas nao altere o draft a cada
revisao. Um MP4 importado inteiro nao equivale a entregar camadas editaveis.

Informe arquivo/versao entregue, o que mudou, o que foi preservado e limites reais
de verificacao. Nao certifique naturalidade por waveform, nem legibilidade por
dimensoes calculadas apenas. Consulte `evals/evals.json` ao evoluir esta skill para
revisar os cenarios de regressao; eles sao casos de teste, nao provas de execucao.
