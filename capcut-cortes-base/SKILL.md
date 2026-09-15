---
name: capcut-cortes-base
description: "Cria, ajusta e revisa cortes editaveis no CapCut com foco neutro em ritmo, limpeza de fala, waveform, gaps, microcortes em escadinha, overlaps foneticos, fades curtos e continuidade. Use sempre que o usuario pedir para cortar ou refinar um video no CapCut, corrigir pausas, gaguejos, entrada mordida, audio com tique, sobreposicao ruim, draft editavel ou mapa de corte para qualquer projeto, cliente, live, podcast, aula, video roteirizado ou video de YouTube. Nao define duracao, layout, formato vertical, legenda, titulo, nicho, estilo de marca ou publicacao; essas camadas devem vir do briefing ou de outra skill do projeto."
---

# CapCut Cortes Base

Esta skill e a camada tecnica de corte. Ela ensina como cortar bem no CapCut sem prender o trabalho a um cliente, formato, tempo, campanha, identidade visual ou plataforma.

Use esta skill como motor base. Outras skills podem definir o estilo editorial, a duracao, o layout, a legenda, o titulo, o destino e as regras do projeto.

## O que esta skill resolve

- limpar pausas, repeticoes, gaguejos, falsos arranques e erros de fala;
- transformar uma fala lenta ou travada em uma edicao mais fluida;
- usar waveform e timestamps para achar pontos reais de silencio ou baixa energia;
- fazer microcortes com overlap fonetico sem comer silaba;
- aplicar fade-in e fade-out curtos quando a emenda precisa suavizar;
- montar clipes em escadinha para facilitar revisao;
- proteger drafts editaveis no CapCut sem impor layout;
- documentar um mapa de corte para revisao humana.

## O que fica fora

Nao assuma por conta propria:

- duracao minima ou maxima;
- formato vertical, horizontal ou quadrado;
- posicao do video, titulo ou legenda;
- fonte, cor, tamanho, estilo visual ou identidade de marca;
- regra de gancho, tese, legenda, titulo ou copy;
- destino de publicacao;
- velocidade fixa;
- que todo video precisa virar short.

Se o usuario ou uma skill do projeto definir alguma dessas coisas, siga essa regra externa. Se nao definir, preserve o formato e a intencao do material original.

## Referencias

Leia apenas o que for relevante para o pedido:

- `references/audio-waveform-e-fonetica.md`: quando o trabalho envolver precisao de audio, pausas na wave, respiracao, silabas comidas, gaguejo, source duplicado ou fades.
- `references/refino-fonetico-por-emenda.md`: quando o usuario apontar caudas cortadas, overlap mecanico ou pedir o mesmo refino em todos os takes; inclui cobertura da revisao e verificacao de render/draft.
- `references/microcortes-e-continuidade.md`: quando for criar ou refinar a montagem, escolher onde cortar, limpar fala ou preservar naturalidade.
- `references/capcut-draft-editavel.md`: quando precisar editar ou criar draft no CapCut, mexer em JSON, organizar camadas, precompor ou evitar quebra da timeline.
- `references/exportacao-e-qa.md`: quando o usuario pedir MP4 final/exportacao ou quando for necessario conferir se o layout foi preservado.

Quando precisar detectar silencios tecnicamente, use ou adapte `scripts/analisar_waveform_silencios.py`.

## Entrada do trabalho

O usuario pode fornecer:

- video ou audio;
- transcricao com timestamps;
- draft CapCut existente;
- mapa de corte;
- feedback em print ou texto;
- briefing de cliente;
- criterio editorial vindo de outra skill;
- pedido amplo como "deixa esse video mais dinamico".

Se a tarefa exigir transcricao e ela nao existir, peça autorizacao antes de enviar audio/video para servicos externos. Se houver alternativa local disponivel, use-a quando fizer sentido.

## Workflow

### 1. Descobrir a intencao do corte

Antes de cortar, identifique o tipo de trabalho:

- `limpeza`: remover erros, pausas e gaguejos mantendo o mesmo conteudo;
- `compactacao`: encurtar mantendo a linha de raciocinio;
- `recorte`: extrair um trecho especifico de um material maior;
- `refino`: corrigir um draft que o usuario ja editou;
- `montagem`: criar um draft editavel com microcortes;
- `exportacao`: renderizar preservando o draft.

Nao use uma regra de tempo padrao. Pergunte ou derive do briefing. Para video roteirizado, o melhor corte pode preservar quase tudo. Para live, podcast ou aula, pode haver muito excesso a remover.

### 2. Separar conteudo de tecnica

O que cortar depende do objetivo editorial do projeto. A tecnica desta skill entra depois:

```text
objetivo do video
-> trechos que devem permanecer
-> sobras que devem sair
-> pontos de corte finos
-> overlap/fade
-> revisao auditiva
```

Nao invente narrativa nem reorganize a cronologia para "melhorar" o argumento. Voce pode remover trechos, mas a ordem final deve respeitar a ordem original, salvo pedido explicito do usuario.

### 3. Marcar candidatos de corte

Use transcricao e waveform juntos:

- a transcricao mostra o que foi falado;
- a waveform mostra onde a voz entra, termina, respira ou fica em silencio.

Marque candidatos para remover:

- pausas perceptiveis;
- repeticao sem valor novo;
- gaguejo e falso arranque;
- erro corrigido logo depois;
- frase incompleta que o proprio falante refaz melhor;
- respiro longo;
- silencio antes de uma fala util;
- trecho que abre outro assunto fora do objetivo.

Nao corte automaticamente toda baixa energia. Respiracao curta, pausa expressiva ou uma cauda natural de palavra podem ser parte da fluidez.

### 4. Ajustar bordas com margem fonetica

