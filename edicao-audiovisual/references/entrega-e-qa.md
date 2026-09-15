# Entrega e QA

## Preservar o Aprovado

Antes de alterar, identifique fontes, versao de referencia e camadas autorizadas.
Mantenha nova saida versionada, sem sobrescrever o unico aprovado. Registre
configuracao e mapa temporal para reproduzir o resultado. Nao leve caminhos,
credenciais ou materiais privados do cliente para um repositorio publico de skill.

Em revisao so visual, reutilize o video-base aprovado sem empilhar overlays velhos
e novos. Preserve o audio por copia de stream quando container e codec permitirem;
compare hash do stream/dados de audio, nao do MP4 inteiro. Se houver recodificacao
necessaria, nao prometa igualdade bit a bit: confira sincronismo e alteracoes.

Se apenas a trilha mudou, nao modifique cortes, zooms ou duracao da fala. Se a
montagem mudou, recalcule os tempos de musica e visuais pelo novo mapa, em vez de
reutilizar timestamps antigos sem conferir.

## Registro Reproduzivel

Para trabalho com varias camadas, mantenha um manifesto simples com:

- Fontes e versao-base; formato, FPS, duracao e relacao source/timeline.
- Cortes: take, in/out na fonte, start/end na timeline, velocidade, overlap/fades,
  motivo e status de revisao individual.
- Musica: fonte licenciada, offset, cue, automacao, transicoes e pausas intencionais.
- Visuais: ideia, texto, tipo, familia de ativos, posicao, cores, timing e animacao.
- Entrega: arquivos, versao, camadas preservadas e estado do projeto editavel.
- QA: verificacoes executadas, resultados, amostras e limitacoes perceptivas.

Nao imponha ferramenta ou schema novo se o projeto ja tiver um adequado. Guarde
fontes, geometria e dados de animacao, nao somente overlays rasterizados, caso o
usuario queira editabilidade posteriormente.

## Verificar o Arquivo Final

1. Meca duracao, resolucao, FPS, numero de frames, streams e erros de decodificacao
   no render final. Verifique inicio/fim e sincronismo, nao so exit code do render.
2. Compare cortes por indice de frame quando o tempo exato cair numa transicao:
   seek por timestamp pode selecionar frames vizinhos em fontes com PTS irregular.
   Derive frames de limites absolutos para evitar arredondamento acumulado por clipe.
3. Para fonetica, ouca bordas na voz isolada e na mixagem; revise ataques, caudas,
   duplicacoes, cliques e respiracoes. Medicoes e ASR sao pistas, nao aprovacao.
4. Para musica, confira inicio audivel, todas as passagens, picos, ducking e final.
   Um mapa de cues sem gaps nao prova ausencia de silencio na propria gravacao.
5. Para visuais, inspecione cada cue no MP4 final em momentos de entrada, leitura
   e saida. Confira tambem em movimento: contraste, rostos, barras, acentos, limites
   do overlay, alpha, fontes e os piores fundos claros/escuros.
6. Confira cobertura por take. Nao declare video inteiro revisado com base apenas
   em tres screenshots. Se houver apenas amostragem, diga qual foi o alcance.

Contact sheets aceleram revisao estatica, mas nao demonstram fluidez. Alpha em
cantos transparentes ajuda a detectar painel acidental, mas nao substitui olhar
o conjunto. Sem capacidade de ouvir/ver movimento, entregue apenas as conclusoes
suportadas e indique a revisao perceptiva pendente.

## Editavel Quando Solicitado

Enquanto o usuario aprova MP4s, nao atualize CapCut automaticamente. Se o draft
precisar ficar intocado, registre hashes antes/depois nos arquivos relevantes.

Quando solicitado, entregue fontes recuperaveis e camadas separadas de fala,
musica, SFX, texto e elementos visuais, respeitando o editor escolhido. Compare
timeline e render final, inclusive compostos. Preserve backups e edicoes humanas.
Explique quais efeitos permanecem editaveis e quais precisaram ser pre-renderizados;
nao prometa texto, tracado ou curvas editaveis quando so existe um video alpha.
