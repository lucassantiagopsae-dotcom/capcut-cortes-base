# Referencia e Montagem

## Analisar So o Trecho Pedido

Se o pedido limita uma live a 00:00-05:38, limite a extracao, transcricao e
inspecao a esse intervalo. Metadados podem exigir ler o container; isso nao
equivale a analisar toda a live. Acesso remoto pode exigir download maior por
restricoes do servidor: nao prometa transferencia parcial sem verificar suporte.
Um arquivo ja local pode ser recortado sem enviar o restante ao modelo ou a uma API.

Extraia frames por mudanca de plano e perto das transicoes; refine a amostragem
onde houver animacao. Frames isolados nao demonstram ritmo nem suavidade.
Para audio, use somente o trecho autorizado. Reutilize transcricoes existentes;
envio externo exige autorizacao, inclusive quando ha chave configurada.
Nao prometa custo exato de tokens a partir da duracao do arquivo.

Registre: timecode, fala/acao, corte, enquadramento, musica, transicao, elemento
visual e funcao narrativa. Uma referencia inspira principios; nao autoriza
copiar musica, marca ou ativos sem licenca. Canal, titulo, thumbnail ou transcricao
nao provam que voce assistiu e ouviu um video. Cite a fonte e o alcance real da
analise, sem atribuir tecnicas a um criador cujo trecho nao foi verificado.

## Fonetica Antes do Overlap

Timestamps de palavras sao candidatos, nao fronteiras acusticas. Verifique ataque,
sustentacao e decaimento na fonte dos dois lados de cada emenda. Vogais finais,
consoantes fracas e ar podem continuar depois do fim textual; ruido tambem pode
parecer voz. RMS e detector de silencio nao distinguem isso sozinhos.

Recupere primeiro a palavra inteira; remova depois a pausa que prejudica a
fluidez. Nao elimine respiracao expressiva nem aplique um tempo igual a todas as
pausas. Ajustar o fim de uma palavra pode aumentar a duracao final; nao compense
com outro corte sem necessidade editorial.

Escolha por emenda: manter, mover bordas, restaurar continuidade, ou sobrepor
margens compativeis. Sobreposicao fonetica encaixa cauda e ataque sem disputar
silabas inteligiveis. Nao duplique o mesmo intervalo da fonte. Fade curto pode
suavizar descontinuidade, mas nao recupera uma silaba apagada nem conserta uma
fronteira errada. Ouca a voz isolada e depois a mixagem em velocidade normal.

J-cut significa que o audio do proximo plano entra antes de sua imagem; L-cut
mantem o audio anterior depois da troca de imagem. Ambos separam a fronteira
visual da sonora: nao exigem duas falas completas simultaneas nem dissolve de
video. Um corte visual para zoom pode manter audio perfeitamente contiguo.

Revise todas as emendas e extremidades quando o pedido abranger todos os takes.
Registre inclusive cortes mantidos e overlaps desfeitos. Uma varredura de volume
nos takes restantes nao equivale a aplicar o mesmo refino individual.

## Escala e Ritmo Visual

Inspecione barras na propria fonte. Defina crop/escala base que as esconda em todo
o movimento, inclusive no zoom-out. Use o quadro util como referencia; proteja
rosto, gestos e contexto. Nao use zoom para esconder fonetica mal cortada.

Em plano aberto, alterne reenquadramentos quando houver mudanca de ideia ou
enfase. Evite pulsacao constante e ampliacao alem da qualidade da fonte. Se o
pedido for apenas acelerar um take, ajuste pontualmente com preservacao de pitch
quando disponivel, verificando labios e naturalidade; nao acelere todos.
