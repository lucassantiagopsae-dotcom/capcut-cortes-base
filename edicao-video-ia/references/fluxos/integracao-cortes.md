# Origem e Integracao dos Cortes

Use ao manter a biblioteca integrada. A base inicial foi consolidada em
15/09/2026 a partir de cortes-base, capcut-cortes-base e capcut-cortes-rugido.
Em 22/09/2026, a entrada recebeu metodo Lucas independente do editor, atlas de
ganchos e aprendizado de legendas mais recente. As skills de origem continuam
intactas; estes modulos e o script incluido permitem usar edicao-video-ia
isoladamente. Nao ha sincronizacao automatica de
futuras mudancas nas fontes: compare conteudo e evidencia ao incorporar revisoes.

## Inventario da consolidacao de 22/09/2026

Treze diretorios foram preservados integralmente em
`trabalho/skill_consolidation_backup_20260922/` no workspace Lucas Felix.
A copia 01 registra esta skill antes desta rodada. As duas skills dos repositorios
CapCut permaneceram intactas: sao fontes versionadas, nao instalacoes globais
automaticas. Use este inventario para auditar origem; a execucao dos modulos
acima nao depende dos caminhos do backup.

| Copia | Fonte | Conhecimento integrado / limite |
| --- | --- | --- |
| 01 | edicao-video-ia (global) | Base ja consolidada; ponto de entrada a evoluir, nao evidencia nova |
| 02 | cortes-base (global) | Fonetica, waveform, microcortes, QA; tecnica neutra |
| 03 | cortes-de-live (global) | Cobertura total, ranking, mix editorial, privacidade, remontagem condicionada: [curadoria](curadoria-live-detalhada.md) |
| 04 | mapeamento-ganchos-brutos (global) | Nucleo/unidade, gates, calibracao e estados humanos: [atlas avancado](atlas-rugido-avancado.md) |
| 05 | capcut-legendas-autoral (global) | Sincronia acustica e quebra semantica; identidade visual de outro cliente nao migra para Lucas |
| 06 | criado-editor (global) | Operacao e comportamento do aplicativo; desenvolvimento do app continua especialidade separada |
| 07 | cortes-rugido (local) | Metodo Lucas e historico H001-H032, inclusive Aula Segunda aprovada |
| 08 | capcut-legendas-rugido (local) | Audio final, ordem dos compostos, TASA Orbiter Bold, one-line quando padrao Lucas |
| 09 | criado-editor (local) | MCP, revisao, comandos, anotacoes, atividade, export: [operacao Criado](criado-operacao-mcp.md) |
| 10 | rugido-loop-cortes-criado-teste (local) | Piloto com checkpoints de gancho, corte, legenda e QA: operacao Criado |
| 11 | descricao-video-tese (local) | Copy de postagem Lucas, distinta de legenda falada: [copy](copy-publicacao.md) |
| 12 | capcut-cortes-base (repositorio) | Implementacao CapCut da tecnica neutra; seis arquivos coincidem com cortes-base |
| 13 | capcut-cortes-rugido (repositorio) | Drafts e casos CapCut Rugido; treze arquivos coincidem com cortes-rugido local |

"Integrado" significa criterio operacional condensado, nao transcricao literal
de cada exemplo ou dado privado. Casos e evidencias completos ficam nas fontes
preservadas. Nao transforme contagens, score ou velocidades historicas em lei
global sem teste e aprovacao no novo contexto.

## Mapa de Conhecimento

