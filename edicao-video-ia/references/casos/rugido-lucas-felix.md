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
entrega ate escuta ou correcao. No template atual Lucas/Fase 1, a velocidade-base
e `1.18x`, salvo quando o usuario pedir outro valor para um video ou lote. O
`1.15x` foi uma calibracao especifica anterior e nao deve ser propagado como
padrao. A aceleracao nao substitui a limpeza: espera de chat, tempo olhando
participantes e silencio entre raciocinios ainda precisam de uma passada propria.
Mantenha somente pausas que carreguem enfase.

Antes de fazer lote, compare tese e trechos-fonte entre os candidatos. O usuario
prefere variedade real; se varios compartilham corpo ou payoff, sinalize
alternativas e selecione menos videos. Cada video precisa de mapa proprio de
gancho, corpo, fechamento e source in/out para que ajustes e aprendizado sejam
reproduziveis.

## Aparencia e linguagem

O usuario nomeia o formato atual como **videos da Fase 1**: uma fase de teste no
Instagram do Lucas. Nesse modelo especifico, use canvas 1080x1920, live horizontal
inteira no centro sem esticar, titulo acima e legenda abaixo. Essa composicao e
um template do Lucas/Fase 1, nao parte da inteligencia geral de cortes e nao deve
ser transferida automaticamente para outro cliente, feed ou fase. Tecnicas como
limpeza editorial, preservacao fonetica, leitura de waveform e controle de bico e
cauda continuam gerais e reutilizaveis independentemente desse layout. O lote Aula
Segunda aprovado usou live em x=0, y=656, 1080x608 sobre preto. Confirme o
template e o enquadramento do projeto; essas coordenadas nao se impoem a toda
campanha.

O titulo visual e uma microtese, nao uma descricao neutra do assunto ou numero
do exemplo. Forme uma frase completa com contexto, tensao e consequencia que
o video realmente entrega. Para Lucas, o titulo tambem precisa ter cara de
gancho dirigido ao publico, e nao de titulo de capitulo. Sempre que a tese
permitir, explicite para quem aquilo importa e a consequencia para essa pessoa,
empresa ou operacao. Nao basta nomear o conceito. O exemplo aprovado em
25/09/2026 foi `Nem o melhor vendedor salva sua empresa se a jornada comercial
for ruim`, em substituicao a `O melhor vendedor nao salva uma jornada ruim`.
Use o exemplo como criterio de intencao, nao como molde verbal obrigatorio.

No L21-C07, tambem em 25/09/2026, o usuario rejeitou `A taxa do vendedor
esconde a origem dos leads` e escolheu, entre as alternativas apresentadas,
`Sua taxa de conversao e decidida antes da reuniao`. A escolha reforca como
evidencia de marca a preferencia por uma microtese dirigida ao publico, com
consequencia clara e uma lacuna de curiosidade. Como o usuario respondeu apenas
`a primeira`, o motivo e inferido do contraste entre as copies, nao uma
justificativa verbal explicita nem uma formula obrigatoria para todo titulo.

No L21-C08, em 25/09/2026, o usuario aprovou o corte sem novo refino porque havia
poucas pausas e o video ja comecava com o Lucas falando, formando um gancho forte
desde o primeiro instante. Isso e evidencia de que, neste caso, entrada imediata
na fala e cadencia compacta pesaram mais do que aplicar microcortes adicionais.
O titulo visual ainda foi separado para uma nova rodada de refinamento; a
aprovacao da montagem nao implica aprovacao automatica da copy no topo.
Na rodada seguinte, o usuario preferiu manter temporariamente o titulo original
`Call fria ou meses de conteudo nao sao as unicas opcoes` em vez de adotar uma
das tres novas alternativas. Trate isso como decisao especifica do L21-C08, nao
como rejeicao geral ao uso de segunda pessoa nem como regra para outros cortes.

No L21-C09, em 25/09/2026, o usuario aprovou o video sem refino adicional e
destacou especialmente o inicio conciso, com poucas pausas. Somado ao caso
L21-C08, isso reforca como evidencia recorrente que o primeiro bloco deve entrar
rapido na ideia; ainda assim, a abertura precisa preservar naturalidade e
contexto, nao apenas minimizar silencio por medicao.

