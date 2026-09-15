# CapCut Editavel

Use somente ao criar, ajustar ou reconstruir um draft CapCut. Conhecimento
empirico de arquivos locais, nao uma promessa de API publica estavel: confirme
campos e unidades num draft da versao instalada. Preserve campos desconhecidos.

## Estado e Identidade

Localize o projeto real pelo ambiente e pelos metadados, sem fixar caminho de
um computador. Confira `.locked`, processo aberto e alteracoes recentes. Nao
escreva contra um projeto que o editor esta salvando. Uma copia tecnica isolada
pode servir a experimentos, sem duplicar automaticamente o projeto visivel.
Trabalhe no mesmo draft quando solicitado; salve backup separado dos arquivos
que serao alterados e mantenha intacta a unica copia recuperavel anterior.

Inspecione `draft_content.json`, `draft_meta_info.json`, `template-2.tmp`,
`draft_settings`, `timeline_layout.json` e `Timelines/*` quando presentes. Nem
todo arquivo e espelho: estabeleca a versao autoritativa antes de sincronizar.
Nao sobrescreva um backup de recuperacao como se fosse cache. Nome da pasta e
nome visivel nao sao necessariamente a mesma identidade; altere somente o que
for necessario para o pedido, mantendo IDs e caminhos de media coerentes.

Em conflito, inventarie hash, horario, IDs e diferencas de segmentos/materiais de
cada candidato. Horario mais recente sozinho nao define autoridade. Compare com
o ultimo estado conhecido e com as alteracoes humanas visiveis; use uma base
comum quando houver para separar mudancas independentes de mudancas concorrentes.
Reconcilie somente campos compreendidos, por IDs e referencias, em copia tecnica;
nao concatene arrays nem escolha automaticamente um lado de conflito semantico.
Se nao houver evidencia suficiente, preserve os candidatos e pergunte qual estado
deve prevalecer antes de modificar o projeto real.

Um `.locked` antigo nao prova abandono. Confirme que o editor/projeto nao esta
aberto ou salvando e observe se arquivos continuam mudando; estabilidade isolada
tambem nao prova ausencia de processo. Prefira fechamento normal pelo usuario
quando necessario. Nao apague o lock nem encerre o editor para forcar a escrita.

## Estrutura e Tempo

Inspecione `tracks[].segments[]`, `material_id`, `extra_material_refs`,
`source_timerange`, `target_timerange`, `materials.videos/texts/speeds/drafts` e
`canvas_config`. Os tempos observados usam microssegundos; confirme no draft.
Source e target diferem quando ha velocidade. Considere velocidade do clipe e
do composto pai sem aplica-la duas vezes; calcule limites absolutos em frames
para evitar erro acumulado por arredondar cada clipe separadamente.

Monte um indice global dos subdrafts, alem da procura local. Um composto pode
referenciar por `extra_material_refs` um item de `materials.drafts` da raiz.
Atravesse os compostos recursivamente ate as fontes reais, respeitando offsets,
recortes, velocidades e transformacoes dos pais. Detecte referencia ausente ou
ciclo em vez de tratar como video vazio. Recalcule duracoes do filho ao projeto.

Ao remover um trecho, remova o segmento na track correta. Cobrir com outro
clipe ou ignora-lo apenas no export deixa residuos que o editor pode mostrar
ou reorganizar. Nao remova materiais ainda referenciados por outros segmentos.

## Protecao dos Microcortes

Para muitos microcortes sobrepostos, preserve a escadinha interna e mantenha
poucos compostos na raiz. Precomponha blocos estabilizados quando isso protege
a montagem ou contorna limite de faixas. Nao achate compostos humanos apenas
para simplificar o JSON; eles podem separar corpo aprovado e final em revisao.
Em corte simples neutro, nao crie complexidade sem beneficio. A preferencia de
precompor a entrega Rugido fica no [caso Rugido](../casos/rugido-cortes-capcut.md).

Em estruturas sujeitas a reorganizacao, confira `config.maintrack_adsorb` e
`render_index_track_mode_on`. Quando existirem e o comportamento estiver
confirmado, desative os que desmontam a montagem, incluindo copias autoritativas
em subdrafts/Timelines. Nao invente campos ou force configuracoes globais sem
entender seu efeito. Se nao puder proteger a montagem, registre a limitacao.

Varios segmentos podem compartilhar `material_id`. Antes de alterar um campo
armazenado no material, conte referencias e isole o material quando necessario.
Nos drafts observados, fades aparecem em `materials.videos[].audio_fade`, com
duracoes em microssegundos. Confirme o esquema local, aplique no material certo
e confira segmentos vizinhos. Descrever fade no mapa nao o aplica no CapCut.
Transformacoes locais de segmento nao exigem duplicar materiais por padrao.

Ao reajustar uma ponte sobreposta, use a ordem editorial descrita em
[Limpeza e cadencia](../tecnicas/limpeza-e-cadencia.md); nao deixe o sucessor no
tempo antigo por ele comecar antes do fim anterior.

## Exportacao Fiel

Leia canvas, proporcao da fonte, `clip.scale`, `clip.transform`, indices de
renderizacao e textos reais. Canvas vertical nao implica colocar a live no
topo nem esticar a imagem horizontal. Preserve titulo e legenda aprovados.

Para overlay simples sem rotacao nem transformacao de pai, nos drafts observados:

```text
center_x = canvas_w/2 + transform.x * canvas_w/2
center_y = canvas_h/2 - transform.y * canvas_h/2
x = center_x - material_w * scale_x/2
y = center_y - material_h * scale_y/2
```

Verifique contra o editor. Rotacao, crop e pais exigem compor suas transformacoes;
nao aplique a formula simples a uma arvore arbitraria. Calcule tamanho exibido
do PNG apos escala: percentual de interface sozinho nao prova ocupacao visual.

Se exportar por FFmpeg, preserve filtros, fades, ganho e velocidade reais. Confira
as opcoes aceitas pela instalacao antes de assumir incompatibilidade. Com limite
de comando ou grafo extenso, arquivos temporarios de trechos podem servir ao
render; mantenha as fontes completas no draft, sem substituir clipes editaveis
por esses intermediarios. Reutilize cache somente se as dependencias nao mudaram.

## Validacao e Recuperacao

Confira referencias, unidades, IDs, duracoes e camadas antes da escrita. Depois,
abra o projeto no CapCut quando disponivel, confirme media online, preview e
editabilidade, e compare o export ao draft. JSON valido nao prova que o projeto
abre. Informe se a verificacao ficou restrita aos arquivos.

Se o projeto ficar vazio, reverter sozinho, perder media ou divergir entre
espelhos, interrompa novas escritas, preserve o estado para diagnostico e
recupere o backup pertinente sem apagar alteracoes humanas posteriores. Nao
tente corrigir apagando estruturas desconhecidas. Consulte
[Entrega e QA](entrega-e-qa.md) para a entrega solicitada.
