# Evoluir a Biblioteca

Use quando o usuario pedir para ensinar um estilo, registrar uma tecnica ou
incorporar feedback. A skill nao treina o modelo nem persiste conversas sozinha:
o aprendizado reutilizavel precisa ser escrito, revisado e salvo nos arquivos.
Atualizar localmente nao autoriza publicar ou fazer push automaticamente.

## Classificar Antes de Escrever

| Natureza do aprendizado | Destino |
| --- | --- |
| Mecanismo que serve a varios formatos, como preservar caudas | `references/tecnicas/` |
| Linguagem editorial recorrente, como depoimentos de abertura | `references/estilos/` |
| Preferencia de cliente, marca ou decisao de uma versao | `references/casos/` |
| Procedimento de revisao, entrega ou manutencao | `references/fluxos/` |

Primeiro procure um modulo existente. Atualize-o se o criterio for o mesmo; crie
outro quando houver uma diferenca real de objetivo, selecao ou linguagem, nao
somente outra cor, cliente ou ferramenta. Nao crie pastas vazias para estilos que
ainda nao foram trabalhados.

## Registrar o Que Foi Aprendido

Extraia do material e do feedback: problema observado, decisao adotada, motivo,
quando se aplica, quando nao se aplica e evidencia disponivel. Separe:

- Pedido do usuario: o criterio solicitado.
- Implementacao: o que foi realmente alterado.
- Verificacao: o que foi medido, visto em movimento ou ouvido.
- Aprovacao: somente o que o usuario de fato aprovou.

Nao converta um render bem-sucedido em aprovacao estetica nem uma sugestao em
regra definitiva. Ao revisar uma regra antiga, preserve a intencao e explique a
condicao que mudou; prefira resolver a contradicao a acumular instrucoes opostas.

Se o Criado registrar uma sessao, use historico de acoes, timeline antes/depois,
estado final, anotacoes e confirmacao humana como evidencias complementares.
Um diff de `duration` isolado nao demonstra motivacao editorial. Associe a
regra candidata ao video/modelo/grupo, versao, fonte, intervalos, acao,
intencao inferida, excecoes e resultado observado. Distinga inferencia da fala
explicita do usuario. Reforce uma regra existente quando for o mesmo criterio;
nao crie uma skill por video ou por revisao. So promova uma preferencia local
para tecnica geral quando houver evidencia de transferencia para outros casos.

## Adicionar um Estilo

Crie um arquivo em `references/estilos/` com nome claro e conteudo sustentado pelo
trabalho: quando usar, objetivo, criterios de montagem/ritmo, linguagem de som e
imagem, limites e verificacoes caracteristicas. Linke tecnicas existentes em vez
de copia-las. Mantenha exemplos especificos em `references/casos/`.

Acrescente a rota em `SKILL.md`, com uma frase que permita distingui-lo dos estilos
vizinhos. Crie um cenario de regressao em `evals/evals.json` que represente uma
decisao real e um caso que nao deva receber aquele estilo. Evite uma lista de
efeitos obrigatorios sem relacao com a narrativa.

Os modulos sao lidos por instrucao da entrada geral; nao dependem de descoberta
recursiva de arquivos `SKILL.md`. Se um modulo futuramente precisar de invocacao,
ferramentas e distribuicao proprias, extraia-o como skill independente, mantenha
a rota explicita e verifique sua disponibilidade no destino. Um plugin pode
agrupar skills independentes, mas nao e necessario para estes modulos internos.

## Validar e Entregar

Confira frontmatter, links relativos e portabilidade da skill instalada sozinha.
Revise os cenarios pertinentes; diferencie cenarios escritos de testes realmente
executados. Nao publique videos, dados privados, chaves, links de acesso ou ativos
licenciados ao transferir aprendizado para um repositorio publico.

Preserve alteracoes locais e historico. Ao renomear, atualize nome, pasta, prompt,
documentacao e referencias; evite duas copias ativas divergentes. Confirme conta
e repositorio antes de um push autorizado, seguindo as regras locais de GitHub.
Na entrega, diga qual modulo mudou e o alcance da validacao, sem prometer que a
skill domina estilos que ainda nao foram ensinados.
