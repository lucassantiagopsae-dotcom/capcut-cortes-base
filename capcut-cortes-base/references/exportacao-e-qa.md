# Exportacao e QA

Use esta referencia quando o usuario pedir um MP4 final ou quando uma alteracao visual/audio precisar ser verificada.

## Exportar nao pode mudar o draft

Quando exportar fora do CapCut com FFmpeg ou outro processo, replique o que esta no draft. Nao aproveite a exportacao para mudar:

- canvas;
- escala;
- posicao;
- layout;
- ordem dos elementos;
- titulo;
- legenda;
- velocidade.

Leia o draft e preserve.

## Antes de renderizar

Verifique:

- resolucao e fps esperados;
- duracao;
- canvas original;
- clipes compostos;
- transform/scale/position;
- audio ativo;
- volume/fades;
- assets referenciados.

Se houver compostos dentro de compostos, atravesse a estrutura ate chegar nos videos reais.

## Depois de renderizar

Confira:

- arquivo existe e abre;
- duracao bate com o draft;
- resolucao bate com o solicitado ou com o draft;
- audio nao esta mudo;
- nao ha tela preta inesperada;
- primeiros segundos nao mordem fala;
- frames intermediarios preservam layout;
- final nao corta a ultima palavra.

Gere frames de QA em pelo menos dois pontos quando o layout importa.

## Quando nao exportar

Se o usuario pediu apenas draft editavel, nao renderize MP4 por conta propria.

Se houver risco de layout errado e voce nao conseguir verificar visualmente, entregue o draft e explique o bloqueio.

