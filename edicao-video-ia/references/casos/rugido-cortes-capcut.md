# Caso Rugido: Cortes no CapCut

Conhecimento integrado de `capcut-cortes-rugido`, incluindo sua entrada e as
16 referencias operacionais consultadas. Os estados e aprovacoes abaixo foram
relatados nas fontes; os drafts antigos nao foram reabertos nesta integracao.
Nao inclui midias, caminhos privados ou ativos de fonte. Use quando o briefing
pedir Rugido/CPL ou esses exemplos, nunca como padrao global da biblioteca.

## Linguagem e Processo

Para esses cortes, seguir [Cortes de live por tese](../estilos/cortes-live-por-tese.md):
gancho aprovado, problema, mecanismo, exemplo/prova e payoff. Mapear o corpo
antes de montar; selecionar ou garimpar gancho e uma etapa distinta de executar
um corte ja escolhido. A fala deve avancar na cronologia e manter sentido fora
da live. Pergunta/chat podem sair quando a resposta declarativa resolve; uma
ponte curta pode ficar quando amarra o dado ou a conclusao.

No fluxo Rugido, a referencia operacional evoluiu para cerca de 1-2 minutos,
ideal perto de 1min30s. Nao e teto rigido: ha exemplos aprovados acima de dois
minutos e menores que um minuto quando a tese fecha. O antigo piso de 40 s e
excecao contextual, nao alvo. Nao corte conclusao nem complete com fala irrelevante
para atingir a faixa. A duracao solicitada no projeto prevalece.

Fazer a passada de cadencia antes de legenda/titulo quando a montagem ainda
parece live. Rever inicio, espera interna e final sem aplicar overlap uniforme
nem picotar fala continua. Use [Limpeza e cadencia](../tecnicas/limpeza-e-cadencia.md)
e [Referencia e montagem](../tecnicas/referencia-e-montagem.md).

## Projeto e Aparencia

- Quando pedir editavel Rugido no CapCut, manter o mesmo projeto ja trabalhado,
  com backup tecnico e microcortes protegidos em compostos. Separar bloco estavel
  e trecho em ajuste; preservar compostos humanos aninhados. Confirmar e desligar
  adsorcao/reorganizacao que desmonte a montagem, conforme o schema observado.
- Nome curto por aula/campanha e gancho, como `CPL 01 - H005`; titulo, tese e
  descricao ficam nos registros, nao no nome do projeto. Status visual por fase
  somente se o usuario pedir organizacao: azul para corte, amarelo para legenda,
  concluido para titulo/finalizado. Nao impor renomeacao fora desse escopo.
- Para o padrao Story/Reels, canvas 1080x1920; live horizontal proporcional no
  meio, sem esticar, com area superior para titulo e inferior para legenda.
  Ler posicoes reais do draft, pois formato sozinho nao fixa composicao.
- Legenda pelo audio final, AssemblyAI conforme autorizacao do trabalho, textos
  editaveis de uma linha. Nao usar auto-caption do CapCut no lugar do fluxo
  escolhido. A referencia amarela usa cerca de 27 caracteres como heuristica;
  casos humanos chegaram a 29. A linha visual e o sentido mandam no agrupamento.
- Titulo complementar ao gancho, curto e sem caixa alta inteira por padrao.
  Se a escolha estiver pendente, apresentar tres opcoes antes de aplicar; uma
  escolha ou autorizacao editorial ja dada dispensa pedir a mesma aprovacao.
  Usar curiosidade ou loop conforme o payoff, nao apenas nomear o assunto.
- O padrao de titulo observado e branco, Aveny T WEB quando disponivel e
  autorizada, PNG transparente recortado justo, 2-4 linhas e entrelinha fechada
  sem colisao. Fundo/faixa so quando solicitado. Aspas indicam fala citada de
  cliente/publico; nao transformar essa fala em afirmacao editorial propria.
