# Multicamera por Direcao do Olhar

## Quando Usar

Uma pessoa gravada simultaneamente por duas ou mais cameras, quando o briefing
pede acompanhar a camera para a qual ela fala. E uma tecnica de montagem, nao
um estilo obrigatorio nem motivo para acrescentar destaques, trilha ou efeitos.

## Distinguir Fontes e Sincronizar

Conteudo transcrito semelhante pode indicar angulos da mesma gravacao, novas
tentativas ou arquivos duplicados. Nao escolha automaticamente a segunda fala
nem descarte uma fonte so pelo texto repetido. Confira waveform, movimento de
boca e gestos para distinguir esses casos; hash igual identifica copia exata.

Metadados e timecode ajudam a propor alinhamento, mas podem refletir relogios
diferentes. Use correlacao de audio ou de envelopes de energia para localizar
offset; confirme com boca/gestos e em janelas no inicio, meio e fim do trecho
usado. Um pico de correlacao numa frase repetida pode apontar a ocorrencia errada.
Se o offset variar, investigue deriva temporal antes de aplicar uma constante.
Registre a convencao, por exemplo `tempo_B = tempo_A + offset`.

Escolha uma fonte de audio pela inteligibilidade e continuidade. Trocar a imagem
nao exige alternar microfones: isso pode mudar timbre, ruido e nivel a cada plano.
Mantenha cortes de conteudo e trocas apenas visuais identificados separadamente.

## Escolher a Camera e Preservar o Ritmo

Compare as imagens sincronizadas: olhos, rosto e orientacao do corpo, incluindo
a ida e a volta entre cameras. Olhar lateral ou para baixo nao prova leitura,
erro ou hesitacao; a outra camera pode estar naquela direcao.

Revise o trecho inteiro solicitado, incluindo chamada final e encerramento,
em vez de corrigir somente os tempos ditados pelo usuario. Use amostragem para
localizar candidatos e sequencias mais densas nas mudancas; frames isolados nao
certificam fluidez. Calibre a direcao de cada olhar pelas duas vistas reais.

Quando houver mudanca sustentada de interlocucao, acompanhe-a. Avalie microdesvios
e retornos breves dentro da unidade de sentido: cortar a cada piscada ou giro
curto pode produzir um vai e volta de poucos frames. Se o usuario rejeitar esse
picote, sustente o plano durante a frase e mude nos pontos de direcao e ritmo
significativos. Nao resolva impondo um intervalo fixo ou trocas periodicas.

Um olhar transitorio pode coexistir com fala correta. Decida o que remover pelo
conteudo e pela continuidade, nao pela regra de que a ultima tentativa e melhor.
Se uma pausa atrapalhar, refine a fala com
[Referencia e montagem](referencia-e-montagem.md) e preserve a sincronizacao de
cada angulo com a nova timeline. Uma troca visual isolada mantem audio continuo;
uma sobreposicao fonetica deve ser registrada explicitamente como tal.

## Verificar

Confira labios antes/depois das trocas, cobertura do trecho e o arquivo renderizado.
Recalcule legendas depois de cortes/overlaps e confira sua posicao em cada angulo:
enquadramentos distintos podem deslocar queixo e clavicula na tela. Velocidade,
estilo de legenda e posicao exata vem do briefing, nao desta tecnica.

Para voz de sala, distinga ruido de fundo de reverberacao. Filtros leves de ruido,
equalizacao e compressao podem ajudar, mas nao demonstram remocao de eco. Compare
com a fonte quando houver escuta, preservando consoantes e evitando voz metalica;
informe o alcance real do tratamento. Consulte
[Entrega e QA](../fluxos/entrega-e-qa.md) para separar medicao, inspecao e escuta.
