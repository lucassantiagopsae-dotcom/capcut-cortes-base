# Metodo de Cortes Lucas Felix / Rugido

Use para trabalhos do Lucas Felix/Rugido independentemente de CapCut, Criado
ou FFmpeg. Este e o criterio editorial e de aparencia do cliente, nao um
formato de arquivo nem um editor obrigatorio. Para conceitos gerais, leia
[Cortes de live por tese](../estilos/cortes-live-por-tese.md); para extrair
ganchos, leia [Atlas e curadoria](../fluxos/gancho-atlas-e-curadoria.md).

## Construir o corte

Comece por um gancho que funcione para publico frio e mapeie a tese que ele
promete. Escolha, no material real, problema, mecanismo, prova ou exemplo e
menor fechamento que entregue a ideia. Preserve a cronologia da fala e as
pontes necessarias. Remova espera de chat, falso arranque, redundancia e
exemplo lateral sem amputar uma premissa. Duracao frequente de 1-2 minutos,
perto de 90 segundos, e referencia de planejamento. Para os cortes de live do
Lucas, 40 segundos e o minimo editorial aceitavel e a preferencia e ficar acima
de um minuto. Nao estenda com fala generica apenas para atingir duracao: o corte
precisa contextualizar a dor, desenvolver mecanismo, prova ou exemplo e deixar
uma nova chave para aquecer e conscientizar o publico. Se a fonte nao sustentar
isso, retire o candidato do lote. A tese fechada e o ritmo natural prevalecem.

Faca uma passada propria de cadencia depois da selecao do conteudo. Aproveite
pausas de baixa energia e sobreponha cauda/ataque de forma adaptativa, ouvindo
cada emenda para evitar silabas duplicadas ou mordidas. Nao converta toda pausa
em corte: respiracao e enfase podem sustentar credibilidade. Nao fixe quantidade
de microcortes nem duracao padrao de overlap.

Antes de liberar lote para Instagram, audite todos os MP4s finais com
`scripts/auditar_cadencia_reels.py`. Para a fala pausada do Lucas, baixa energia
interna a partir de `0.60 s` entra em revisao e a partir de `0.90 s` bloqueia a
entrega ate escuta ou correcao. A aceleracao em `1.15x` nao substitui a limpeza:
espera de chat, tempo olhando participantes e silencio entre raciocinios ainda
precisam de uma passada propria. Mantenha somente pausas que carreguem enfase.

Antes de fazer lote, compare tese e trechos-fonte entre os candidatos. O usuario
prefere variedade real; se varios compartilham corpo ou payoff, sinalize
alternativas e selecione menos videos. Cada video precisa de mapa proprio de
gancho, corpo, fechamento e source in/out para que ajustes e aprendizado sejam
reproduziveis.

## Aparencia e linguagem

No formato vertical das lives recentes, use canvas 1080x1920, live horizontal
inteira no centro sem esticar, titulo acima e legenda abaixo. O lote Aula
Segunda aprovado usou live em x=0, y=656, 1080x608 sobre preto. Confirme o
template e o enquadramento do projeto; essas coordenadas nao se impoem a toda
campanha.

O titulo visual e uma microtese, nao uma descricao neutra do assunto ou numero
do exemplo. Forme uma frase completa com contexto, tensao e consequencia que
o video realmente entrega. Use `Aveny T WEB`, branco, centralizado e proximo
ao video. Em canvas de 1080 px de largura, a caixa do titulo pode ocupar no
maximo 900 px. Use fonte entre 72 px e 88 px; nunca comprima ou amplie o bitmap
depois de renderizar para escapar dessa faixa.