| Origem consultada | Destino mantido nesta skill |
| --- | --- |
| cortes-base/SKILL e capcut-cortes-base/SKILL: escopo, limpeza, cronologia, mapa, escadinha | [Limpeza e cadencia](../tecnicas/limpeza-e-cadencia.md) |
| Ambas: audio-waveform-e-fonetica, microcortes-e-continuidade, refino-fonetico-por-emenda | [Referencia e montagem](../tecnicas/referencia-e-montagem.md), limpeza e QA |
| Ambas: exportacao-e-qa | [Entrega e QA](entrega-e-qa.md) |
| Ambas: capcut-draft-editavel; cortes-base: capcut-engenharia-reversa-json | [CapCut editavel](capcut-editavel.md) |
| cortes-base: criado-ffmpeg-timeline | [Criado e FFmpeg](criado-ffmpeg-editavel.md) |
| scripts/analisar_waveform_silencios.py das bases | Script local incluido, com validacao de parametros; uso em limpeza e cadencia |
| Rugido/SKILL, H004/H005 e H020: tese, ponte, declarativa, fechamento | [Cortes de live por tese](../estilos/cortes-live-por-tese.md) e [metodo Lucas](../casos/rugido-lucas-felix.md) |
| Rugido: H001 overlap, H006/H009/H010/H014/H015/H016/H027, waveform e lote setembro | Limpeza, referencia/montagem e [caso CapCut](../casos/rugido-cortes-capcut.md) |
| Rugido: H005 export, capcut-layout-export e protecao da timeline no SKILL | CapCut editavel e entrega/QA |
| Rugido: H001 titulo/export e regras de titulo/legenda do SKILL | Metodo Lucas, caso CapCut e [Legendas do audio final](legendas-audio-final.md) |
| cortes-rugido e Aula Segunda aprovada: tese, ritmo 1.15x contextual, layout e copy | [Metodo Lucas](../casos/rugido-lucas-felix.md) |
| mapeamento-ganchos-brutos e cortes-de-live: atlas, cobertura, buildability, curadoria | [Atlas e curadoria](gancho-atlas-e-curadoria.md) |
| capcut-legendas-rugido: retiming, ordem editorial, bloco de sentido, TASA Orbiter Bold | [Legendas do audio final](legendas-audio-final.md) e metodo Lucas |
| capcut-legendas-autoral: ataque/cauda acusticos e segmentacao semantica/prosodica | [Legendas do audio final](legendas-audio-final.md), sem transferir estilo visual de outra marca |
| descricao-video-tese: titulo/copy de publicacao versus legenda na tela | Metodo Lucas; regra de publicacao permanece no projeto |
| criado-editor local/global e piloto Rugido | [Operacao Criado](criado-operacao-mcp.md) e [Criado/FFmpeg](criado-ffmpeg-editavel.md); programar app e outra tarefa |
| Evals das tres fontes e falhas desta integracao | Cenarios de regressao em evals/evals.json |

## Resolucao de Diferencas

- CapCut e Criado sao caminhos de edicao atuais, nao eras sucessivas. FFmpeg e
  motor de processamento/exportacao e pode ser usado diretamente para MP4
  avulso. O editor escolhido e a entrega solicitada pelo usuario prevalecem.
- A biblioteca geral nao impoe prazo, duracao, vertical, fonte ou titulo. As
  preferencias Rugido ficam no caso, ativadas pelo briefing correspondente.
- Mais microcortes no H006 e menos no H027 resolvem problemas distintos. Decida
  por silencio real e continuidade, nao pelo numero de cortes do exemplo.
- Cauda/ataque simultaneos sao desejados no overlap fonetico; o erro e antecipar
  silabas fortes ou duplicar source, nao a mera entrada antes do fim anterior.
- Intermediarios de FFmpeg podem facilitar export; nao substituem fontes completas
  num projeto prometido como editavel. Nao expandir edicao de video para desenvolver
  um editor sem que esse desenvolvimento esteja no escopo.
- Nova versao e correcao no mesmo MP4 sao convencoes de entrega diferentes.
  Siga a convencao do usuario com backup recuperavel, preservando trabalho humano.
- Conteudo herdado relata evidencias historicas. Abrir arquivos de skill e
  validar JSON/links nao equivale a reabrir todos os drafts ou ouvir as fontes.

Mantenha o conhecimento em seu modulo responsavel, com rotas explicitas no
SKILL.md. Consulte [Evoluir a biblioteca](evoluir-biblioteca.md) para novos casos;
nao replique os SKILL.md inteiros nem exija caminhos locais de outra instalacao.
