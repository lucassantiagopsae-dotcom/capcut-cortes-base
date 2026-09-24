# Caso: lote Ryan (Socio Talentos) - cadencia por refinamento humano

Aprovado em 17/09/2026 no video 01 (ST Ryan 01). Registro do antes/depois
entre o corte automatico pos-limpeza e o ajuste humano no CapCut.

## O que o humano mudou (mesmos 9 blocos, mesma ordem)

1. **Overlap uniforme -> adaptativo por juncao**:
   - maquina: 8 emendas iguais de 0,018s;
   - humano: 0,30s na transicao que precisou mascara, 0,10-0,17s nas
     intermediarias, 0,067s na emenda limpa final.
2. **Ataques mais secos**: entradas adiantadas em +0,04 a +0,34s (pre-roll
   da maquina era sistematicamente longo; mirar 0,05-0,15s do ataque real
   quando a entrada vem de vale de silencio).
3. **Caudas calibradas por palavra**: -0,23s onde sobrava ar, +0,09s onde
   faltou (cauda nao e constante de projeto).
4. Efeito: 39,62s -> 37,47s sem perder conteudo; emendas "respiram" de
   formas diferentes e o video anda em ritmo constante.

## Como derivar o overlap sem ouvido humano (validado na geracao do video 02)

Para cada juncao A->B, medir no envelope do bruto (limiar ~-40 dB):
- `A termina voado?` = fim_da_fala_A perto do corte final de A (<0,05s);
- `B comeca voado?` = ataque de B perto do inicio de B (<0,05s).
Regra:
- ambos voados (fala continua) -> overlap ~0,28s;
- so um voado -> ~0,16s;
- fronteira de frase (ambos com ar) -> ~0,08s.
Bordas: entrada = ataque - 0,08s; saida = ultima fala + 0,20s.

## Armadilhas tecnicas do render por overlay (ffmpeg)

- cada clipe precisa de `setpts=(PTS-STARTPTS)/{speed}+{tgt_in}/TB`;
  sem o offset de janela o overlay consome os frames no inicio do video e
  exibe frame congelado durante a janela inteira (sintoma: slideshow);
- o clipe-base precisa `tpad=stop_mode=clone` ate a duracao total;
- `ass=` com caminho absoluto com espaco/acento quebra o parse do filtro;
  usar caminho relativo com `cwd`;
- no Windows, `tempfile.mkstemp` mantem o handle aberto: fechar antes de
  apagar.

Arquivo completo do antes/depois: no projeto Socio Talentos,
`trabalho/lote_ryan_20260917/aprendizado_refinamento_humano_ryan01.md`.

## Acrescimos validados na correcao do video 02 (mesma noite)

1. **Palavra ASR esticada (>0,8s) = armadilha**: pode conter take repetida
   ("pode confirmar" 2x fundidas numa palavra de 1,62s). Sempre transcrever
   isolado o entorno antes de confiar na ausencia de duplicacao.
2. **Audio em overlap = crossfade equal-power** (sqrt), nunca soma plena:
   somar as duas falas em volume total gera stutter/gaguejo audivel.
3. **Gap de legenda >0,6s com audio presente** = emenda com ar morto
   (respirada alta classificada como fala pelo limiar de envelope): apertar
   cauda por palavra real e reduzir o overlap da juncao.
4. **Conferir a ultima palavra de cada clipe** contra o fim de fala real
   (corte de 0,07s em "consórcio." era audivel).
5. Scan de stutter textual no ASR final: palavras consecutivas iguais.

Log completo com cada edicao temporal:
`trabalho/lote_ryan_20260917/log_edicao_frame_a_frame_ryan02.md` no projeto.

## Ryan 03: sussurro e falso arranque de CTA

- afftdn/denoiser come fala muito baixa: sussurro a -50 dB vira "silencio"
  percebido. Ganho pre-tratamento nao sobrevive ao denoiser; fala >25 dB
  abaixo do nivel do video = cortar (boost nao conserta SNR).
- Cauda colada: quando a ultima palavra encosta na seguinte (régua|só em
  49,82), a cauda de 0,20s engole comeco da proxima; reduzir para ~0,04s.
- Vogais de CTA arrastadas ("É uuma liive") entram no ataque da primeira
  palavra real, preservando o drawl como cadencia do falante.

## Ryan 03 (saga final): lixo de priming AAC em MOV de selfie

- MOVs de celular com AAC/edit list: input-seek (-ss antes de -i) cospe
  ~0,85s de spikes + silencio digital no inicio do clipe. Sintomas: "loud
  sempre a +0,85s", "sussurro que boost nao conserta", RMS -55 com ASR
  transcrevendo palavras.
- Diagnostico: distribuicao de amplitude do clipe (p50/p90/max). Spikes em
  escala cheia com p50 baixo = lixo de seek. Compensar o in ou decodificar
  integral com trim.
- Edit de draft CapCut por LANDMARK de conteudo, nunca por indice.
- Verificacao de entrega: correlacao wav<->mp4 (lag 0, corr ~1) + coerencia
  palavras ASR <-> RMS por bucket.

## Ryan 04: analise fria do erro repetido (3 apontamentos, 1 causa)

- Regiao com TRES takes; ISO com input-seek (offset ~0,85s) enxergava duas —
  a entrada caia no meio da take incompleta. Coordenadas de corte SO de ISO
  fatiado do decode integral (numpy slice), nunca de -ss.
- Boost em palavra que ninguem reclamou = over-correction que gera estouro;
  boost exige limiter + checagem de pico. Mexer somente no que o ouvido apontou.
- Segmentos adjacentes consecutivos na fonte (gap <= 0,45s) sao FUNDIDOS, nao
  emendados — emenda so onde existe salto real.
