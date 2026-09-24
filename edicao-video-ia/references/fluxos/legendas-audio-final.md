# Legendas do Audio Final

Integra o processo compartilhado de legendagem do audio montado, inclusive
aprendizados de `capcut-legendas-rugido`. O editor e escolhido separadamente.

## Sincronismo

Estabilize a montagem antes de legendar. Reconstrua o audio efetivamente ouvido,
incluindo microcortes, overlaps, compostos e velocidade. A transcricao da live
inteira serve para localizar falas, nao como tempo final da legenda.

Respeite o servico escolhido e a autorizacao ja dada pelo usuario. No padrao
Rugido recente, a fonte e AssemblyAI quando houver acesso e autorizacao para
enviar audio; nao troque silenciosamente por Whisper ou legenda automatica
do CapCut. Uma transcricao word-level confiavel da mesma fonte pode ser
remapeada para a timeline final, evitando novo upload. Salve raw JSON,
transcricao legivel, tempos por palavra e SRT junto dos materiais de trabalho,
sem publicar audio ou chaves na biblioteca.
Se o provedor preferido estiver indisponivel, primeiro procure transcricao
word-level confiavel e verificavel da mesma fonte. Sem ela, use apenas outro
provedor autorizado pelo usuario; caso contrario informe que as legendas
cronometradas estao bloqueadas e peca escolha antes de trocar. Uma copy de
postagem pode ser redigida separadamente quando o video/transcricao disponivel
ja sustenta a tese, sem fingir que isso resolveu o timing das legendas.

Se houver nova montagem com texto semelhante ou duracao total quase igual,
recalcule os tempos pela timeline atual. Texto igual nao significa sincronia.
Uma transcricao final localizada pode ajudar em regioes de ASR inconsistente;
use waveform e escuta para refinar ataque/cauda, preservando a fala real.
Ao atravessar precomposicoes ou compostos, leia todos os blocos da timeline
principal em ordem e aplique offset, velocidade e overlap dos pais. Em fala
sobreposta, preserve a ordem editorial das palavras; ordenar apenas pelo
timestamp pode inverter o fim da frase anterior com a proxima entrada.

## Blocos e Aparencia

Agrupe por unidade de sentido, sintaxe, pontuacao, prosodia, respiro e leitura.
Uma legenda pode estar no timestamp certo e ainda falhar pela quebra de frase.
Antes de fechar um bloco, olhe 1-3 palavras adiante e atras: a proxima
completa verbo, complemento ou expressao fixa? O novo bloco comecaria por
preposicao, artigo, "que" ou resto pendurado? Corrija a fronteira sem afastar
demais o texto da fala. Verifique pontuacao minima que ajude o raciocinio,
nao pontuacao inventada pelo ASR. Termine uma ideia antes de iniciar outra:
nao deixe "seis" num bloco e "meses" no
seguinte quando a leitura pedir a expressao completa; nao una o ponto final
de uma tese ao comeco de outra so para preencher largura. Evite palavras isoladas quando
um bloco equilibrado cabe, mas nao prolongue legenda sobre outra fala. Confira
gaps durante fala, sobreposicao indevida entre cues e cobertura de inicio/fim.
Pausas sem fala nao exigem texto artificialmente persistente.

Leia fonte, tamanho, cor, posicao e largura do template/draft aprovado. Se o
briefing pede uma linha, divida o bloco que quebra visualmente; um limite de
caracteres e apenas heuristica, pois largura depende de fonte e enquadramento.
Nao diminua toda a fonte para acomodar um bloco ruim. Na entrega editavel,
instale textos de fato editaveis; queime-os apenas no MP4 quando esse for o pedido.

Em video vertical para anuncio, desenhe a area segura antes de escolher a posicao.
Reserve espaco inferior para descricao, controles e botao de CTA, e espaco lateral
para os elementos nativos do aplicativo. Suba a legenda o suficiente para ela
continuar legivel na veiculacao real; coordenadas de outro projeto nao sao preset.
Teste com uma sobreposicao que simule a interface e confira os blocos mais largos.

Quando a direcao pedir legenda limpa, prefira peso bold ou semibold, entrelinha
compacta e contraste de preenchimento, sem contorno pesado. Fonte grande nao
compensa quebra ruim: limite linhas pelo sentido, aproxime-as como um bloco e
confira ascendentes/descendentes. TASA Orbiter foi aprovada em casos Rugido e
DD Prime, mas continua sendo escolha do projeto, nao padrao para toda marca.
Nao transporte fonte, cor, contorno ou destaques de um cliente para outro:
use o projeto/referencia correspondente. Destaque de palavra e recurso
pontual, nao substituto de segmentacao e leitura.

No CapCut, preserve identidade do projeto e materiais de texto existentes;
consulte [CapCut editavel](capcut-editavel.md). Para Lucas/Rugido, consulte
[Metodo Lucas Felix](../casos/rugido-lucas-felix.md): uma linha amarela,
`TASA Orbiter Bold` sem italico no lote aprovado. Estilo, tamanho e geometria
devem ser conferidos no projeto especifico antes de aplicar.
Confira no render, incluindo angulos e fundos diferentes; nao certifique apenas
pelo comprimento das strings. Mantenha legenda continua distinta de titulo e
de destaque pontual de conceito.