No L21-C10, em 25/09/2026, o usuario apontou que a sequencia de varias frases
curtas iniciadas por `tu` soava como uma rajada e que acelerar agravaria esse
efeito. A V2 removeu duas formulacoes semanticamente redundantes, mas deixou o
fragmento `Tu gera algumas` entre 9 e 11 segundos e por isso nao resolveu a
rajada apontada. A V3 removeu esse fragmento identificado pelo AssemblyAI, mas
tambem falhou: o transcritor agrupou ou omitiu uma vocalizacao alongada que o
usuario marcou na waveform como `Tu... tuuu...`, imediatamente antes do novo
ataque `Tu faz o teu cliente...`. A V4 removeu o bloco inteiro marcado entre
aproximadamente 9,00 e 9,97 s da V3, preservando pre-roll do ataque seguinte e
usando overlap curto; ela ainda depende de revisao auditiva humana. O caso e
evidencia de que cadencia nao e apenas reduzir pausas e que ASR nao valida
sozinho repeticoes foneticas: anotacao e audicao humanas prevalecem quando a
transcricao colapsa uma vocalizacao, e a verificacao deve cobrir exatamente a
janela citada, nao apenas o texto reconhecido.

No L21-C11, em 28/09/2026, o usuario corrigiu quatro problemas de cadencia no
mesmo corte. Pediu que o video comecasse na segunda ocorrencia de `Se eu faco
isso por meio de processo comercial`, eliminando o falso arranque repetido; que
a espera logo depois de `processo comercial` fosse fechada com sobreposicao de
cauda e ataque; que o aparte `So que, se liga no racional` fosse removido para
entrar diretamente em `Tu concorda comigo que`; e que a checagem de audiencia
`Fazendo sentido para voces? Voces estao entendendo?` saisse. No fechamento,
apontou ainda que `total` havia sido cortado antes da conclusao fonetica. A nova
versao preservou margem depois da palavra sem invadir o `Porque` do assunto
seguinte. O antes/depois reproduzivel esta no manifesto
`L21-C11.v2.timeline-diff.json` junto dos arquivos de producao do corte.

Somado aos casos L21-C08 e L21-C09, o L21-C11 confirma para a marca o padrao de
tratar o primeiro bloco com rigor maior de retencao: entrar diretamente na
formulacao valida, retirar repeticao e aparte evitavel e fechar espera artificial
com overlap fonetico adaptativo. Isso nao autoriza apagar toda pausa nem toda
pergunta ao publico. As remocoes de `se liga no racional` e da checagem de
audiencia sao evidencia deste corte; preserve-as em outros videos quando
cumprirem funcao real de contexto, enfase ou interacao. O mesmo rigor do ataque
vale na saida: compactacao nunca justifica entregar a ultima palavra mordida.

Na revisao imediatamente seguinte do L21-C11, o usuario identificou que a V2
ainda cortava a primeira ocorrencia mantida de `comercial`: a emenda havia sido
posicionada apenas 77 ms depois do fim indicado pelo ASR e o crossfade de 60 ms
comecava dentro dessa margem. Portanto, timestamp de palavra reconhecida nao e
fronteira fonetica segura. A V3 alongou a saida, mas continuou errada porque
tentou resolver a juncao com `acrossfade`: isso escolhia entre deixar um gap ou
atenuar/morder a cauda anterior, sem construir a escadinha descrita pelo editor.

O usuario confirmou entao como regra explicita que esta emenda exige duas
camadas simultaneas. Preserve o take inferior ate depois de `comercial`, incluindo
o vazio e a cauda naturais; posicione `eu tenho que fazer varias reunioes` em uma
camada superior com `inicio_proximo = fim_anterior - overlap`; e misture os dois
audios sem crossfade que abaixe automaticamente a fala anterior. O corte visual
pode ser seco no inicio do take superior, enquanto a cauda do audio inferior
continua por baixo. Encurtar a pausa e concatenar clipes nao produz esse efeito.
A V4 implementou essa estrutura com `amix normalize=0` e overlap bruto de 480 ms
nessa juncao especifica. Os 480 ms sao calibracao do caso, nao regra universal;
a regra promovida e preservar a palavra inteira e ajustar a sobreposicao pela
cauda e pelo ataque reais. O antes/depois reproduzivel esta em
`L21-C11.v4.timeline-diff.json`, e a naturalidade final permanece dependente da
escuta humana.

