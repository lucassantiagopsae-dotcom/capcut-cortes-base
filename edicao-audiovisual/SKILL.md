---
name: edicao-audiovisual
description: "Edita e refina videos combinando fala natural, direcao de trilha sonora e motion graphics alinhados ao conteudo e a marca. Use para montagem audiovisual, depoimentos de abertura de live, talking heads, transicoes musicais e destaques visuais. Para apenas limpar pausas ou corrigir fonetica, prefira a skill de cortes disponivel; esta skill coordena as camadas sem impor editor, marca ou formato."
---

# Edicao Audiovisual

Transforme o material e o feedback em decisoes de montagem verificaveis. Nao
confunda aumentar a quantidade de efeitos com melhorar a narrativa. Preserve a
fala, a credibilidade e as camadas ja aprovadas fora do pedido atual.

## Escolher o Escopo

Identifique fontes, intervalos solicitados, versao aprovada, formato, destino,
identidade visual e entrega desejada. Consulte os arquivos antes de assumir que
o nome de um video identifica corretamente todas as pessoas que aparecem nele.

Separe tres niveis: fundamentos reutilizaveis, linguagem do tipo de video e
decisoes do cliente. Nao aplique automaticamente a outro trabalho o estilo do
ultimo caso. Um pedido de contraste no icone nao autoriza criar um painel para
toda a composicao. Um pedido de musica nao autoriza recortar novamente a fala.

## Ler Apenas o Necessario

- Analise de referencia, limites de trechos e cortes naturais:
  [references/referencia-e-montagem.md](references/referencia-e-montagem.md).
- Escolha emocional da musica, transicoes e mixagem:
  [references/direcao-musical.md](references/direcao-musical.md).
- Textos de impacto, icones, animacao e enquadramento:
  [references/motion-e-hierarquia.md](references/motion-e-hierarquia.md).
- Depoimentos e abertura de live, incluindo o caso RocketHub como exemplo:
  [references/depoimentos-abertura-live.md](references/depoimentos-abertura-live.md).
- Exportacao, preservacao do aprovado, editabilidade e evidencias de revisao:
  [references/entrega-e-qa.md](references/entrega-e-qa.md).

Se a skill `cortes-base` ou `capcut-cortes-base` estiver instalada, use suas
referencias para refino fonetico detalhado. Nao e dependencia obrigatoria: o
essencial independente de ferramenta esta em `referencia-e-montagem.md`.
Use a skill especifica do editor apenas quando operar aquele editor.

## Fluxo de Trabalho

1. Inspecione o trecho solicitado e os materiais locais existentes. Diferencie
   o que foi visto, ouvido, transcrito e apenas medido tecnicamente.
2. Registre as unidades de sentido e os pontos emocionais, sem inventar
   resultados nem alterar a ordem fornecida sem autorizacao.
3. Estabilize a fala quando o escopo incluir cortes. Preserve ataque, cauda,
   respiracao expressiva e contexto. Atualize o mapa temporal apos o refino.
4. Planeje a musica sobre essa timeline: intencao, fonte, entradas, saidas,
   transicoes e automacao de volume. Nao escolha so pelo genero musical.
5. Planeje visuais por ideia: o que ajudam a entender, quando entram, por quanto
   tempo ficam e onde cabem sem cobrir a pessoa. Destaque nao e legenda continua.
6. Em mudanca ampla de linguagem, confira amostras representativas em movimento
   antes do render completo; depois procure o mesmo problema em todos os takes.
7. Exporte uma nova versao preservando fontes e aprovado. Confira o arquivo final,
   nao apenas as imagens geradas antes da composicao.

Esse fluxo nao obriga refazer etapas ja aprovadas. Em ajuste apenas visual,
reutilize cortes e audio final; em ajuste de trilha, mantenha o video aprovado.

## Contrato de Entrega

Preview, MP4 e projeto editavel sao entregas distintas. Preserve o editor escolhido;
nao migre para CapCut, Criado ou Remotion por preferencia propria. Quando o usuario
adiar o editavel, mantenha os dados necessarios, mas nao altere o draft a cada
revisao. Um MP4 importado inteiro nao equivale a entregar camadas editaveis.

Informe arquivo/versao entregue, o que mudou, o que foi preservado e limites reais
de verificacao. Nao certifique naturalidade por waveform, nem legibilidade por
dimensoes calculadas apenas. Consulte `evals/evals.json` ao evoluir esta skill para
revisar os cenarios de regressao; eles sao casos de teste, nao provas de execucao.
