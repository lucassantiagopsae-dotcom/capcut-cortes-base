# Caso: Convite em Duas Cameras

Registro de uma revisao aprovada pelo usuario em 15/09/2026. Exemplo anonimizado,
sem midias, transcricao integral, caminhos locais ou dados de acesso. O caso
sustenta as tecnicas abaixo; nao cria um preset para todos os talking heads.

## Pedido

Entregar primeiro um MP4 para avaliacao, sem projeto editavel nesta etapa.
Usar a skill de cortes como motor tecnico e AssemblyAI para timestamps, conforme
escolha explicita do usuario. Os angulos registravam a mesma fala simultaneamente;
acompanhar a camera a que a pessoa se dirigia. Manter legenda abaixo do queixo,
na regiao da clavicula/alto do peito, tratar o ruido da sala com moderacao e
aplicar velocidade final de 1.13x, preservando pitch.

## Problemas e Decisoes

- A semelhanca entre transcricoes foi inicialmente confundida com repeticao de
  takes. A comparacao confirmou angulos simultaneos. O offset usado foi 6.750 s;
  uma verificacao local no fechamento estimou 6.740 s por envelope de energia,
  com correlacao aproximada de 0.83. Isso nao prova deriva nula em toda a gravacao.
- Um olhar lateral foi interpretado como consulta/leitura. As duas vistas
  mostraram fala dirigida a outra camera. A montagem passou a considerar ambas.
- A entrada de uma palavra foi cortada perto demais. O usuario aprovou a revisao
  com margem de ataque; timestamps deixaram de ser tratados como bordas finais.
- A revisao literal de cada microdesvio criou voltas breves de camera no convite.
  O usuario rejeitou o picote. A versao aprovada sustenta mais a segunda camera
  durante a unidade de fala e retorna a frontal no encerramento.
- Um descarte anterior atravessava palavras de ligacao, embora a legenda ainda
  as exibisse. Nova transcricao localizada e waveform levaram a recuperar a fala.
- Encurtar uma pausa sem overlap nao satisfez o refino desejado. O usuario pediu
  explicitamente que o bico seguinte entrasse enquanto a cauda anterior decaia.

## Implementacao Aprovada

| Emenda | Fim anterior na fonte | Inicio seguinte na fonte | Overlap antes da aceleracao |
| --- | --- | --- | --- |
| vem / aprender | 60.370 s | 61.115 s | 75 ms |
| soltos / em um funil | 63.150 s | 63.585 s | 90 ms |

As duas faixas de audio se sobrepoem de fato, com soma sem normalizacao automatica.
Foram usados fades de entrada de 5 ms e saida de 15 ms, escolhidos para proteger
as bordas inspecionadas. A fricativa final de "soltos" foi preservada; um limiar
unico de silencio teria perdido informacao relevante. Esses tempos sao exemplos
deste material, nao limites nem recomendacao universal.

O corte de imagem ficou no meio de cada sobreposicao sonora, sem dissolve do
rosto. A timeline e as legendas foram recalculadas; os overlaps na entrega a
1.13x correspondem a cerca de 66 ms e 80 ms. O resultado manteve audio de uma
camera e legenda amarela na posicao aprovada. Tratamento leve de ruido,
equalizacao e compressao nao foi certificado como eliminacao da reverberacao.

## Evidencia e Aprovacao

- Inspecao do agente: sequencias de frames das duas cameras, waveform de bordas,
  energia de altas frequencias, faixas sobrepostas e soma, transcricao AssemblyAI.
- Verificacao tecnica: render decodificado sem erros, 1080x1920 a 30 fps,
  aproximadamente 51.60 s; picos medidos sem clipping nas emendas.
- Limite: o agente nao fez escuta direta. Medicoes e imagens nao foram chamadas
  de aprovacao perceptiva nem de revisao em movimento.
- Aprovacao humana: apos receber a versao com as duas sobreposicoes, o usuario
  a aprovou explicitamente e pediu registrar os aprendizados nesta skill.

Para reutilizar, leia [Multicamera por direcao do olhar](../tecnicas/multicamera-por-olhar.md)
e [Referencia e montagem](../tecnicas/referencia-e-montagem.md). Leve os criterios
de decisao; nao imponha AssemblyAI, 1.13x, legenda amarela, posicao ou duracoes de
overlap a outro cliente sem briefing que os determine.