Na revisao seguinte do mesmo L21-C11, o usuario ampliou explicitamente essa
regra para o corte inteiro: toda pausa minimamente consideravel e comparavel a
primeira deve receber a mesma escadinha de cauda e ataque, porque esse tratamento
torna o video dinamico, rapido e fluido. A V5 varreu pausas internas e residuos
nas juncoes, dividiu os takes somente em vazios entre palavras e criou 21
sobreposicoes reais em camadas. A calibracao usou a duracao de cada vazio, sem
copiar os 480 ms da primeira emenda, e deixou o ataque seguinte entrar cerca de
60 ms antes do fim fonetico anterior. Uma segunda auditoria encontrou vales de
energia dentro de palavras longas; eles nao foram convertidos em cortes, pois
baixa energia dentro de um fonema nao equivale a pausa editavel. O limiar de
300 ms e a antecipacao de 60 ms sao parametros deste caso, nao constantes da
marca. A regra de marca e varrer o corte completo e aplicar overlap adaptativo
em toda pausa perceptivel que nao tenha funcao expressiva, preservando sempre
as palavras inteiras. O mapa reproduzivel esta em
`L21-C11.v5.timeline-diff.json`.

Depois de assistir a V5, o usuario aprovou o resultado como perfeito com
`Agora sim` e atribuiu diretamente a melhora a enxurrada de feedback acumulada.
Essa aprovacao confirma o conjunto, nao apenas a primeira emenda: varredura do
corte inteiro, overlap verdadeiro em camadas, calibracao por cauda e ataque,
preservacao fonetica e auditoria que distingue pausa entre falas de baixa energia
dentro de palavras. Em novos cortes Rugido/Lucas, consulte os casos anteriores e
cruze essas evidencias antes da primeira montagem; o objetivo operacional e
antecipar os ajustes recorrentes e aumentar a chance de aprovacao na primeira
revisao, sem transformar os parametros numericos deste caso em constantes.

Em 28/09/2026, ao pedir a revisao do lote seguinte (`L21-C16` a `L21-C20`),
o usuario reforcou como regra explicita que os cortes e overlaps devem preservar
o `bico` no inicio das frases. Trate o bico como o ataque acustico real do
primeiro fonema: mantenha pre-roll suficiente antes dele e nao posicione a
fronteira apenas no timestamp textual do ASR. A escadinha pode antecipar o novo
take sobre a cauda anterior, mas nunca as custas de amputar a consoante, vogal
ou transiente que faz a frase entrar inteira. Confirme essa margem na waveform
e, quando disponivel, pela escuta humana.

Em 28/09/2026, o usuario declarou que esse pacote aprovado deveria ser aplicado
proativamente aos quatro cortes restantes do lote, sem esperar que os mesmos
erros fossem apontados video por video. A montagem de `L21-C12` a `L21-C15`
removeu falsos arranques, repeticoes, apartes e checagens de audiencia sem funcao,
preservou teses completas e refez as emendas em camadas com overlap adaptativo.
Na auditoria, cinco pausas reais estavam escondidas dentro de tokens longos do
ASR (`pra`, `que`, `um` e `Tu`). Nesses casos, a waveform e o onset/offset
acustico prevaleceram sobre o timestamp textual: a palavra foi mantida no lado
em que era efetivamente pronunciada e apenas o silencio interno foi retirado.
Depois dessa correcao, os quatro arquivos passaram na varredura de cadencia a
`-35 dB`, sem spans de revisao de 600 ms nem bloqueios de 900 ms, e nenhuma
fronteira ficou dentro de palavra depois dos ajustes acusticos. Os mapas estao
em `L21-C12.v2.timeline-diff.json` a `L21-C15.v2.timeline-diff.json`. Esses
resultados tecnicos nao substituem a escuta humana: a naturalidade das quatro
versoes ainda precisa de aprovacao perceptiva do usuario.

O primeiro refino do `L21-C12` confirmou esse limite de forma negativa. A
auditoria a `-35 dB` declarou o arquivo sem pausas, mas o usuario o rejeitou como
`cheio de pausas`, sobretudo no inicio. Uma segunda leitura a `-30 dB`, com
janela minima de 150 ms, encontrou quinze vales no corte e seis nos primeiros
16 segundos; o maior tinha cerca de 605 ms. O ruído ambiente e a respiracao
mantinham energia suficiente para mascarar as pausas no limiar antigo, enquanto
o ASR absorvia varias delas dentro de tokens longos. Portanto, `pass` em
silencedetect nao prova fluidez. Cruze pelo menos waveform, distancia entre
ataques, contexto fonetico e revisao humana; quando o usuario disser que ha
pausa, trate o diagnostico tecnico anterior como falso negativo. O segundo
refino do C12 reposicionou os ataques em 30 camadas, reduziu o arquivo de 58,3 s
para 54,4 s e zerou vales de 150 ms ou mais a `-30 dB`, sem fronteiras dentro de
palavra apos a correcao acustica. Esse segundo resultado ainda depende da escuta
e aprovacao do usuario.

