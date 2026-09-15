# Origem e Integracao dos Cortes

Use ao manter a biblioteca integrada. Consolidacao solicitada pelo usuario em
15/09/2026 a partir de cortes-base, capcut-cortes-base e capcut-cortes-rugido.
As skills de origem continuam intactas; estes modulos e o script incluido
permitem usar edicao-video-ia isoladamente. Nao ha sincronizacao automatica de
futuras mudancas nas fontes: compare conteudo e evidencia ao incorporar revisoes.

## Mapa de Conhecimento

| Origem consultada | Destino mantido nesta skill |
| --- | --- |
| cortes-base/SKILL e capcut-cortes-base/SKILL: escopo, limpeza, cronologia, mapa, escadinha | [Limpeza e cadencia](../tecnicas/limpeza-e-cadencia.md) |
| Ambas: audio-waveform-e-fonetica, microcortes-e-continuidade, refino-fonetico-por-emenda | [Referencia e montagem](../tecnicas/referencia-e-montagem.md), limpeza e QA |
| Ambas: exportacao-e-qa | [Entrega e QA](entrega-e-qa.md) |
| Ambas: capcut-draft-editavel; cortes-base: capcut-engenharia-reversa-json | [CapCut editavel](capcut-editavel.md) |
| cortes-base: criado-ffmpeg-timeline | [Criado e FFmpeg](criado-ffmpeg-editavel.md) |
| scripts/analisar_waveform_silencios.py das bases | Script local incluido, com validacao de parametros; uso em limpeza e cadencia |
| Rugido/SKILL, H004/H005 e H020: tese, ponte, declarativa, fechamento | [Cortes de live por tese](../estilos/cortes-live-por-tese.md) |
| Rugido: H001 overlap, H006/H009/H010/H014/H015/H016/H027, waveform e lote setembro | Limpeza, referencia/montagem e [caso Rugido](../casos/rugido-cortes-capcut.md) |
| Rugido: H005 export, capcut-layout-export e protecao da timeline no SKILL | CapCut editavel e entrega/QA |
| Rugido: H001 titulo/export e regras de titulo/legenda do SKILL | Caso Rugido e [Legendas do audio final](legendas-audio-final.md) |
| Evals das tres fontes e falhas desta integracao | Cenarios de regressao em evals/evals.json |

## Resolucao de Diferencas

- O padrao Criado de uma fonte e o padrao CapCut de outra sao opcoes de execucao;
  o editor escolhido e a entrega solicitada pelo usuario prevalecem.
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
