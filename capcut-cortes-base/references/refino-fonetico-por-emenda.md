# Refino Fonetico por Emenda

Use ao corrigir palavras mordidas, caudas interrompidas, sobreposicoes mecanicas
ou ao estender um refino para varios takes. Aprendizado generalizado da revisao
dos depoimentos RocketHub; nao define estilo, duracao ou regra de cliente.

## Localizar o som completo

A transcricao pode encerrar uma palavra antes de sua vogal, consoante final ou
ar terminar. Tambem pode esticar o timestamp sobre uma pausa. Portanto, nem o
fim textual nem a intersecao de um timestamp com um gap decidem sozinhos o corte.

Para cada emenda, examine a fonte antes e depois das duas bordas. Relacione o
texto com o ataque, a sustentacao e o decaimento do som. Preserve sons fracos
que completam a pronuncia; uma respiracao pode sustentar a cadencia. Nao remova
automaticamente tudo abaixo de um limiar de volume.

Um envelope RMS em janelas curtas ajuda a encontrar candidatos. Janelas de
5 ms foram uteis neste caso, mas tamanho de janela e limiar dependem da fonte.
Microfone, ruido, compressao e velocidade mudam a leitura. Resolucao numerica
fina nao e garantia de precisao fonetica.

## Decidir cada emenda

1. Leia o contexto falado e examine o som original dos dois lados.
2. Recupere ataque e cauda que tenham ficado fora dos clipes, sem trazer outra
   palavra indesejada nem repetir o mesmo pedaco da fonte.
3. Remova somente a parte da pausa cuja ausencia melhora a continuidade.
4. Escolha entre manter o corte, ajustar suas bordas ou restaurar fala continua.
5. Quando houver overlap, encaixe as margens de modo que a proxima silaba nao
   mascare a terminacao anterior. Use fade curto apenas onde a emenda pedir.
6. Confira o resultado em velocidade normal quando houver escuta disponivel.

Nao aplique o mesmo overlap a todos os cortes. Algumas emendas deste caso
usaram 20 a 70 ms e outras voltaram a ser continuas; sao exemplos, nao limites
nem valores padrao. Tampouco e obrigatorio alterar uma borda que ja funciona.

Se a fala ja e continua, um corte visual para zoom pode manter o audio contiguo,
sem pular tempo de fonte, duplicar som ou aplicar fade. A escolha de zoom ou
reenquadramento depende do briefing, nao da tecnica fonetica.

Confira tambem a entrada e o encerramento de cada take. Uma ultima palavra
precisa de sua terminacao completa. Se ela nao estiver na fonte selecionada,
verifique o original disponivel e o escopo do recorte; nao invente som ausente.
Recuperar fonetica pode aumentar a duracao. Nao compense cortando outras falas
para voltar ao tempo anterior, salvo restricao editorial explicita.

## Cobertura de varios takes

Registre por emenda: take, tempos anteriores e novos na fonte, posicao na
timeline, contexto, decisao, motivo e overlap/fades. Inclua as decisoes de
manter ou desfazer um corte. Preserve os trechos ja aprovados fora do pedido.

Separe tres alcances na entrega: varredura tecnica, refino individual e escuta
perceptiva. Nao anuncie que todos os takes receberam o mesmo tratamento quando
somente os primeiros foram refinados e os demais passaram por um detector de
silencio. Se o pedido cobre todos, percorra todas as emendas e extremidades.

## Conferir o que foi entregue

- Mantenha as fontes e margens recuperaveis no projeto editavel, com backup do
  estado anterior. Overlap na timeline nao exige duplicacao de tempo da fonte.
- Ao exportar por outro motor, compare os clipes reais, inclusive dentro de
  compostos: fonte, inicio, duracao, velocidade, posicao, volume e fades devem
  corresponder ao mapa de render. Confira tambem as transicoes entre compostos.
- Evite acumular arredondamento por clipe: derive os frames dos limites absolutos
  da timeline e mantenha o audio alinhado. Valide duracoes de audio e video.
- Para diagnosticar emendas, inspecione a voz sem a musica de fundo. Verifique
  ataques e caudas na regiao sobreposta, alem de saturacao e erros de decodificacao.
  Ausencia de dois sinais fortes simultaneos nao prova naturalidade.
- Quando houver transcricao final, compare-a com as fontes para localizar
  possiveis perdas. Diferencas em siglas, palavras curtas e pontuacao precisam
  ser conferidas no audio e no mapa; similaridade textual nao certifica fonetica.
- Confira imagens se alterou escala ou posicao. Uma barra da fonte pode continuar
  aparecendo em parte dos zooms, mesmo quando um frame parece correto.

Waveform, transcricao e integridade do arquivo complementam a escuta, mas nao
a substituem. Sem capacidade de ouvir diretamente, entregue o resultado
tecnicamente verificado e informe que a naturalidade perceptiva nao foi ouvida.