Na revisao imediatamente seguinte, o usuario rejeitou novamente o C12 porque a
montagem ainda nao havia aplicado a limpeza editorial ja ensinada: muletas,
fillers, falsos arranques e redundancias precisam ser avaliados antes da
waveform. A regra existia na fonte historica `cortes-de-live`, mas nao estava
explicita no checklist operacional de `edicao-video-ia`; confiar apenas nas
regras de overlap fez a execucao pular uma etapa. O terceiro refino removeu a
formulacao duplicada de `cumprir/assumir premissas`, a segunda repeticao de
`levar meses para consumir uma hora`, a repeticao `eu nao preciso de meses para
isso` e o qualificador `basicamente` sem funcao. So depois refez cadencia e
legendas. O corte passou de 54,4 s para 44,4 s, manteve as palavras originais na
ordem, nao deixou fronteiras dentro de palavra e nao apresentou vales de 150 ms
ou mais a `-30 dB`. A naturalidade e a selecao final continuam pendentes de
aprovacao humana.

Em 29/09/2026, o usuario rejeitou a abertura do `L21-C22` com
`O que que eu to fazendo aqui agora, turma?` porque o corte isolado nao mostra
o que estava sendo feito. A fonte confirma que a pergunta e um debrief do
exemplo anterior: no `L21-C21`, Lucas conduz o publico a concluir que pode
ensinar o cliente por saber mais sobre o problema; depois de um participante
dizer que a fala destravou um medo, Lucas nomeia o mecanismo como
`construindo viabilidade`. Portanto, o inicio do C22 depende do contexto do
C21. Registre este caso como evidencia que reforca o gancho autonomo para
publico frio: pergunta metalinguistica ou referencia como `isso`, `aqui` e
`o que eu estou fazendo` so pode abrir o corte quando o referente estiver
claro no proprio video. Se a pergunta for mantida como gancho, o corpo precisa
recuperar a premissa anterior; outra opcao e abrir por uma proposicao
autossuficiente da propria fonte. Nao presuma que o espectador viu o corte
anterior.

Na revisao seguinte do mesmo `L21-C22`, o usuario corrigiu o fechamento da
montagem: depois de `cara, nao e pra mim. Eu nao consigo.`, a fala `Outra
objecao.` nao deveria permanecer. A V3 preservou a cauda completa de `consigo`
e terminou antes da ponte seguinte. Isto e evidencia do caso, nao regra para
apagar toda frase metalinguistica no fim: quando o payoff ja fecha a tese, confira
se uma rotulacao como `outra objecao` apenas anuncia o proximo raciocinio e, se
for assim, deixe-a para o bloco seguinte. As duas ocorrencias encontradas nos
arquivos de entrega eram versoes do proprio C22, nao dois cortes distintos.

Em 29/09/2026, no `L21-C24`, o usuario pediu para reduzir o longo bloco de
interacao sobre quantas reunioes o publico fazia. Ele explicitou que a interacao
nao e proibida; o problema era repetir varias vezes a mesma pergunta. A V2
preservou uma ocorrencia de `Quantos de voces... duas reunioes por semana?`, o
limite curto `pelo menos duas / de duas pra cima` e um unico convite de resposta,
mas removeu a segunda formulacao da pergunta, a reafirmacao `se voce ja faz mais
de duas reunioes por semana` e as esperas correspondentes. Isto entra como
evidencia de limpeza editorial da marca: compacte repeticao de interacao sem
apagar automaticamente toda conversa com o publico.

Ao revisar essa V2, o usuario manteve a selecao editorial e tambem preservou o
trecho `aumentar tua taxa de conversao pra ontem`, mas apontou que as emendas do
bloco de interacao ainda soavam espacadas. O mapa mostrou cinco juncoes entre
`vendas? -> pelo menos duas -> de duas pra cima -> manda eu ai -> entao` usando
apenas 60 ms de overlap apesar de residuos de aproximadamente 200-300 ms entre
cauda e ataque. A V3 aplicou overlap adaptativo somente nessas juncoes, entre
aproximadamente 267 e 345 ms brutos, sem remover mais palavras nem alterar o
restante do corte. Isto reforca a separacao entre as duas passadas: acertar o
conteudo nao encerra o trabalho; a interacao mantida ainda precisa da mesma
escadinha sutil de cauda e bico usada nas falas declarativas. Os valores sao
calibracao deste caso e continuam dependentes de escuta humana.

