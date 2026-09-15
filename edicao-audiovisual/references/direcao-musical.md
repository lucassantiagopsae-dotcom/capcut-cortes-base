# Direcao Musical

## Planejar Pela Cena

Antes de procurar faixa, relacione o sentido da fala, expressao, cadencia e
imagem com a emocao desejada. Exemplos de funcao: proximidade, expectativa,
confianca, conquista, pertencimento. Nao imponha essa sequencia se o material nao
a sustentar; nao transforme depoimento contido em trailer epico por padrao.

Escolha por densidade, instrumentacao, pulso, arco dinamico e espaco para a voz.
Musica alegre pode contrariar uma dificuldade ainda nao resolvida. Letras e
melodias muito presentes podem competir com a fala. Uma mesma composicao pode
oferecer blocos suficientes; nao e necessario trocar de musica a cada pessoa.

Mapeie cada cue na timeline final: inicio/fim, trecho de fonte, funcao emocional,
nivel, automacao e relacao com os cues vizinhos. Alinhe chegadas musicais a ideias
reais sem antecipar visualmente uma conquista que ainda nao foi narrada.

## Fazer Uma Faixa Engatar na Outra

Escolha a tecnica pela passagem concreta, nao por uma lista de efeitos:

- **Continuidade de fonte:** se dois cues percorrem a mesma gravacao em tempos
  contiguos, prefira uma passagem continua e uma unica automacao. Duplicar os
  mesmos samples em duas faixas pode elevar volume ou causar cancelamento se
  houver processamento/atraso diferente.
- **Crossfade:** sobreponha saida e entrada em frases musicais compativeis. Ajuste
  o tempo ao andamento e a harmonia; fade longo nao garante uma emenda musical.
  Equal-power e candidato para sinais pouco correlacionados, nao regra universal.
  Em material identico/correlacionado pode haver ressalto: teste curva linear ou
  continuidade direta e confira ganho no meio da transicao.
- **Encaixe ritmico:** quando o pulso e evidente, compare batidas e frases das duas
  fontes. Evite duas baterias dessincronizadas. Pequeno time-stretch pode ajudar
  se nao criar artefatos; nao force BPM nem altere a voz para acomodar a musica.
- **Passagem espectral:** reduza temporariamente graves/percussao de uma fonte
  enquanto a outra assume, se houver conflito. A EQ deve soar como transferencia
  de energia, nao desaparecer com a trilha ou deixar a transicao abafada demais.
- **Ponte/SFX/cauda:** textura, impacto discreto, reverse ou cauda de reverb podem
  ligar timbres muito diferentes. Sao opcionais; nao adicione whoosh em todo corte
  nem reverbere a voz para mascarar uma emenda ruim. Respeite a licenca dos SFX.
- **Pausa intencional ou corte seco:** cabe em uma virada que pede ruptura. Defina
  o motivo, o ponto de parada e a retomada. Nao confunda lacuna acidental entre
  arquivos com silencio expressivo.

Ouca alguns segundos antes e depois com voz, e a musica isolada para diagnostico.
Confira pulso, harmonia, nivel, caudas e sentido emocional. Ondas sobrepostas nao
provam continuidade percebida. Se nao houver escuta direta, registre a pendencia.

## Mixar em Funcao da Fala

Mantenha voz, musica e efeitos separados enquanto trabalha. Use automacao
editorial para abrir espaco nas frases delicadas e crescer entre ideias;
sidechain/ducking, se necessario, complementa isso. Evite bombeamento a cada
silaba. Nao aumente a musica so porque o detector encontrou uma respiracao.

Confira o inicio real: o cue pode comecar em zero e ainda conter segundos mudos
na fonte ou um fade inaudivel. Quando o briefing pede musica desde a abertura,
escolha um trecho ativo e uma entrada audivel sem estalo. Confira tambem a cauda
final para nao interromper a ultima palavra nem cortar a resolucao musical.

Nao reutilize um valor fixo de ganho entre faixas com loudness diferente. Meca
loudness e true peak da mixagem final conforme o destino; esses numeros nao
atestam inteligibilidade. Audicione fala baixa, sibilancias e transicoes, tambem
em reproducao pequena quando possivel. Se so o visual mudou, preserve a mixagem
aprovada sem normalizar de novo.

## Licencas e Implementacao

Registre autor, titulo, URL, licenca, atribuicao exigida e modificacoes. Gratis
para ouvir nao significa licenciado para anuncio ou redistribuicao. Verifique os
termos do ativo escolhido na data de uso; nao suba faixas ao repo da skill.

Consulte a [documentacao oficial do FFmpeg](https://ffmpeg.org/ffmpeg-filters.html)
para `acrossfade`, `afade`, `sidechaincompress`, `loudnorm` e `ebur128` quando
esse for o motor usado. Confira as opcoes na versao instalada. Crossfades
encurtam a concatenacao pela duracao sobreposta; mantenha isso no mapa temporal
para nao deslocar eventos. Sao mecanismos, nao substitutos da direcao editorial.
