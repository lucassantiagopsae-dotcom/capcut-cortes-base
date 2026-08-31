# Draft Editavel no CapCut

Use esta referencia quando a tarefa envolver CapCut diretamente.

## Antes de mexer

Quando editar um projeto existente:

1. identifique a pasta do draft;
2. confira se existe sinal de projeto aberto/travado;
3. salve backup tecnico;
4. entenda o que o usuario ja editou;
5. preserve ajustes humanos;
6. trabalhe no mesmo projeto quando o usuario pedir isso.

Crie copia apenas quando:

- o usuario pedir;
- o projeto estiver travado;
- houver risco real de corromper;
- a mudanca for experimental e reversibilidade for importante.

## Nao impor layout

Esta skill nao define formato. Antes de alterar canvas ou posicao:

- leia o `canvas_config`;
- veja a proporcao original;
- preserve escala e transform dos clipes existentes;
- siga o briefing do projeto;
- se outra skill definir layout, siga a outra skill.

Nao transforme tudo em vertical por padrao.

## Timeline principal

Para cortes simples, a timeline pode continuar simples.

Para muitos microcortes:

- mantenha microcortes dentro de composto;
- deixe a timeline principal com poucos blocos;
- precomponha blocos estabilizados;
- preserve compostos criados pelo humano quando ajudam organizacao;
- evite deixar dezenas de microcortes soltos se o CapCut puder reorganizar.

## Ima, snap e organizacao automatica

Quando campos equivalentes existirem no draft, evite que o CapCut puxe clipes para o inicio ou reorganize camadas automaticamente.

Campos que podem aparecer em drafts:

- `config.maintrack_adsorb`;
- `render_index_track_mode_on`;
- configuracoes de organizacao automatica de camada.

Nao force valores se nao souber o efeito no projeto. Mas quando houver microcortes sobrepostos e risco de desmontar a timeline, desligar esses comportamentos costuma proteger a edicao.

## Materiais compartilhados

Em CapCut, varios segmentos podem apontar para o mesmo material.

Antes de aplicar fade, volume, transform ou corte que deveria ser local:

- veja se o `material_id` e compartilhado;
- se for compartilhado, isole o material do segmento quando necessario;
- valide que a mudanca nao espalhou para o clipe inteiro.

## Mapa de edicao

Quando alterar draft por JSON, salve um mapa junto do backup:

- draft alterado;
- arquivo de backup;
- clipes mexidos;
- tempos antes/depois;
- fades aplicados;
- riscos ou pontos para revisao.

O mapa permite que o humano entenda o que mudou sem abrir cada detalhe do JSON.