Depois de assistir aos cinco arquivos finais `L21-C21` a `L21-C25`, em
29/09/2026, o usuario aprovou o lote inteiro como `perfeito`. A aprovacao inclui
explicitamente o `L21-C22` V3, com gancho autonomo e fechamento antes de
`Outra objecao`, e o `L21-C24` V3, com a interacao compactada e overlaps de
cauda e bico recalibrados. Registre isto como evidencia de resultado do conjunto:
as correcoes acumuladas resolveram os problemas percebidos sem exigir novo
refino nos cinco videos. A confirmacao de agendamento feita na mesma mensagem e
apenas autorizacao operacional e nao faz parte desta evidencia editorial.

Em 30/09/2026, no primeiro corte da live de 19/09 (`L19-C01`), o usuario
identificou pela entonacao que o fechamento em `Onde eu estou perdendo
resultado?` parecia interromper uma enumeracao ainda aberta, embora a transcricao
isolada pudesse parecer semanticamente completa. A fonte seguinte traz
`o quao distante eu estou dos benchmarks`, formando o terceiro item da lista
iniciada por `Onde eu estou perdendo performance?`. Foi gerada uma previa que
inclui somente esse sucessor e termina antes da explicacao seguinte sobre
benchmarks. O caso entra como evidencia, ainda pendente de escolha humana:
antes de travar o final de um corte, confira nao apenas palavras e waveform,
mas tambem se a prosodia projeta continuacao; quando houver duvida, inspecione e
apresente o sucessor real em vez de presumir que a ultima frase ja fechou a tese.

Ao revisar a continuacao completa, o usuario definiu a montagem do fechamento do
`L19-C01`: preservar `o quao distante eu estou dos benchmarks`, remover o aparte
de live `a gente tambem vai falar de benchmarks depois`, manter a explicacao que
comeca em `porque / a partir do momento que tu comeca a analisar dados` e seguir
pelas perguntas de CTR, conversao, pagina, reuniao e ticket medio. O corte deve
terminar em `Como e que eu sei todas essas coisas?`, antes da oferta do documento
de benchmarks. O gap acustico dentro de `porque / a partir` deve ser compactado
por cauda e ataque, nao mantido porque o ASR o absorveu num token. A primeira
renderizacao duplicou na legenda tokens que atravessavam gaps removidos (`a a`,
`tu tu`, `de de`); cada token deve aparecer uma vez dentro do mesmo grupo
editorial. Depois de assistir a versao completa, o usuario aprovou o `L19-C01`
com `esse dai ja ta bom`, confirmando esse fechamento e a emenda compactada
como resultado valido para este caso.

Na revisao seguinte, no `L19-C02`, o usuario apontou entre aproximadamente
`00:58` e `01:01` uma risada/hesitacao antes de `No fim das contas`. O ASR havia
fundido a vocalizacao e a entrada da frase num unico token longo (`No`), enquanto
a montagem dividiu esse token em dois intervalos e a legenda resultante mostrou
`No No fim das contas`. O diagnostico so ficou claro ao cruzar waveform, posicao
dos intervalos na timeline e transcricao. A correcao remove o primeiro fragmento
e preserva pre-roll antes do ataque verdadeiro. O caso reforca como regra de
processo da marca que waveform, timestamp/timeline e transcricao devem ser
analisados em conjunto; nenhuma fonte isolada valida palavra, risada ou fronteira.

Ainda no `L19-C02`, a revisao do arquivo completo revelou que a divisao
automatica por baixa energia atravessou tokens longos e remontou as duas metades
como repeticoes audiveis. O inicio passou a dizer `no funil que esta / no funil
que esta rodando hoje`; mais adiante, `algum` apareceu duas vezes, junto de
outros falsos arranques e redundancias que a passada editorial deveria ter
retirado. A versao corrigida escolheu a segunda ocorrencia valida de `algum`,
preservou somente `no funil que esta rodando hoje`, removeu o falso arranque
antes de `nunca ta rico` e refez o restante da limpeza editorial antes das
emendas. O gate final a `-35 dB` passou sem spans de `0.60 s` ou bloqueios de
`0.90 s`; a naturalidade continua dependente da revisao auditiva do usuario.

