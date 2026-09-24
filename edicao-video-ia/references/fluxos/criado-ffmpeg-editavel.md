# Criado e FFmpeg Editavel

Use quando o usuario escolher Criado, ja houver projeto nele, ou solicitar um
MP4 local gerado com FFmpeg. Nao migre um draft CapCut ou outro editor por
preferencia da skill. Um MP4 solicitado isoladamente nao exige criar editor.

## FFmpeg sem projeto Criado

Quando a entrega e so um arquivo local, monte um mapa reproduzivel com fonte,
in/out, ordem, velocidade, audio, transformacoes, legenda e titulo conforme o
escopo. Renderize com FFmpeg, preserve originais e confira o MP4 final. Nao
prometa uma timeline editavel que nao foi criada. Se o usuario pedir editavel
posteriormente, converta o mapa em camadas no editor escolhido, sem usar o MP4
final como unica fonte.

## Fonte de Verdade no Criado

O projeto parametrico e a fonte de verdade; MP4 e derivado. Importe a midia
completa e represente cada corte com referencia a fonte, in/out, inicio/duracao
na timeline, faixa, velocidade, volume e fades, mais transformacoes e texto
quando existirem. Use o schema/API vigente do ambiente; esse e um modelo mental,
nao um contrato de campos universais.

Para descobrir a interface, localize o aplicativo/projeto escolhido pelo usuario,
leia suas instrucoes locais e procure documentacao, exemplos de projetos salvos
e comandos de importacao/exportacao existentes. Se houver codigo disponivel,
identifique o parser/serializador da timeline e os testes antes de escrever.
Compare um projeto minimo salvo pelo proprio editor com a estrutura atual;
teste uma alteracao reversivel numa copia tecnica e reabra-a. Nao invente URL,
porta ou endpoint. Sem interface confirmada, registre o mapa de cortes e informe
o bloqueio da aplicacao, sem chamar esse mapa de projeto editavel entregue.

Nao pre-renderize cada corte para substituir a fonte no projeto: arrastar a
borda deve poder recuperar a fala e sua margem original. Caches temporarios de
render nao substituem editabilidade. Texto queimado ou um MP4 unico importado
nao equivalem a camadas editaveis de legenda, titulo, fala e efeitos.

Se o recurso necessario nao existe no editor, procure representacao suportada e
informe o limite. Se o pedido exige uma edicao editavel no Criado e a funcao
ausente e indispensavel, confirme o escopo tecnico do projeto antes de
implementa-la de forma delimitada. Um pedido apenas de MP4 nao autoriza criar
controles, API ou efeitos no aplicativo.

## Aplicacao

1. Leia projeto e alteracoes humanas, salve revisao e identifique escopo.
2. Use [Limpeza e cadencia](../tecnicas/limpeza-e-cadencia.md) e
   [Referencia e montagem](../tecnicas/referencia-e-montagem.md) para as bordas.
3. Atualize parametros e mapa da timeline, mantendo originais recuperaveis.
4. Garanta que preview e export interpretem os mesmos offsets, overlaps, ganho,
   fades, velocidade e transformacoes. Uma mudanca invalida QA da parte afetada.
5. Reabra o projeto, confira controles editaveis e compare o arquivo final quando
   houver exportacao. Declare quais efeitos precisaram ser renderizados.

Um projeto sem trilha ou efeitos nao precisa receber essas camadas. Uma entrega
somente de draft nao exige MP4 final. Para dados e verificacoes, consulte
[Entrega e QA](entrega-e-qa.md).
