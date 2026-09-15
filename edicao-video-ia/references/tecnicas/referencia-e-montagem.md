# Referencia e Montagem

Tecnica compartilhada; nao determina estilo ou marca.

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

Antes de escolher angulos de gravacoes simultaneas, consulte
[Multicamera por direcao do olhar](multicamera-por-olhar.md).

Inspecione barras na propria fonte. Defina crop/escala base que as esconda em todo
o movimento, inclusive no zoom-out. Use o quadro util como referencia; proteja
rosto, gestos e contexto. Nao use zoom para esconder fonetica mal cortada.

Em plano aberto, alterne reenquadramentos quando houver mudanca de ideia ou
enfase. Evite pulsacao constante e ampliacao alem da qualidade da fonte. Se o
pedido for apenas acelerar um take, ajuste pontualmente com preservacao de pitch
quando disponivel, verificando labios e naturalidade; nao acelere todos.

## Emendas de Bico Sobre Cauda

Use quando o briefing pedir a entrada da proxima fala durante o decaimento da
anterior. Encurtar a pausa e concatenar dois clipes nao produz essa sobreposicao.
"Bico" designa aqui o pre-ataque/ataque da fala, inclusive sons fracos anteriores
ao pico; cauda inclui a terminacao audivel, nao apenas a vogal mais forte.

1. Relacione transcricao e som ao redor de cada borda. Se o ASR comprimir varias
   palavras em poucos milissegundos ou esticar um fim sobre a pausa, confira a
   fonte e, quando necessario e autorizado, retranscreva somente o trecho.
2. Examine o intervalo candidato a descarte, nao apenas as pontas. Uma legenda
   pode continuar exibindo palavras cujo audio foi removido. Recupere primeiro
   qualquer parte da frase que esteja faltando.
3. Localize o decaimento completo da primeira fala e a entrada fraca da seguinte.
   Inspecione tambem as altas frequencias ao procurar consoantes como o "s" final;
   um limiar unico de volume pode confundir fricativas com silencio.
4. Posicione o inicio do proximo clipe antes do fim do anterior. A regiao comum
   deve conter a cauda e o bico, sem empilhar duas silabas fortes nem duplicar
   amostras da mesma fala. Ajuste cada emenda; nao use overlap fixo universal.
5. Misture as duas faixas durante esse intervalo. Fades curtos servem para
   evitar clique nas extremidades; nao devem apagar o bico nem terminar a cauda
   antes de a proxima fala entrar. Confira ganho e clipping da soma: normalizacao
   automatica ou uma curva de crossfade podem reduzir a voz sem necessidade.

O mapa precisa representar a sobreposicao real:
`inicio_proximo = fim_anterior - overlap`. Recalcule a timeline acumulada com essa
subtracao, inclusive legendas, visuais e duracao. Uma troca visual pode ficar
dentro da emenda sonora sem dissolver dois rostos. Nao confunda overlap de audio
com duas imagens simultaneas ou com um fade entre clipes sem intersecao temporal.

Se houver aceleracao final, transforme todos os tempos pelo mesmo fator. Verifique
as duas faixas e a soma; inspecione picos, ataques e caudas e ouca as emendas em
velocidade normal e na entrega quando houver escuta disponivel. Ausencia de
clipping nao certifica naturalidade. Consulte o
[caso aprovado](../casos/convite-duas-cameras.md) para exemplos, nao presets.