Evite encaixes artificiais como `salvar sua empresa de uma jornada ruim`.
Reorganize a frase para que destinatario, condicao e consequencia soem naturais
e preservem a tese real. Use `Aveny T WEB`, branco, centralizado e proximo
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
essa calibracao continua sendo evidencia daquele lote, mas o usuario esclareceu
em 30/09/2026 que ela foi uma excecao replicada indevidamente. Para os videos
atuais da Fase 1, use `1.18x` como base e aceite override explicito por video ou
lote. Houve correcao de titulo alto/fraco e fonte antes da aprovacao. `SEG-C03`
foi aprovado como video final, mas pode funcionar como alternativa editorial no
planejamento do feed; `SEG-C07` e `SEG-C08` reaproveitam material e nao contam
como ideias novas.

Em 30/09/2026, depois de assistir aos cinco renders `L19-C01` a `L19-C05` ja
recalculados em `1.18x`, o usuario avaliou o lote como otimo e autorizou preparar
titulo, copy e agendamento. Registre isto como evidencia de aprovacao conjunta
da montagem e da velocidade nesse lote especifico, sem inferir que cada escolha
de gancho, duracao ou texto visual virou regra para outros cortes.

No lote, o MP4 final foi validado em 1080x1920, 24 fps, audio estereo 48 kHz
e decodificacao completa. Esses parametros sao referencia de entrega daquele
lote, nao autorizacao para mudar um projeto diferente. O historico de drafts
CapCut H001-H032 esta em [Caso CapCut](rugido-cortes-capcut.md); leia-o so
quando o projeto for CapCut ou aquele exemplo for relevante. No Criado, mantenha
timeline editavel e FFmpeg como render derivado. Em FFmpeg avulso, preserve
mapa, fonte e comandos reproduziveis sem prometer camadas editaveis.

Em 28/09/2026, no arco `L21-C16` a `L21-C20`, o usuario pediu um experimento
editorial adicional: preservar os cinco microcortes por ponto de atencao e
produzir tambem uma versao longa unica para o mesmo dia, porque os cinco trechos
faziam parte de uma explicacao maior. A versao `L21-LONG01` recompoe em ordem
cronologica o arco `relevancia -> ruptura -> rediagnostico -> direcao ->
consciencia -> confianca`, sem simplesmente concatenar MP4s com titulos
diferentes.

Depois de ver o resultado, o usuario promoveu explicitamente esse experimento a
regra do metodo: sempre que o mapeamento de ganchos fragmentar uma explicacao
maior, completa e coerente em varios pontos de atencao, mantenha os microcortes e
gere tambem o video completo. Planeje a versao longa para o mesmo dia dos
fragmentos, de modo que o feed possa oferecer tanto as entradas curtas quanto o
raciocinio inteiro. A regra depende de existir um arco maior real; nao estique
falas independentes nem junte pecas apenas porque vieram da mesma live. Monte a
versao longa a partir das fontes, com titulo, legenda, cadencia e fechamento
proprios, preservando cronologia e eliminando duplicacoes causadas pela quebra em
microganchos.

Em 01/10/2026, o usuario rejeitou no `L19-C09` o titulo `Volume, conversao,
custo e resultado contam historias diferentes`, dizendo que ele nao parecia ter
relacao com o video. A fala do corte contrasta numero aparentemente bom com o
problema que pode ficar escondido: volume alto com baixa qualidade, conversao
alta com volume insuficiente, CPL baixo com leads ruins e muitas vendas com
baixa margem. Registre a rejeicao como evidencia do caso: o novo titulo deve
expor essa tensao ou consequencia, em vez de apenas enumerar quatro metricas ou
repetir a primeira frase. Entre as alternativas seguintes, o usuario escolheu
`Uma metrica boa pode esconder uma operacao ruim`, rejeitando `O numero parece
bom, mas esconde o problema` e `Voce pode estar comemorando a metrica errada`.

Na revisao imediatamente seguinte, o usuario rejeitou no `L19-C10` o titulo
`Reuniao barata demais costuma esconder lead ruim` porque ele basicamente
repetia o que Lucas ja dizia na abertura. O corte desenvolve uma camada que o
titulo anterior ignorava: CAC e custo de reuniao so podem ser avaliados junto
do ticket, do valor recebido por cliente e do tipo de funil. Registre como
evidencia do caso que o titulo visual deve completar o gancho falado com essa
consequencia ou mecanismo, e nao funcionar como uma segunda legenda da mesma
frase. O usuario escolheu `Seu CAC nao precisa ser baixo. Seu ticket precisa
pagar a conta`, rejeitando `CAC alto so e problema quando o ticket nao acompanha`
e `O custo da aquisicao so faz sentido junto do valor por cliente`.