Trate a quebra de linha como composicao, nao como resultado casual da largura.
Prefira duas linhas. Tres sao aceitaveis quando a copy realmente precisa;
quatro so em excecao, quando o texto for indispensavel e continuar forte.
Equilibre simultaneamente quantidade de palavras, quantidade de caracteres e
largura visual renderizada. Evite uma ultima linha curta, uma palavra orfa ou
uma silhueta triangular. Para corrigir, nesta ordem: procure uma quebra melhor,
aumente a fonte ate 88 px se houver espaco e ajuste a largura efetiva da caixa
sem ultrapassar 900 px. Se ainda exigir mais de quatro linhas, refine a copy em
vez de reduzir a fonte abaixo de 72 px. O primeiro render, alto demais, com
fonte incorreta e linhas mal distribuidas, foi rejeitado; ajuste pela referencia
humana, nao so por coordenadas.

Para o mecanismo de medicao, geracao de quebras e validacao, leia
[Titulos visuais balanceados](../tecnicas/titulos-visuais-balanceados.md). Neste
caso, `72-88 px`, `900 px` e `Aveny T WEB` formam o preset Rugido/Lucas; nao
transforme esses valores em regra de outra marca sem confirmar o template.

O feedback direto do Lucas em 23/09/2026 tornou a proximidade uma regra do
template vertical: nao deixe titulo e legenda flutuando no vazio preto. No canvas
1080x1920 com video entre y=656 e y=1264, ancore a base do titulo por volta de
y=620 e o topo da legenda por volta de y=1300, deixando aproximadamente 36 px
de respiro em cada lado. A regra e pela borda visual do texto, nao pelo centro
de caixas com alturas variaveis. Preserve as areas seguras da interface social.

Legenda na tela e diferente da copy da postagem. A legenda acompanha a fala,
em blocos de sentido e na area inferior; no padrao aprovado, amarelo, fonte
`TASA Orbiter Bold`, sem italico. Leia [Legendas do audio final](../fluxos/legendas-audio-final.md).
Copy de postagem e titulo de YouTube sao entregas opcionais conforme o pedido
e a regra local do projeto. Escreva a partir da tese, antagonista, mecanismo e
consequencia, sem promessa vazia nem CTA inventado. Guarde a correspondencia
exata entre ID do video, titulo visual, titulo de plataforma e copy.
Para o processo completo, leia [Copy de publicacao](../fluxos/copy-publicacao.md).
Na copy Rugido aprovada, prefira frase direta, mecanismo e fechamento em tese,
sem resumir a fala, hashtags automaticas ou tom de agencia. A referencia local
usa cerca de 80-140 palavras quando isso ajuda a ideia e usa "voce/seu/sua" na
publicacao salvo pedido em contrario; nao deixe uma contagem rigida empobrecer
o argumento. Consulte material de marca disponivel antes de inventar uma
"tese-mae" que o video nao sustenta.

## Evidencia e limites de reutilizacao

Na Aula Segunda de setembro de 2026, o usuario aprovou o resultado final e
avaliou os videos `SEG-C01` a `SEG-C05` como excelentes. O equilibrio aprovado
combinou gancho mapeado, tese completa, pausas limpas, overlaps pontuais,
titulo/copy refinados e legenda. Para aquela fala pausada, `1.15x` funcionou;
nao acelere todo video Lucas a 1.15x por automatismo. Houve correcao de titulo
alto/fraco e fonte antes da aprovacao. `SEG-C03` foi aprovado como video final,
mas pode funcionar como alternativa editorial no planejamento do feed;
`SEG-C07` e `SEG-C08` reaproveitam material e nao contam como ideias novas.

No lote, o MP4 final foi validado em 1080x1920, 24 fps, audio estereo 48 kHz
e decodificacao completa. Esses parametros sao referencia de entrega daquele
lote, nao autorizacao para mudar um projeto diferente. O historico de drafts
CapCut H001-H032 esta em [Caso CapCut](rugido-cortes-capcut.md); leia-o so
quando o projeto for CapCut ou aquele exemplo for relevante. No Criado, mantenha
timeline editavel e FFmpeg como render derivado. Em FFmpeg avulso, preserve
mapa, fonte e comandos reproduziveis sem prometer camadas editaveis.
