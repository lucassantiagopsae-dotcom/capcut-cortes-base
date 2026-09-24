# Limpeza e Cadencia

Motor tecnico integrado de cortes-base, CapCut Cortes Base e refinamentos Rugido.
Nao define duracao, marca, formato, titulo, legenda ou publicacao.

## Escolher a Intervencao

Identifique se o pedido e limpeza de erros, compactacao, recorte de conteudo,
refino de uma montagem humana ou somente exportacao. Preserve a cronologia;
reordenar falas exige briefing que autorize isso. Remova repeticao sem valor,
falso arranque, gaguejo e espera que prejudicam o objetivo; nao remova uma pausa
expressiva apenas porque ela tem pouca energia.

Separe selecao de conteudo e passada de cadencia. Quando a ideia esta correta,
ajuste as emendas antes de buscar outra tese. Um trecho longo pode precisar de
divisao em clausulas; uma frase que ja flui pode precisar da remocao de cortes.
Quantidade de microcortes, duracao mediana e ausencia de gaps nao provam ritmo.
Atencao especial ao inicio, onde falso arranque e palavra curta mordida ficam
evidentes, e ao final, onde uma cauda pode introduzir o comeco de outro assunto.

Uma resposta declarativa pode substituir pergunta/espera de chat se preservar
o sentido. Guarde a menor frase-ponte que explica a entrada de grafico, dado ou
conclusao. Se a ponte trouxer a ultima palavra da fala anterior repetida, retire
a repeticao e a pausa escondida, mantendo a ponte util.

## Decidir por Emenda

Leia [Referencia e montagem](referencia-e-montagem.md) para bico, cauda, waveform
e sobreposicao. Para cada transicao, escolha manter, estender fala continua,
mover bordas, remover vazio ou sobrepor margens foneticas. Confira ambos os lados
e tambem o material descartado. Nao force a segunda tentativa como correta.

Em fala comercial compacta, uma emenda pode ganhar continuidade quando o ataque
da proxima take entra durante a cauda de baixa energia da anterior. Aplique isso
por juncao e por fonema: preserve a palavra inteira, evite duas silabas fortes ao
mesmo tempo e mantenha voz em faixas simultaneas durante o overlap real. O caso
DD Prime aprovou overlaps curtos de 30-40 ms em quatro juncoes e nenhum overlap
nas duas entradas finais; esses numeros sao evidencia daquele audio, nao receita.
O corte visual pode cair no meio do room tone sobreposto, desde que boca, gesto e
continuidade nao denunciem a troca.

Palavras curtas no ataque requerem margem real antes do som; pre-silencio longo
nao e margem fonetica. Uma palavra curta seguida de espera e depois outra frase
pode exigir dois clipes, em vez de eliminar a palavra curta. Na saida, retire
apenas a sobra que comeca outro assunto, sem reduzir caudas do projeto inteiro.

Se houver estalo ou fala adiantada, investigue source duplicado, corte desnecessario
e overlap cedo demais antes de adicionar fade. Um clipe entre duas emendas pode
precisar de fade de entrada e saida distintos; a maioria nao precisa de efeito.
Leia as duracoes com a unidade correta: em timecode com frames a 30 fps, seis
frames equivalem a 0.20 s, nao a seis milissegundos. Isso nao e limiar de corte.

## Recalcular a Timeline

Mantenha uma ordem editorial explicita, distinta da ordem de tracks ou camadas.
Ao encurtar um clipe com overlap, nao desloque apenas os itens com
`start >= fim_antigo`: o proximo pode comecar antes desse fim justamente pela
sobreposicao. Recalcule todos os sucessores pertencentes ao fluxo de fala,
preservando as relacoes de overlap/gap intencional, e remapeie as outras camadas.

Verifique `gap = inicio_seguinte - fim_atual`: positivo e espera, negativo e
sobreposicao. Em bloco compactado, procure gaps artificiais; nao zere pausas
intencionais em outro estilo. Confira referencias de source sobrepostas para
evitar duas copias da mesma fala. Atualize duracoes de compostos, segmentos pais
e projeto, bem como legendas; duracao total quase igual nao prova timing igual.

Quando houver overlaps editaveis, organize faixas em escadinha se isso facilitar
a revisao, sem transformar a organizacao em corte visual automatico. Preserve
blocos humanos estaveis e trabalhe o trecho instavel separado quando util.

## Analisador Local

O script incluido usa Python e FFmpeg para calcular RMS por janela e produzir
JSON, CSV e Markdown com candidatos de baixa energia. Nao faz transcricao nem
edita o video. Exemplo de uso a partir da pasta da skill:

```powershell
python scripts/analisar_waveform_silencios.py "video.mp4" --start 00:01:00 --end 00:01:15 --window-ms 5 --out-dir "analise"
```

Escolha janela, limiar e duracao minima pela fonte. Os valores de CLI sao apenas
parametros iniciais; ruido, fricativas e respiracao exigem interpretacao. Os
spans de saida usam tempos absolutos da fonte, incluindo o offset de `--start`.
Nao envie audio a outro servico por causa da existencia de uma chave: respeite
a escolha e a autorizacao ja dadas no trabalho atual.

Para entregas curtas de Instagram/Reels, rode tambem a auditoria no MP4 final:

```powershell
python scripts/auditar_cadencia_reels.py "pasta-da-entrega" --output "qa-cadencia.json"
```

Na referencia Lucas/Rugido, spans internos de baixa energia a partir de `0.60 s`
exigem revisao e spans a partir de `0.90 s` bloqueiam a entrega ate escuta ou
correcao. Esses limiares sao um gate de triagem para fala pausada em video curto,
nao autorizacao para apagar automaticamente respiracao, enfase ou pausa expressiva.
Se uma pausa bloqueada for mantida, registre o motivo editorial no QA.

## Cobertura

Se o pedido cobre todos os takes, registre cada emenda e extremidade, incluindo
decisoes de manter ou desfazer cortes. Comeco, transicoes e fim sao prioridades,
nao substitutos para cobrir o restante. Compare o draft humano mais recente com
o backup para entender as decisoes, sem reverter a versao humana. Diferencie
varredura tecnica, ajuste individual e escuta conforme [Entrega e QA](../fluxos/entrega-e-qa.md).
