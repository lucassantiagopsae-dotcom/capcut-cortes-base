# Audio, Waveform e Fonetica

Use esta referencia quando a qualidade do corte depender de precisao fina de audio.

## Waveform como criterio

A waveform mostra energia sonora ao longo do tempo. Em fala limpa, ela ajuda a distinguir:

- voz real;
- respiracao;
- silencio;
- cauda de palavra;
- ataque da proxima fala;
- pausa expressiva;
- pausa morta.

Nao use a wave so para "cortar tudo que parece baixo". Use-a para decidir onde a fala realmente termina e onde volta a comecar.

## Timestamps nao sao borda final

Transcricoes com palavra por palavra ajudam muito, mas nao representam perfeitamente a pronuncia.

Problemas comuns:

- a transcricao marca a palavra como encerrada antes do som acabar;
- palavras curtas no inicio somem se o corte comeca no timestamp exato;
- a vogal final e o ar da boca sao cortados;
- o clipe seguinte entra em cima da mesma frase do anterior.

Por isso, trate timestamp como ponto de partida. Ajuste com ouvido e waveform.

## Margem fonetica

Como ponto inicial:

- antes da palavra: use uma margem curta para nao morder o ataque;
- depois da palavra: preserve cauda suficiente para a fala soar completa;
- em palavras como "e", "ou", "mas", "se", "so", "entao", "qual", use cuidado extra;
- se vier silencio longo antes da palavra, corte o silencio e preserve apenas a entrada real;
- se vier uma palavra indesejada, reduza localmente a margem.

A margem deve proteger o som, nao trazer sujeira.

## Pausas e gaps

Um gap pode ser:

- silencio util, quando cria intencao;
- silencio morto, quando a pessoa espera, olha, respira ou perde ritmo;
- pausa de live, quando o falante espera chat ou troca slide;
- pausa de roteiro, quando a frase respira naturalmente.

Remova gaps que quebram ritmo. Preserve gaps que fazem a fala ficar humana.

## Source duplicado

Antes de usar overlap, confira se os dois clipes nao trazem o mesmo pedaco do original.

Sinais de source duplicado:

- a mesma palavra aparece duas vezes;
- surge um tique alto na emenda;
- parece que a fala deu um pulo estranho;
- a frase entra cedo demais;
- a transicao soa como corte em cima de corte.

Solucao:

1. reduza a cauda do clipe anterior;
2. mova o inicio do proximo clipe para depois do trecho duplicado;
3. refaca o overlap na cauda/ataque correta;
4. so depois avalie fade.

## Fade curto

Use fade como ajuste cirurgico.

Casos bons:

- ataque do clipe seguinte entra seco;
- cauda do clipe anterior foi cortada perto demais;
- corte no meio de uma fala emendada precisa suavizar;
- respiracao baixa precisa sumir sem clique.

Casos ruins:

- tentar esconder duas vozes brigando;
- compensar um corte em source duplicado;
- aplicar fade em todos os clipes por padrao;
- usar fade longo que cria buraco audivel.

Duracao:

- use poucos frames;
- `0,05s` a `0,10s` costuma ser suficiente;
- ate cerca de `10 frames` quando o ouvido pedir;
- em 30fps, 10 frames sao cerca de `0,33s`.

No CapCut, confirme que o fade entrou no segmento certo. Se varios segmentos compartilham o mesmo `material_id`, pode ser necessario isolar o material antes.

## Script de apoio

Use `scripts/analisar_waveform_silencios.py` para gerar candidatos de baixa energia:

```powershell
python scripts/analisar_waveform_silencios.py "D:\caminho\video.mp4" --start 00:01:00 --end 00:03:00
```

O script gera JSON, CSV e Markdown com spans candidatos. Ele nao decide sozinho o corte final.

