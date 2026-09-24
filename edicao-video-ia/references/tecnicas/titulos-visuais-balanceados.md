# Titulos Visuais Balanceados

Use ao compor titulo dentro do video, capa ou criativo quando a quebra de linha
precisa formar um bloco visual forte. Nao confunda com titulo de plataforma nem
com legenda sincronizada a fala.

## Parametros do template

Defina antes de quebrar o texto:

- largura do canvas;
- largura maxima da caixa;
- fonte e peso reais;
- tamanho minimo e maximo;
- quantidade preferida e limite de linhas;
- alinhamento e posicao em relacao ao conteudo.

No preset Rugido/Lucas atual, use canvas de 1080 px, caixa de ate 900 px,
`Aveny T WEB`, fonte entre 72 px e 88 px e alinhamento central. Esses numeros
sao do cliente/template; a tecnica continua parametrizavel para outros projetos.

## Escolher a quebra

Meça com a fonte renderizada. Contagem de caracteres e apenas um indicio porque
letras diferentes ocupam larguras diferentes.

1. Normalize espacos e preserve a ordem das palavras.
2. Tente duas linhas primeiro; use tres quando duas nao couberem ou produzirem
   um bloco ruim. Quatro linhas sao excecao editorial.
3. Para cada quantidade de linhas, gere particoes contiguas entre palavras.
4. Teste os tamanhos do maximo ao minimo e descarte qualquer candidato que
   ultrapasse a largura da caixa.
5. Entre os candidatos validos, prefira larguras visuais proximas e contagens
   de palavras razoavelmente distribuidas.
6. Penalize fortemente palavra orfa, ultima linha com menos de cerca de 55% da
   maior linha e quebra que deixa preposicao/conector pendurado no fim.
7. Confirme que a quebra preserva unidades de sentido. O melhor placar visual
   nao autoriza separar uma expressao de modo artificial.

O objetivo nao e formar um retangulo matematico perfeito. E evitar a silhueta
triangular, a cauda curta e a sensacao de palavra abandonada. O peso principal
e a largura visual; a quantidade de palavras ajuda a desempatar.

## Ordem de correcao

Quando o titulo estiver mal distribuido:

1. procure outra quebra sem mudar a copy;
2. ajuste o tamanho dentro da faixa aprovada;
3. ajuste a largura efetiva da caixa sem ultrapassar o maximo;
4. refine a copy se ainda exceder linhas ou largura.

Nao reduza abaixo do minimo, nao estique/comprima o bitmap e nao force quatro
linhas para preservar uma copy fraca. No Rugido, 72 px e piso, 88 px e teto e
valores intermediarios como 76 px ou 84 px sao decisoes normais de composicao.

## Verificacao

- Renderize na resolucao final, centralizado na caixa real.
- Verifique largura da caixa incluindo padding.
- Leia cada linha em voz alta e confirme continuidade semantica.
- Compare as linhas pelo contorno visual, nao apenas por palavras.
- Confira que nenhuma linha foi cortada e que a posicao respeita areas seguras.
- Registre no artefato o tamanho escolhido, as linhas e as dimensoes medidas.

Para calcular e renderizar de forma reproduzivel, use
`scripts/balancear_titulo.py`. O script gera JSON com a decisao e, quando
solicitado, um PNG transparente sem redimensionamento posterior.
