# Caso RocketHub

Consulte apenas para o cliente ou como exemplo explicitamente solicitado. O estilo
reutilizavel esta em [Depoimentos de abertura](../estilos/depoimentos-abertura-live.md).

## Caso RocketHub: Aprendizado, Nao Preset Global

Contexto: montagem horizontal de depoimentos SAP para abertura de live. A revisao
V12 tem aproximadamente 4min11s, 1920x1080 a 30fps e 29 intervencoes visuais.
Esses numeros documentam o caso; nao sao metas para futuros videos.

Decisoes especificas solicitadas durante a revisao:

- Preservar cortes e mixagem aprovados nas revisoes apenas visuais.
- Primeiro plano aberto: esconder a barra presente na fonte com escala base e
  usar reenquadramentos pontuais, sem a barra reaparecer no zoom-out.
- Primeiro e segundo takes precisavam de limpeza; depois o refino fonetico
  individual foi solicitado para todos. Nao bastava repetir detector de silencio.
- Trilha desde o inicio e passagens continuas, sem parar uma musica para so depois
  iniciar outra. Blocos de proximidade, confianca, apoio, conquista e pertencimento
  orientaram automacao e selecao de trechos de uma mesma composicao.
- Destaques e diagramas laterais distribuidos pelas ideias do video, sem legenda
  continua. Aumentar cobertura depois do feedback, sem encher cada segundo.
- Fonte Geist; azul `#0759e6`, marinho `#07152c` e tons claros da identidade
  consultada no projeto. Revalidar identidade se o cliente a atualizar.
- Icones de uma familia, brancos sobre tile azul levemente arredondado. Sem
  card envolvendo titulo, texto e diagrama. Textos livres, com contraste por take.
- Cabecalho e destaque mais proximos, alinhamento comum e iniciais maiusculas;
  caixa-alta apenas em enfases selecionadas. Sem contornos inconsistentes.
- Gerar novas versoes MP4; CapCut somente quando solicitado explicitamente.
- Nos cortes verticais destinados a anuncio, reservar a faixa inferior para a
  descricao, controles nativos e botao de CTA. Recalcular a area segura para o
  enquadramento atual em vez de copiar coordenadas de outro projeto.

## Legenda dos Anuncios Verticais

Na revisao aprovada em 30/09/2026, a direcao gostou da linguagem, mas pediu mais
legibilidade. A nuvem azul ampla na base foi rejeitada por competir com a
mensagem. Mostrar a frase atual e uma previa menor da proxima tambem foi rejeitado:
em trocas de take, a previa entregava antes da hora uma fala de outro angulo.

A solucao aprovada manteve somente o cue atual, em uma linha quando a unidade de
sentido permitia, com `TASA Orbiter Bold` branca. Cada cue recebeu uma caixa
arredondada ajustada a sua largura, em azul forte `#004bcb` a 70% de opacidade,
em vez de scrim, nuvem ou tarja de largura total. No canvas 1080x1920 deste caso,
a implementacao usou aproximadamente 28px de respiro horizontal, 14px vertical,
raio 14px e eixo principal em y=1250, deixando 614px ate a base para a interface
e o CTA. Sao dados da V9, nao preset para outro canvas. O cue anterior permanece
durante pausas curtas ate a entrada do seguinte; nunca se antecipa o proximo.

Nos primeiros segundos, a legenda comum foi substituida por uma abertura cinetica
cue a cue ate o fechamento semantico do gancho. Inter Black e Anton alternaram
amarelo `#f7bb02` e branco, com entrada por escala/deslocamento e saida antes da
proxima unidade. Para sustentar contraste em fundos claros e escuros, a sombra
ficou mais opaca e difusa do que na primeira tentativa; a implementacao FFmpeg/PIL
usou alpha aproximado de 210-215/255, stroke 3px e blur 9px. Preserve o principio,
nao esses numeros, quando fonte, resolucao, editor ou enquadramento mudarem.

O ajuste inicial de referencia em 1080p aumentou tile de 84 para 112px, glifo de
54 para 76px e cabecalho de 34 para 38px, com destaque de 56px em um overlay de
560x480px. Sao coordenadas internas de um caso, nao tamanhos padrao de video.
O resultado precisa ser recomposto para outra fonte, enquadramento ou tela.

## O Que Nao Repetir

| Falha observada | Decisao que melhora o resultado |
| --- | --- |
| Cortar na borda textual da palavra | Conferir e preservar a cauda acustica |
| Overlap igual em tudo | Decidir cada emenda e restaurar continuidade quando couber |
| Inicio sem musica apesar do cue em zero | Conferir som efetivo, offset da fonte e fade |
| Trocas de trilha como parar/recomecar | Compor a passagem e validar ritmo e nivel |
| Poucos visuais concentrados no inicio | Mapear ideias e cobertura no video inteiro |
| Icone azul perdido no fundo | Tile somente no icone e glifo contrastante |
| Caixa envolvendo todo o conjunto | Remover painel; manter texto/diagrama livres |
| Palavras distribuidas numa largura fixa | Compor tipografia pelo tamanho real e proximidade |
| Nuvem ou tarja azul ocupando a base | Caixa local ajustada ao cue e testada sobre cada take |
| Proxima frase exibida antes da fala | Mostrar somente o cue atual, especialmente entre angulos |
| Caixa azul clara ainda sem contraste | Testar variante mais fechada da cor da marca e texto branco |
| Titulo inicial perdido no fundo | Reforcar opacidade e difusao da sombra sem criar contorno pesado |
| Um MP4 chamado de projeto editavel | Entregar fontes e camadas quando o editavel for pedido |

## Evidencia e Limites

O registro tecnico da V12 indica 7545 frames, decodificacao completa sem erros,
audio identico ao aprovado e draft CapCut inalterado. Houve inspecao de composicoes
e imagens finais. Isso nao prova uma nova escuta integral: o mapa musical registra
que nao houve escuta perceptiva direta nessa etapa. Preserve essa distincao.

A faixa documentada foi [Bring Me The Sky, de Scott Buckley](https://www.scottbuckley.com.au/library/bring-me-the-sky/),
com licenca CC BY 4.0 indicada na pagina do autor. E registro historico, nao
recomendacao automatica; ao reutilizar, confira termos e atribuicao exigida.
Hillier Smith foi indicado como referencia pelo usuario; nao atribua os procedimentos
deste caso a um video especifico dele sem verificar o material correspondente.

Este guia nao inclui videos, depoimentos privados, links de Drive, chaves de API,
credenciais, dados de infraestrutura nem copias de musica. Nao sao necessarios
para transferir o aprendizado editorial.