Nao corte exatamente no timestamp textual da palavra. A palavra costuma terminar no texto antes de terminar no som.

Como ponto de partida:

- deixe uma pequena folga antes da primeira palavra util;
- deixe cauda depois da ultima palavra para preservar vogal, ar e movimento de boca;
- em palavras curtas no ataque, use mais cuidado porque e facil morder a silaba;
- se a folga trouxer silencio longo, reduza ate perto do ataque real da voz;
- se a folga trouxer source duplicado do clipe anterior, ajuste a fronteira.

O ouvido manda mais que o numero. Se a emenda soa mordida, aumente a margem. Se soa arrastada, reduza a sobra.

Confira tambem o inicio e o encerramento de cada take. A duracao anterior do
corte nao e uma meta: recuperar uma terminacao pode aumentar o video. Para o
procedimento por emenda, leia `references/refino-fonetico-por-emenda.md`.

### 5. Fazer overlap como zona fonetica

Overlap nao e empilhar falas. E encaixar a cauda da fala anterior com o ataque da proxima.

Use overlap quando:

- removeu uma pausa entre duas falas;
- cortou um falso arranque;
- precisa mascarar uma emenda seca;
- quer simular continuidade natural.

Evite overlap quando:

- os dois clipes carregam a mesma frase;
- a fala original ja segue natural;
- o corte adiantaria uma palavra antes da hora;
- duas vozes ficariam brigando.

Se houver tique, bipe ou friccao audivel, procure primeiro source duplicado ou overlap cedo demais. Fade e recurso secundario, nao conserto para uma fronteira errada.

### 6. Usar fade curto so nos pontos sensiveis

Primeiro ajuste borda e overlap. Depois use fade quando a emenda ainda ficar dura.

Padrao pratico:

- fade-in curto no clipe que entra quando a primeira silaba entra seca;
- fade-out curto no clipe anterior quando a cauda foi cortada perto demais;
- fade-in + fade-out no mesmo microcorte quando ele fica entre duas emendas delicadas;
- use duracoes pequenas, medidas em poucos frames;
- trate cerca de 10 frames como teto comum, nao como alvo obrigatorio.

Confira no CapCut se o fade foi aplicado no segmento correto. Em alguns drafts, varios segmentos compartilham o mesmo material; nesses casos, isole o material antes de aplicar fade para nao espalhar o efeito.

### 7. Organizar em escadinha

Ao montar microcortes editaveis, organize os clipes em escadinha:

- cada novo clipe entra em outra faixa quando ha overlap;
- a sequencia visual deve mostrar onde as emendas acontecem;
- evite pingue-pongue mecanico de apenas duas faixas quando isso atrapalha leitura;
- ao bater limite de camadas, precomponha o bloco ja estabilizado e continue.

A escadinha ajuda o editor humano a revisar a logica do corte e mexer nas bordas sem se perder.

### 8. Trabalhar com drafts CapCut

Quando editar draft existente:

- confira se o projeto esta aberto/travado;
- preserve edicoes humanas;
- salve backup tecnico antes de mexer;
- edite em cima quando o usuario pediu ajuste no mesmo projeto;
- crie copia apenas se houver risco real de corromper ou se o usuario pedir;
- nao altere layout, canvas ou posicao de elementos sem pedido.

Quando houver muitos microcortes:

- mantenha a timeline principal simples;
- coloque microcortes dentro de composto quando isso proteger a montagem;
- desligue comportamentos de adsorcao/snap da faixa principal quando o campo existir e isso puder desmontar a edicao;
- mantenha compostos humanos quando eles expressam organizacao do trabalho.

### 9. Revisar antes de entregar

Faca uma passada final ouvindo as emendas principais:

- nenhuma primeira palavra deve entrar mordida;
- nenhuma ultima palavra deve terminar cortada;
- nao deve haver silencio longo sem intencao;
- nao deve haver duas copias da mesma frase se sobrepondo;
- nao deve haver tique forte causado por corte mal posicionado;
- o ritmo precisa parecer editado, mas nao atropelado;
- a cronologia precisa continuar compreensivel.

Se o usuario apontar um erro no CapCut por print ou timecode, corrija primeiro o problema especifico e depois procure o mesmo padrao no restante do video.

Em pedidos de refino de todos os takes, registre a revisao individual de cada
emenda, inclusive as mantidas ou desfeitas. Uma varredura de baixa energia nao
equivale a esse refino. Na entrega, diferencie o que foi ajustado, inspecionado
tecnicamente e ouvido; se nao houve escuta direta, declare essa limitacao.

## Mapa de corte

Quando o trabalho for complexo, salve um mapa em Markdown ou CSV com:

- tempo no original;
- tempo no draft;
- texto ou descricao do trecho;
- acao feita;
- motivo do corte;
- tipo de transicao;
- uso de overlap/fade;
- observacoes para o editor.

O mapa ajuda a transformar feedback humano em aprendizado sem misturar isso com regras de cliente.

## Checklist final

- [ ] Objetivo do corte identificado
- [ ] Sem regra de tempo/layout inventada
- [ ] Cronologia preservada
- [ ] Pausas perceptiveis analisadas pela waveform
- [ ] Gaguejos e falsos arranques removidos quando atrapalham
- [ ] Bordas com margem fonetica
- [ ] Sem silaba comida
- [ ] Sem fim de palavra cortado
- [ ] Sem source duplicado em overlap
- [ ] Overlaps encaixados na cauda/ataque
- [ ] Fades curtos somente onde ajudam
- [ ] Escadinha organizada quando ha microcortes
- [ ] Draft protegido sem alterar layout
- [ ] Backup tecnico salvo antes de editar draft
- [ ] QA auditivo feito
- [ ] Mapa de corte salvo quando necessario
