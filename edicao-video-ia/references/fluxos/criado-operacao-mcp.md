# Operacao Editavel no Criado

Leia junto de [Criado e FFmpeg](criado-ffmpeg-editavel.md) somente quando o
usuario escolheu o Criado. Esta referencia incorpora o fluxo operacional das
duas skills `criado-editor` e do piloto `rugido-loop-cortes-criado-teste`.
O schema e as ferramentas mudam: confirme capabilities e a documentacao do
projeto instalado antes de usar exemplos antigos como contrato.

## Descoberta e revisao

Encontre servidor/projeto pelo ambiente, sem assumir porta. Consulte
capabilities, projeto, revisao, contexto, assets e anotacoes antes de editar.
Use comandos revisionados para importar midia, adicionar faixas/clipes,
alterar cortes, fades, velocidade, texto, legenda e precomposicao. `409` ou
revisao diferente significa reler estado e reconciliar com edicao humana;
nao aumentar o numero automaticamente. Depois de cada lote de comandos,
releia a revisao e o resultado. A fonte completa permanece importada; clipes
apontam para in/out, nao para renders achatados. Confirme `get_waveform` e
frames de fonte quando disponiveis, ouvindo as bordas.

Se houver atividade visivel, reporte marcos reais de trabalho, sem afirmar
conclusao antes de verifica-la. Notificacao visual nao comprova edicao.
Ao exportar, acompanhe o job ate arquivo final e confira preview/render;
exportar nao publica. Anotacoes sao pedidos ou evidencias: leia o alvo, a
revisao e o comentario antes de resolver; so marque resolvido apos aplicar
e verificar ou registrar impossibilidade.

Legenda automatica no Criado usa apenas o audio final da timeline como entrada
tecnica. Conecte transcritor autorizado ou remapeie words confiaveis da fonte;
aplique cues como faixa de texto editavel. Se a revisao mudou durante a
transcricao, nao aplique tempos velhos sem reconciliar. Chaves ficam no cofre
ou ambiente seguro, nunca no projeto ou na skill.

## Piloto e aprendizado

Quando o usuario pedir validar o fluxo antes de escalar, rode um corte piloto:
bruto/transcricao -> gancho aprovado -> mapa de tese e source/timeline ->
projeto editavel -> QA da fala -> legenda editavel -> QA final. Pare onde o
pedido parar; um atlas isolado nao cria draft. Registre ID/revisao, verificacoes
feitas e pendencias. Se MCP/API nao estiver disponivel, entregue mapa de
comandos e diga que nada foi aplicado.

Uma sessao de aprendizado deve incluir historico de acoes, timeline antes e
depois, estado final, anotacoes, escopo do modelo/video/grupo e confirmacao
humana. `record_learning` ou endpoint equivalente pode atualizar uma skill do
projeto Criado, mas nao altera automaticamente esta biblioteca geral. Compare
e promova somente regras confirmadas e transferiveis, evitando duplicatas por
video. Nao confunda acao observada com intencao editorial inferida.

Desenvolvimento do aplicativo e outra tarefa: se pedido, leia instrucoes do
repo Criado e use a skill operacional de engenharia; a skill editorial nao
autoriza mutar codigo do app durante uma simples edicao.