- No exemplo H001, PNG 459x217 a escala 1.45 ocupou cerca de 666x315, com
  transform x=0/y=0.56. H014/H005 ficaram perto de 650-770 px de largura exibida.
  Sao referencias daquele canvas; medir apos escala e conferir visualmente,
  sem reutilizar percentual de outro PNG ou impor essa geometria a outra marca.

Para estrutura, materiais compartilhados e export de compostos, leia
[CapCut editavel](../fluxos/capcut-editavel.md). Para retiming e blocos de uma
linha, leia [Legendas do audio final](../fluxos/legendas-audio-final.md).

## Refinamentos que Mudaram as Decisoes

| Fonte operacional | Conhecimento preservado e condicao |
| --- | --- |
| H004 | O gancho nao limita o corte a uma janela; composto final pode conter blocos/microcortes e velocidade global. Exportar sem mudar live, titulo ou legenda. |
| H005 refinamento | Guardar corpo humano aprovado, ajustar final em outro composto; remover pergunta redundante e exemplo lateral, preservando ponte e cadeia logica. |
| H005 export + layout | Subdrafts podem estar no indice global e ser referenciados por extra_material_refs; transform normalizada usa metade do canvas no caso simples. |
| H001 overlap adaptativo | Emendas diferentes pedem overlaps diferentes; o caso variou aproximadamente de 28 a 395 ms. Nao copiar mediana ou 350 ms como regra. |
| H001 titulo/export | PNG recortado pode ficar pequeno com escala herdada; avaliar largura exibida, nao so entrelinha ou percentual da interface. |
| H006 cadencia final | Mesma tese/duracao pode exigir mais cortes internos; caso passou de 33 para 55. Isso justifica segunda passada, nao uma quota de cortes. |
| H009 fade-in/out | Avaliar saida e entrada como par; poucos clipes podem receber ambos os fades, isolando material compartilhado. Draft travado foi apenas lido. |
| H014 waveform/fade | Candidatos automaticos ainda exigem selecao; remover microcortes sem funcao, aplicar fade pontual e verificar campo real no material. |
| H010 gaguejo/cauda | Limpar falso arranque inicial; encaixar proxima fala na cauda e estender conclusao quando necessario. Ajuste posterior invalidou legendas apesar de texto/duracao semelhantes. |
| H015 ponte | Remover palavra duplicada e espera sem apagar ponte; puxar sucessores pela ordem editorial, incluindo os que sobrepoem o fim antigo. |
| H016 entrada | Palavra curta precisa de pre-ataque; silencio longo nao e margem. Fade deve existir no material e nao apagar a primeira silaba. |
| H020 fechamento | Preservar o ultimo exemplo que muda a conclusao; reduzir overlap agressivo em fala quase continua, aceitando aumentar duracao para fechar tese. |
| H027 continuidade | Unir/estender frases fluidas reduziu friccao e microcortes; nem toda pequena baixa de energia pede overlap. |
| Lote H010/H019/H024/H026/H032 | Draft humano recente e a referencia do estado aprovado; rever emendas, inicio e final, depois resincronizar legenda e conferir escala do titulo. |
| Waveform operacional | RMS marca candidatos; sons fracos, respiracao e intencao ainda decidem. Sobrepor cauda e ataque, sem duas copias do source. |

As duracoes historicas de fades/overlaps nao se tornam minimos ou maximos globais.
O aprendizado mais recente de bico sobre cauda complementa esses casos em
[Convite em duas cameras](convite-duas-cameras.md).

## Entrega

Preservar o arquivo/draft escolhido pelo usuario. Se ele pedir correcao no mesmo
export, substituir apenas apos QA, com recuperacao da versao anterior; evitar
nomes repetidos de final e clones visiveis. Se pedir novas versoes, manter essa
convencao. Render intermediario nao substitui as fontes do editavel.

Entregar draft, MP4, mapa e transcricao conforme o escopo, indicando o que abriu,
foi visto, ouvido ou medido. Nao publicar nem mover para pasta de postagem por
inferir que um export foi aprovado. Esta integracao documenta o processo;
nao representa uma nova validacao perceptiva de todos os casos historicos.
