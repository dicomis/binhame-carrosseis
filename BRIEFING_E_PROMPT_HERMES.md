# Projeto Binhame: briefing completo e prompt para o Hermes Agent

**Clínica de Odontologia Binhame | Dr. Tiago Binhame, cirurgião-dentista | Santo André, SP**
Documento criado em 15/10/2026. Reúne tudo o que foi construído até agora (site, identidade visual, 7 carrosséis) e o prompt para o Hermes Agent criar uma fábrica de carrosséis.

---

## Índice

0. Como usar este documento
1. Resumo do projeto e linha do tempo
2. O cliente: dados da clínica e pendências
3. Identidade visual
4. Tom de voz, regras de texto e engajamento
5. Anatomia do carrossel (formato, tipos de slide, arquivo de conteúdo)
6. Carrosséis já produzidos e banco de temas
7. Como foi construído (e o que aprendemos errando)
8. Regras de conteúdo e conformidade
9. Roadmap das fases
10. **O PROMPT para o Hermes Agent**
- Apêndice A: exemplo completo de arquivo de conteúdo
- Apêndice B: checklist de revisão do Dr. Tiago
- Apêndice C: pendências com o cliente
- Apêndice D: glossário em linguagem simples
- Apêndice E: mapa dos arquivos do pacote

---

## 0. Como usar este documento

Este documento tem duas funções ao mesmo tempo: **contexto** (seções 1 a 9) e **instrução** (seção 10, o prompt).

**Passo a passo para criar o agente:**

1. Abra o Hermes Agent e **anexe a pasta inteira do pacote** (este documento + as pastas `assets`, `engine`, `specs`, `exemplos`, `referencias`, `site`). Se o Hermes só aceitar arquivos soltos, anexe pelo menos: este documento, `assets/`, `engine/` e `specs/`.
2. **Cole o texto da seção 10** (o bloco do prompt) na conversa com o Hermes. Ele já manda o Hermes ler o resto do documento.
3. **Responda às perguntas** que o Hermes fizer. Ele foi instruído a perguntar em linguagem simples, uma de cada vez, sempre com opções e uma recomendação. Se não souber responder, diga "você escolhe".
4. Ao final da Fase 1 você terá um agente que recebe um tema e devolve o carrossel pronto.

> **Importante:** este documento foi escrito por uma IA (Claude) a partir de uma sequência de conversas. Os itens marcados como "a confirmar" dependem do Dr. Tiago. O conteúdo clínico dos carrosséis deve ser revisado por ele antes de qualquer publicação.

---

## 1. Resumo do projeto e linha do tempo

**Objetivo geral:** dar à Clínica de Odontologia Binhame uma presença digital profissional, acessível e descontraída, e transformar isso em captação de pacientes em Santo André e região.

**O que já existe:**

| # | Entrega | Situação |
|---|---------|----------|
| 1 | **Landing page** (um único arquivo HTML) com apresentação da clínica, tratamentos, primeira consulta, Dr. Tiago, dúvidas, contato e mapa | Pronta. Falta publicar e preencher pendências (CRO, horários) |
| 2 | **Identidade visual derivada do logo** (verde-oliva + dourado) | Definida (seção 3) |
| 3 | **Foto do Dr. Tiago** recortada a partir de prints do Instagram | Provisória. Qualidade limitada; ideal trocar por foto original |
| 4 | **7 carrosséis para Instagram** (1080×1350) | Prontos, aguardando revisão técnica do Dr. Tiago |
| 5 | **Gerador de carrosséis** (programa que transforma um arquivo de texto em imagens) | Pronto e testado (`engine/`) |
| 6 | **Este briefing + prompt para o Hermes** | Este documento |

**Linha do tempo resumida:**

1. Pedido inicial: landing page para a clínica do Dr. Tiago, com pesquisa de referências de clínicas de São Paulo, tom profissional mas descontraído, visual moderno e baseada no logo.
2. A pesquisa de referências trouxe sobretudo diretórios e anúncios. O padrão que se repete nas clínicas de São Paulo: ambiente moderno e tecnológico, foco na experiência do paciente, avaliações, localização fácil e agendamento rápido. A página foi desenhada a partir disso.
3. Foram enviados dois prints do Instagram do Dr. Tiago. Deles saíram: a confirmação de que ele trabalha com **clareamento**, a foto dele e o alerta sobre a **oferta "avaliação gratuita"** (ver seção 8).
4. Foi criado o primeiro carrossel (mitos do clareamento). O primeiro desenho confundia o leitor (a afirmação errada aparecia em destaque com "Verdade" logo abaixo). **Foi refeito** com mito riscado e etiquetas claras.
5. Foram criados mais 6 carrosséis, formando uma sequência conectada (seção 6).
6. Foi criado o gerador reutilizável e este documento.

---

## 2. O cliente: dados da clínica e pendências

| Campo | Valor |
|-------|-------|
| Nome no logo | Clínica de Odontologia Binhame |
| Nome nos posts do Instagram | Clínica Odontológica Binhame (sigla COB) |
| Profissional | Dr. Tiago Binhame, cirurgião-dentista |
| Endereço | Av. Eduardo Prado, 575, Santo André, SP |
| Telefone / WhatsApp | (11) 94046-3921 |
| Link de WhatsApp | `https://wa.me/5511940463921` (aceita `?text=` com mensagem pronta) |
| Cidade/região de atuação | Santo André e Grande ABC |

**Pendências que dependem do Dr. Tiago (nada disso foi inventado):**

- Número do **CRO-SP** (obrigatório na identificação; no rodapé do site está como `CRO-SP nº [inserir número]`).
- **@ do Instagram** e demais redes.
- **Horários de atendimento** (hoje o site diz "combinados pelo WhatsApp").
- **Serviços confirmados.** Confirmados por posts: clareamento e cirurgia. A confirmar: limpeza, restaurações, implantes, estética, ortodontia, atendimento infantil.
- **Nome oficial a usar** ("de Odontologia" no logo ou "Odontológica" nos posts).
- **Foto original** do Dr. Tiago (de preferência em pé, fundo liso, boa luz, arquivo direto da câmera, não de WhatsApp).
- **Paleta:** o Instagram dele usa verde-azulado (teal) e uma versão azul-esverdeada do logo (COB). O trabalho seguiu o logo enviado (verde-oliva e dourado). Decidir se o Instagram será atualizado para a mesma paleta.
- **Oferta "avaliação gratuita":** ver seção 8; recomenda-se **não usar**.

---

## 3. Identidade visual

### 3.1 O logo
Círculo verde-oliva com texto em arco: "CLÍNICA DE ODONTOLOGIA BINHAME" em cima e "DR. TIAGO BINHAME DENTISTA CIRURGIÃO" embaixo, em tipografia serifada clara. No centro, um **dente dourado** com o perfil de um rosto e as letras **C** e **B** douradas em degradê, ligadas por um traço fino.
- Arquivo: `assets/logo.jpeg` (414×414). O fundo é exatamente `#4b5a43`.
- Uso: sempre redondo, sempre sobre fundo verde ou claro. Nunca esticar, recolorir, girar ou aplicar efeito.
- Presente no site (cabeçalho, capa, rodapé) e no slide final dos carrosséis (cartão de contato).

### 3.2 Paleta

| Nome | Hex | Onde usar |
|------|-----|-----------|
| Verde-oliva (cor do logo) | `#4b5a43` | Fundo de capa e de CTA; botões; título nas respostas |
| Verde-profundo | `#3a4733` | Fundo da parte superior dos slides de conteúdo |
| Verde-noite | `#2b3527` | Rodapé do site |
| Dourado claro | `#ecd382` | Realces, contornos, ícones sobre verde |
| Dourado | `#c9971f` | Bordas (avatar, arco), detalhes |
| Dourado escuro | `#8f6410` | Realces sobre fundo claro |
| Degradê dourado | `linear-gradient(135deg, #f0dc8c 0%, #c9971f 52%, #8f6410 100%)` | Etiquetas e botões principais |
| Papel | `#f3f5ef` | Fundo claro e painéis |
| Papel 2 | `#e6ebde` | Caixas de destaque ("o que fazer") |
| Tinta | `#232d1f` | Texto sobre fundo claro |
| Tinta suave | `#4d5946` | Texto secundário |
| Vermelho do mito | `#b4493b` | **Só** para "Mito" e "Procure atendimento" |
| Risco do mito | `#e8806f` | Linha que risca a frase do mito |

Regra: o fundo é verde ou "papel"; **dourado é acento, nunca fundo grande**; vermelho aparece só nos dois usos acima.

### 3.3 Tipografia

| Onde | Títulos | Texto |
|------|---------|-------|
| **Carrosséis** | **Lora** (serifada, bold) | **Poppins** (400, 500, 600, 700) |
| **Site** | Fraunces (serifada de aparência suave) | Figtree |

As duas duplas são serifada calorosa + sem serifa amigável. Os carrosséis usam Lora/Poppins por terem sido produzidos assim. O Hermes deve **manter** essas fontes nos carrosséis. Se rodar sem internet, Lora e Poppins precisam estar instaladas no computador (são fontes gratuitas do Google Fonts).

### 3.4 Formas e elementos de assinatura
- **Etiquetas em pílula** (cantos totalmente arredondados) para tipo de slide ("Sinal", "Dica", "Mito", "Na verdade").
- **Painel claro com topo arredondado (64 px)** subindo sobre o fundo verde nos slides de conteúdo.
- **Caixa "o que fazer"** (papel 2, cantos de 28 px) com ícone de check verde.
- **Anel dourado tracejado** atrás do Dr. Tiago, ecoando o círculo do logo, mais um brilho verde-claro (degradê radial).
- **Avatar redondo com borda dourada** + "Dr. Tiago Binhame / Clínica Binhame" no rodapé dos slides de conteúdo (marca pessoal em todo slide).
- **Arco** (topo semicircular) para a foto do Dr. Tiago no site.
- **Ícones** simples de traço (alerta, pergunta, lâmpada, check, X, comentário, enviar, salvar).
- Sem sombras pesadas, sem degradês decorativos além do dourado e do brilho atrás da foto, sem ilustrações de dentes/procedimentos.

### 3.5 Foto do Dr. Tiago
- Arquivos: `assets/tiago_cut.webp` e `assets/tiago_cut.png` (recorte com fundo transparente, 1226×1676).
- Origem: print de postagem do Instagram, por isso a resolução é limitada e a borda do recorte é automática. Em tela grande o rosto fica levemente "macio".
- Regras de uso: sempre ancorada no canto inferior direito; rosto livre de texto; orelha direita não pode ser cortada pela borda; o corte de baixo e da direita fica fora do quadro de propósito.
- **Melhoria planejada:** substituir por foto original (pergunta D7 do prompt).

### 3.6 O que evitar
Fundo creme com serifa e laranja-terracota genéricos; fundo preto com cor neon; muitos cartões idênticos com sombra; excesso de legendas em caixa-alta; setas "→" no fim de botões; animações em tudo; cores que não estejam na paleta; imagens de dentes geradas por IA; qualquer visual "hospitalar frio".

---

## 4. Tom de voz, regras de texto e engajamento

### 4.1 Tom
**Profissional, mas acessível e descontraído.** Fala como um dentista de confiança que explica sem pressa: claro, calmo, sem medo e sem pressão. Humor leve é bem-vindo, mas **nunca** à custa de dor, medo ou do paciente.

### 4.2 Regras de escrita
- Português do Brasil, tratamento por **"você"**.
- Frases curtas. Voz ativa. Primeira letra maiúscula só no início da frase (não usar Caixa Alta em títulos).
- Palavras simples. Se um termo técnico for necessário (gengivite, bruxismo, tártaro), explicar na mesma frase.
- **Botões e chamadas dizem exatamente o que acontece:** "Agende sua avaliação", "Chame no WhatsApp". Nada de "Clique aqui" ou "Saiba mais".
- Usar "pode", "costuma", "em geral", "depende da avaliação" para temas clínicos.
- Não usar: "o melhor", "garantido", "perfeito", "milagre", preços, promoções, "grátis", "gratuito".
- Emoji: só na legenda, 2 a 4 no máximo.

### 4.3 Limites de tamanho dos textos (para caber no slide)

| Campo | Limite de referência |
|-------|----------------------|
| Capa: etiqueta | até 28 caracteres |
| Capa: título | 3 a 4 linhas de até 17 caracteres cada |
| Capa: subtítulo | até 60 caracteres |
| Conteúdo: título (frase em cima) | até 60 caracteres (3 linhas) |
| Conteúdo: frase de resposta (em destaque) | até 55 caracteres (2 linhas) |
| Conteúdo: texto de apoio | 120 a 190 caracteres (4 a 5 linhas) |
| Conteúdo: "o que fazer" | até 80 caracteres |
| Mito: frase do mito | até 55 caracteres |
| Lista: título | até 45 caracteres; 4 a 5 itens; item até 34 caracteres + detalhe até 42 |
| CTA: título | até 40 caracteres |
| CTA: ações | 3 itens, até 55 caracteres cada |
| CTA: nota (opcional) | até 95 caracteres |

O gerador reduz a fonte sozinho até certo ponto e **avisa** se ainda assim não couber. Nesse caso, encurte o texto.

### 4.4 Mecânicas de engajamento usadas
1. **Capa com gancho:** pergunta ("Em quantos você acredita?", "Sua boca está pedindo ajuda?") ou número ("5 hábitos...").
2. **Convite para arrastar** na capa.
3. **Um conteúdo por slide**, com a resposta curta em destaque (quem só passa o dedo já aprende algo).
4. **Slide "salvável":** rotina, checklist ou lista no meio/fim (aumenta salvamentos).
5. **Último slide com 3 ações:** comentar (pergunta específica), enviar (a quem, de forma concreta: "para quem vive tomando café") e agendar.
6. **Marca pessoal em todo slide:** avatar + nome do Dr. Tiago.
7. **Série conectada:** cada carrossel remete ao anterior e prepara o próximo (hábitos → sinais → medo → mitos → siso → dente faltando → urgência).

### 4.5 Modelo de legenda
```
[Gancho em 1 linha, com 1 emoji]
[1 a 2 linhas dizendo o que a pessoa vai aprender ao arrastar]
[Pergunta para comentar, específica] 👇
[Convite concreto para salvar e/ou enviar]
Agende sua avaliação pelo WhatsApp: (11) 94046-3921
📍 Av. Eduardo Prado, 575, Santo André
[6 a 8 hashtags: 2 de tema, 2 de profissão, 2 de local (#dentistasantoandre #santoandre), 1 a 2 de público]
```
Exemplos completos: `legendas-carrosseis.md`.

---

## 5. Anatomia do carrossel

**Formato:** imagens PNG de **1080×1350 pixels** (proporção 4:5, o formato vertical do Instagram). Cada carrossel tem de **5 a 9 slides**, padrão **7**. Margem interna de 80 px.

### 5.1 Tipos de slide

**`cover` (capa)**
```
┌──────────────────────────┐
│ (Etiqueta redonda)       │
│ TÍTULO EM 3-4 LINHAS     │
│ ...                      │
│ subtítulo     ◜ Dr.Tiago │
│ curto           (foto)   │
│ Arraste para o lado  →   │
└──────────────────────────┘
fundo verde-oliva, anel dourado tracejado atrás da foto
```

**`content` (sinal, hábito, dica, pergunta, "o que acontece", "procure atendimento")**
```
┌──────────────────────────┐ fundo verde-profundo
│ [etiqueta]  2 de 5       │
│ Título em destaque       │
│ (até 3 linhas)           │
│ ╭──────────────────────╮ │ painel "papel", topo arredondado
│ │ Frase de resposta    │ │
│ │ Texto de apoio       │ │
│ │ [✓ O que fazer     ] │ │
│ │ (avatar) Dr. Tiago 3/7│ │
└──────────────────────────┘
```
Cor da etiqueta: `gold` (padrão) ou `red` (urgência).
Ícones da etiqueta: `alert`, `question`, `bulb`, `check`.

**`myth` (mito e verdade)**
```
┌──────────────────────────┐
│ [✕ Mito]  1 de 5         │
│ ~~Frase do mito riscada~~│ (vermelho do risco)
│ ╭──────────────────────╮ │
│ │ [✓ Na verdade]       │ │
│ │ Frase correta        │ │
│ │ Explicação           │ │
└──────────────────────────┘
```

**`list` (rotina, checklist, passo a passo)**
Título curto + 4 a 5 itens com ícone de check, cada um com detalhe menor embaixo. Feito para ser **salvo**.

**`cta` (chamada final)**
Título-pergunta, 3 ações com ícone (comentar, enviar, salvar), foto do Dr. Tiago à direita e cartão claro embaixo com logo, WhatsApp e endereço. Campo opcional `note` para aviso (ex.: emergência).

### 5.2 Estrutura recomendada de um carrossel
`cover` → 5 slides de conteúdo (`content` ou `myth`) → (opcional) 1 `list` → `cta`.

### 5.3 O arquivo de conteúdo
O conteúdo de cada carrossel é um arquivo de texto `.json` com este formato (exemplos reais em `specs/`; um completo no Apêndice A):

```
{
  "slug": "nome-curto-sem-acentos",
  "tema": "descrição do tema",
  "objetivo": "alcance | salvamentos | agendamento ...",
  "slides": [
    {"type":"cover",  "tag":"...", "title":["linha 1","linha 2","linha 3"], "sub":"..."},
    {"type":"content","badge":"Sinal","icon":"alert","color":"gold",
                      "title":"...","headline":"...","text":"...","action":"..."},
    {"type":"myth",   "claim":"...","headline":"...","text":"..."},
    {"type":"list",   "badge":"Salve este slide","title":"...",
                      "items":[{"title":"...","detail":"..."}]},
    {"type":"cta",    "title":"...",
                      "actions":[{"icon":"comment","text":"..."},{"icon":"send","text":"..."},{"icon":"save","text":"..."}],
                      "card_title":"Agende sua avaliação",  "note":"opcional"}
  ]
}
```
Ícones de ação do `cta`: `comment`, `send`, `save`.

### 5.4 Como gerar as imagens
Dentro de `engine/`:
```
python build_carousel.py ../specs/urgencia.json --out ../saida/urgencia
```
Resultado: `slide-01.png`, `slide-02.png`... Requer Python 3, a biblioteca Playwright e o navegador Chromium (`pip install playwright` e `playwright install chromium`). Os dados da clínica (nome, WhatsApp, endereço) ficam em `engine/clinic.json`.

---

## 6. Carrosséis já produzidos e banco de temas

### 6.1 Os 7 carrosséis (todos em `exemplos/` e `specs/`)

| # | Tema | Formato | Slides | Objetivo |
|---|------|---------|--------|----------|
| 1 | **Mitos do clareamento**: estraga o esmalte, pasta de carvão, limão e bicarbonato, efeito eterno, qualquer pessoa pode | `myth` | 7 | Comentários e compartilhamentos; reforçar clareamento |
| 2 | **Sinais de que a higiene bucal precisa de atenção**: gengiva que sangra, mau hálito, sensibilidade, tártaro, mais de 1 ano sem consulta + rotina | `content` + `list` | 8 | Salvamentos (rotina) e agendamento |
| 3 | **5 hábitos que estragam os dentes**: beliscar doce, bebida ácida, ranger, roer unha, dormir sem escovar | `content` | 7 | Alcance novo |
| 4 | **Medo de dentista**: 5 dicas | `content` | 7 | Acolhimento |
| 5 | **Siso**: 5 perguntas e respostas | `content` | 7 | Captar quem tem dúvida de cirurgia |
| 6 | **Urgência**: dor forte, inchaço, dente quebrado, dente que caiu, sangramento | `content` (vermelho) | 7 | Salvamentos e confiança |
| 7 | **Dente faltando**: o que acontece com o tempo e o que fazer | `content` + `list` | 8 | Tratamentos de maior valor (a confirmar serviço) |

Ordem sugerida de postagem: 3 → 2 → 4 → 1 → 5 → 7 → 6 (um por semana).

### 6.2 Pilares de conteúdo (para o Hermes balancear os temas)

| Pilar | Peso sugerido | Exemplos |
|-------|---------------|----------|
| **Prevenção e rotina** | 40% | Escovação: erros comuns; fio dental: dúvidas; quando trocar a escova; o que é flúor; boca seca; alimentos amigos e inimigos dos dentes |
| **Acolhimento** | 15% | Primeira consulta: o que esperar; perguntas que você tem vergonha de fazer; como se preparar para a consulta |
| **Serviços da clínica** | 25% | Clareamento: cuidados durante e depois; siso: pós-operatório; cirurgias orais; reposição de dentes *(a confirmar)*; estética *(a confirmar)* |
| **Urgência e segurança** | 10% | O que fazer até chegar ao dentista; dente de leite que cai; trauma |
| **Institucional** | 10% | Conheça o Dr. Tiago (só com informações dele); como a clínica cuida do seu conforto (só com informações dele) |

Cada novo tema deve ser **relacionado** à série (pode citar ou preparar outro carrossel) mas **não repetir** um tema já feito: o Hermes consulta `HISTORICO.md` antes de propor.

---

## 7. Como foi construído (e o que aprendemos errando)

### 7.1 Passo a passo técnico (em português simples)

1. **Referências.** Pesquisa de clínicas de São Paulo. Resultado: diretórios e anúncios; padrão de ambiente moderno, tecnologia e conforto.
2. **Cores do logo.** Foram medidas as cores do próprio arquivo: o fundo é `#4b5a43` e o dourado vai de um amarelo claro a um âmbar escuro, que virou o degradê da marca.
3. **Landing page.** Escrita como **um único arquivo HTML** (logo e foto embutidos), com fontes do Google Fonts, uma animação de entrada na capa, anel girando devagar, respeito a quem prefere menos movimento, botão fixo de WhatsApp, mapa e dados para o Google entender que é um consultório odontológico. Para publicar: renomear para `index.html` e subir em qualquer hospedagem.
4. **Foto do Dr. Tiago.** A partir do print do Instagram: recorte do fundo por processamento de imagem, limpeza de sobras (letras do post, sombra), ampliação 2×, leve ajuste de nitidez e brilho, borda suavizada, margem transparente no topo e corte de baixo para remover marcas do Instagram. Salva em WebP (64 KB).
5. **Carrosséis.** Cada slide é uma página web de 1080×1350 desenhada com HTML e CSS; um navegador sem tela (Chromium via Playwright) tira a "foto" de cada slide e salva em PNG.
6. **Ajuste automático de texto.** Um pequeno programa mede se o texto cabe e reduz a fonte quando necessário; se ainda não couber, avisa.
7. **Conferência visual.** Todo carrossel foi visto em miniatura (folha de contato) e em tamanho real antes de entregar.
8. **Empacotamento.** Os textos viraram arquivos `.json` e o gerador reproduz os 7 carrosséis idênticos aos entregues.

### 7.2 Lições aprendidas (o Hermes deve evitar repetir)

| Problema | O que aconteceu | Solução adotada |
|----------|-----------------|-----------------|
| **Mito x verdade confuso** | A frase do mito aparecia grande e bonita, com a etiqueta "Verdade" logo abaixo; dava para ler o contrário | Mito **riscado**, etiqueta vermelha "✕ Mito"; resposta em painel separado com "✓ Na verdade" e a frase correta em destaque |
| **Número gigante colidindo com o título** | Numeral decorativo atrás do título | Removido; contagem "1 de 5" na etiqueta |
| **Texto estourando o slide** | Textos longos cobriam o rodapé | Ajuste automático de fonte + aviso do gerador + limites de tamanho |
| **Contador errado** | "1 de 6" num carrossel com 5 conteúdos | Contador calculado automaticamente |
| **Foto cortando a orelha** | Foto grande demais na capa | Largura 740 px com margem controlada |
| **Entalhe no braço da foto** | Remoção dos pontinhos do Instagram apagou um bloco | Em vez de apagar um bloco, a imagem foi cortada rente |
| **Avatar mostrando só o queixo** | Posição errada no recorte | Ampliação e posição calibradas (160%, 100% 32%) |
| **Sugerir "avaliação gratuita" no topo** | Foi sugerido como argumento forte | Pesquisa mostrou que serviço gratuito é vedado pela publicidade odontológica; **não usar** |

### 7.3 O que o gerador faz e não faz
Faz: monta os slides a partir do arquivo de conteúdo, aplica identidade, ajusta texto, gera PNG, avisa de problemas.
Não faz: escrever o conteúdo (isso é papel do Hermes), publicar, gerar legenda, validar fatos.

---

## 8. Regras de conteúdo e conformidade

> Resumo de pesquisa feita durante o projeto. **Não é parecer jurídico.** O Dr. Tiago deve confirmar tudo com o CRO-SP.

**Base normativa consultada:** Código de Ética Odontológica (Resolução CFO-118/2012) e Resolução CFO-196/2019, que flexibilizou a divulgação de autorretratos e de imagens de diagnóstico e resultado final de tratamento.

**O que a pesquisa indicou:**
- Continuam **proibidos**: sensacionalismo, autopromoção, concorrência desleal, mercantilização da odontologia e **promessa de resultado**.
- Segundo material de estudo consultado, continuam vedados a divulgação de **preços, formas de pagamento e serviços gratuitos** (por isso "avaliação gratuita" é um risco; o post de Instagram da clínica que usa essa expressão deve ser revisado).
- Imagens de pacientes e "antes e depois" dependem de **autorização prévia e expressa do paciente** e de condições específicas (caso do próprio profissional, termo de consentimento).
- A resolução também restringe imagens que permitam identificar equipamentos, materiais e tecidos biológicos (conferir o texto oficial).
- Tudo que envolve dados pessoais e de saúde também cai na **LGPD** (Lei 13.709/2018).

**Fontes para conferir:** texto da Resolução CFO-196/2019 em `website.cfo.org.br` e `sistemas.cfo.org.br`; Código de Ética (Capítulo sobre anúncio, publicidade e propaganda); CRO-SP.

**Regras operacionais derivadas (as mesmas do prompt):** sem preço, sem "grátis", sem promessa, sem diagnóstico, sem receita, sem paciente identificável, sem afirmar serviço não confirmado, CRO visível, tudo como rascunho até o Dr. Tiago aprovar.

---

## 9. Roadmap das fases

| Fase | O que entrega | Como o usuário usa | Depende de |
|------|---------------|--------------------|------------|
| **1. Fábrica de carrosséis** | Tema → carrossel pronto (imagens + legenda + lista de conferência) | Conversando com o Hermes | Gerador (pronto), regras (este documento), decisões D1 a D8 |
| **2A. Bot da equipe** | O mesmo pelo Telegram (ou WhatsApp), com perguntas curtas de refinamento | Conversando com o bot | Fase 1 estável; decisão D9 a D12 |
| **2B. Bot de pacientes** | Responde dúvidas só com conteúdo aprovado e encaminha para a equipe | Pacientes no Telegram/WhatsApp | Base de perguntas e respostas aprovada; LGPD; decisões D11 a D13 |
| **3. Rotina e medição** | Sugestão semanal de temas, agendamento, métricas | Opcional | Fases anteriores; decisão D14 |

**Ciclo que conecta tudo:** pergunta de paciente → vira tema → vira carrossel aprovado → vira resposta do bot.

---

## 10. O PROMPT PARA O HERMES AGENT

**Copie tudo o que está dentro do bloco abaixo** (do "Você é o Hermes" até "Comece agora...") e cole na conversa com o Hermes, depois de anexar o pacote.

````markdown
Você é o Hermes. Vou pedir que você construa, comigo, um agente chamado provisoriamente **"Fábrica de Carrosséis Binhame"**.

O que ele faz: eu digito um **tema** (por exemplo, "escovação: 5 erros comuns") e ele devolve um **carrossel de Instagram pronto para postar**, no padrão visual e de linguagem da Clínica de Odontologia Binhame (Dr. Tiago Binhame, Santo André, SP), junto com a legenda e uma lista curta do que o dentista precisa conferir antes de publicar.

Tudo o que você precisa saber sobre a clínica, a identidade visual, o jeito de escrever, o que já foi produzido e as regras de conteúdo está **neste documento, antes deste prompt**, e nos arquivos da pasta anexa (assets, engine, specs, exemplos). Leia tudo antes de responder qualquer coisa.

---

## 1. COMO CONVERSAR COMIGO (é a regra mais importante)

Eu **não sou desenvolvedor**. Sou gestor e entendo bem de processo, de negócio e de IA no nível de uso, mas não conheço termos técnicos de programação, servidores ou redes. Por isso:

1. **Fale em português simples.** Sem jargão. Se um termo técnico for inevitável, explique em uma frase, com exemplo do dia a dia. Use o glossário do documento (Apêndice D) como guia: diga "conexão com outro serviço" em vez de "API", "colocar no ar" em vez de "deploy", "servidor na internet" em vez de "nuvem/VPS", e assim por diante.
2. **Uma decisão por vez.** Faça no máximo uma pergunta principal por mensagem (até três se forem claramente do mesmo assunto). Nunca me jogue uma lista de dez perguntas.
3. **Toda pergunta de decisão segue este formato:**
   - **Situação:** em uma ou duas frases, por que isso precisa ser decidido agora.
   - **Opções:** 2 a 3 opções, cada uma com o que muda **na prática** para mim (custo, tempo, esforço, risco, privacidade). Nada de comparação técnica.
   - **Minha recomendação:** qual você escolheria no meu lugar e por quê, em uma frase.
   - **Resposta fácil:** termine com algo como "Pode responder só A, B ou C. Se não tiver certeza, diga 'você escolhe' e eu sigo a recomendação."
4. **Seja direto e honesto.** Se uma ideia minha tiver problema (de custo, de risco, de qualidade ou de regra do conselho de odontologia), diga com clareza e proponha uma alternativa. Não precisa me agradar. Prefiro ser desafiado a ser validado.
5. **Peça confirmação antes de qualquer coisa que:** gaste dinheiro, instale programas no meu computador, conecte uma conta minha (Instagram, Google, Telegram, WhatsApp), apague arquivos ou **publique algo em qualquer lugar**. Nunca publique nada sozinho nesta fase.
6. **Decisões pequenas e reversíveis** (nome de pasta, ordem de arquivos, pequenos ajustes de layout dentro das regras): decida você e apenas me avise em uma linha. Não me pergunte coisas que eu não teria como opinar.
7. **Quando algo der errado**, explique em linguagem simples o que aconteceu e qual é o plano. Não me mostre mensagens de erro cruas, a menos que eu peça. Se precisar de algo de mim (um arquivo, uma senha, um clique), diga exatamente o que e onde.
8. **Termine cada etapa dizendo qual é o próximo passo** e o que você precisa de mim, se for o caso.
9. **Registre cada decisão** que eu tomar no arquivo `DECISOES.md` (data, pergunta, minha resposta, o que isso muda). Se eu mudar de ideia depois, atualize. No início de cada nova sessão, leia esse arquivo.
10. Se o que eu disse na conversa contradisser este documento, **vale o que eu disse na conversa** (mas me avise da contradição se ela afetar regra de conteúdo ou de conformidade).

---

## 2. O QUE VOCÊ VAI CONSTRUIR: AS FASES

**Fase 1 (agora): Fábrica de carrosséis.** Eu digito um tema, você devolve o carrossel pronto da forma **mais simples possível**.

**Fase 2 (depois): conversa por Telegram ou WhatsApp.** O mesmo agente passa a conversar por mensagem, fazendo perguntas e respostas. Há duas possibilidades de uso (veja a decisão D9) e talvez as duas: (a) **eu e o Dr. Tiago** pedimos carrosséis conversando com o bot, e o bot me faz perguntas para refinar o tema; (b) **pacientes** tiram dúvidas com o bot sobre saúde bucal e a clínica, com respostas baseadas só em conteúdo aprovado.

**Fase 3 (futuro, só se eu pedir):** sugerir temas toda semana, agendar e publicar, medir resultados.

Nesta conversa você **constrói a Fase 1** e deixa a base preparada para a Fase 2 (por exemplo, guardando conteúdo aprovado em um formato que o bot possa reutilizar). Não construa a Fase 2 sem eu pedir.

---

## 3. FASE 1: O FLUXO QUE O AGENTE DEVE TER

**Entrada mínima:** só o tema, em linguagem natural. Opcionais que eu posso informar: objetivo (alcance, salvamento, agendamento), número de slides, formato preferido, algo que eu queira evitar.

**Passo 1. Entender o tema.** Se o tema estiver claro, siga em frente sem perguntar nada. Só pergunte se faltar algo essencial (por exemplo, o tema depende de um serviço que a clínica talvez não ofereça). Nesse caso, pergunte em linguagem simples, no formato da seção 1.

**Passo 2. Escolher o formato.** Entre os tipos de slide disponíveis (veja a seção 5 do documento):
- **Sinais / hábitos / dicas / perguntas e respostas** → slides do tipo `content` (título em cima, resposta embaixo, caixa "o que fazer");
- **Mitos e verdades** → slides do tipo `myth` (mito riscado + "Na verdade");
- **Rotina, passo a passo, checklist** → slide do tipo `list` (pensado para ser salvo);
- Sempre: 1 capa (`cover`) no início e 1 slide final de chamada para ação (`cta`).
Padrão: **7 slides** (capa + 5 de conteúdo + chamada final), podendo chegar a 8 com um slide de lista. Entre 5 e 9 slides no total.

**Passo 3. Verificar o conteúdo.** Se tiver acesso à internet, consulte fontes confiáveis de odontologia (conselhos e associações de odontologia, Ministério da Saúde, organizações internacionais reconhecidas, material de faculdades públicas). **Não invente dado clínico, número, porcentagem ou estudo.** Se não tiver certeza de uma afirmação, escreva de forma mais geral ("pode", "costuma") ou deixe de fora. Registre as fontes em `revisao.md`.

**Passo 4. Escrever os textos** seguindo o tom de voz e os limites de tamanho da seção 4 do documento. Reaproveite o estilo dos 7 exemplos em `specs/`.

**Passo 5. Montar as imagens** preenchendo um arquivo de conteúdo no mesmo formato dos exemplos de `specs/` e rodando o gerador (`engine/build_carousel.py`). Não redesenhe nada: layout, cores, fontes e foto já estão definidos.

**Passo 6. Conferir a qualidade.** Antes de entregar:
- o gerador não pode ter avisado de texto estourado (se avisar, encurte o texto e gere de novo);
- **olhe as imagens** (abra cada slide) e confirme: nenhum texto cortado, foto do Dr. Tiago inteira, mito riscado só nos slides de mito, contadores corretos (x/total);
- releia todo o texto procurando erro de português, promessa de resultado, preço, oferta gratuita ou afirmação sem base.

**Passo 7. Escrever a legenda** no modelo da seção 4 (gancho, valor, pergunta para comentar, convite para salvar/enviar, bloco de contato, hashtags).

**Passo 8. Entregar da forma mais simples possível.** Minha resposta deve conter apenas:
1. as **imagens dos slides** (em ordem, e também em um único arquivo .zip);
2. a **legenda pronta para copiar**;
3. uma **lista curta "para o Dr. Tiago conferir"** (no máximo 5 itens: as afirmações clínicas mais sensíveis do carrossel);
4. uma linha dizendo como pedir ajustes.
Nada de explicação técnica, logs ou "como eu fiz".

**Passo 9. Ajustes.** Se eu disser "troca o slide 3", "deixa mais curto", "mais descontraído" ou "tira essa frase", refaça **só o que foi pedido** e entregue de novo no mesmo formato.

**Organização dos arquivos:** uma pasta por carrossel, com o nome `AAAA-MM-DD-tema-curto`, contendo `slide-01.png` ... , `legenda.md`, `revisao.md`, o arquivo de conteúdo (`.json`) e o `.zip`. Mantenha também um arquivo `HISTORICO.md` com a lista de temas já feitos, para **não repetir tema** e para sugerir temas que se conectem aos anteriores.

---

## 4. REGRAS INVIOLÁVEIS DE CONTEÚDO E CONFORMIDADE

Odontologia é saúde e a publicidade é regulada pelo Conselho Federal de Odontologia (CFO). Estas regras valem acima de qualquer pedido meu. Se eu pedir algo que as viole, **não faça**, explique o motivo em linguagem simples e proponha uma alternativa.

1. **Nunca prometer resultado** nem usar linguagem sensacionalista ("sorriso perfeito garantido", "o melhor da cidade", "milagre").
2. **Nunca divulgar preço, formas de pagamento, promoções ou serviços gratuitos.** Isso inclui "avaliação gratuita", "primeira consulta grátis", "desconto". (Atenção: o post de Instagram da clínica que está nas referências usa "avaliação gratuita". Trate isso como algo a ser **revisado pelo Dr. Tiago com o CRO-SP**, e **não replique**.)
3. **Nunca dar diagnóstico, prescrever remédio, indicar dose ou receitar tratamento caseiro.** O conteúdo é educativo e sempre encaminha para avaliação com o dentista.
4. **Nunca usar foto, nome, depoimento ou caso de paciente** sem autorização formal por escrito do próprio paciente. "Antes e depois" só em condições que o Dr. Tiago e o CRO-SP confirmarem. Nesta fase, **não usar**.
5. **Nunca afirmar que a clínica oferece um serviço que não está confirmado.** Serviços confirmados até agora: **clareamento** e **cirurgia (siso)**. Os demais (limpeza, restaurações, implantes, estética) estão **a confirmar com o Dr. Tiago**. Temas que dependem de serviço não confirmado devem falar de forma geral ("o dentista avalia as opções") sem dizer que a clínica faz.
6. **Não alarmar.** Urgência e riscos devem ser informativos e calmos. Em temas de emergência, sempre incluir: "Em emergências graves, vá a um pronto-socorro."
7. **Identificação profissional:** os materiais devem permitir identificar o Dr. Tiago Binhame, cirurgião-dentista. O **número do CRO-SP ainda não foi informado**; pergunte e coloque onde o documento indicar quando eu fornecer.
8. **Dados pessoais (LGPD).** Não coletar, guardar ou repetir dados de saúde ou pessoais de ninguém sem necessidade e sem aviso. Isso vale muito para a Fase 2.
9. **Linguagem de dúvida honesta:** use "pode", "costuma", "em geral", "depende da avaliação" quando a evidência for variável. Nunca "sempre" ou "nunca" em tema clínico, salvo quando for consenso inequívoco.
10. Todo carrossel sai marcado como **"RASCUNHO: aguardando revisão do Dr. Tiago"**. Eu (ou ele) aprovo. Você **não publica**.

> Observação: estas regras foram resumidas de pesquisas feitas durante o projeto e **não substituem orientação jurídica ou do CRO-SP**. Quando tiver dúvida real, recomende que o Dr. Tiago confirme com o CRO-SP.

---

## 5. REGRAS INVIOLÁVEIS DE DESIGN

1. Use sempre o gerador `engine/build_carousel.py`, os arquivos de `assets/` (logo e foto do Dr. Tiago) e as cores e fontes definidas no documento (seção 3). **Não troque paleta, fonte, formato (1080×1350) nem estilo.**
2. Não use IA para gerar imagens de pessoas, dentes ou procedimentos. O visual é feito de tipografia, formas, ícones simples e a foto real do Dr. Tiago.
3. Não coloque texto sobre o rosto do Dr. Tiago. Não distorça nem recolora o logo.
4. Respeite os limites de tamanho de texto. Se o gerador avisar que o texto está longo, **encurte o texto**, não diminua a fonte além do que o gerador faz sozinho.
5. Mito riscado e ícone "✕ Mito" só em slides de mito; ícone "✓ Na verdade" só para a resposta correta. **Nunca coloque a afirmação errada em destaque sem estar claramente marcada como mito** (já tivemos esse erro e foi corrigido).
6. Português do Brasil, você, frases curtas, sem gíria pesada, emoji só na legenda e com moderação.

---

## 6. COMO COMEÇAR (faça nesta ordem)

1. **Leia** o documento inteiro e a pasta anexa. Abra pelo menos 2 exemplos de `exemplos/` para ver o resultado final.
2. **Teste o gerador** com `specs/urgencia.json` e confirme que as imagens saem iguais às de `exemplos/urgencia/`. Se não conseguir rodar (falta algum programa, por exemplo), me diga em linguagem simples o que falta e peça autorização para instalar.
3. **Apresente-se** em no máximo 8 linhas: o que você entendeu do projeto, o que vai fazer primeiro e o que ainda não sabe.
4. **Faça as perguntas de decisão**, uma por vez, na ordem da seção 7, **começando por D1**. Só avance quando eu responder.
5. Com D1 a D6 respondidas, **gere um carrossel de teste** com um tema que eu escolher (ou, se eu não escolher, "Escovação: 5 erros comuns") e entregue no formato do Passo 8.
6. Peça meu feedback ("o que mudaria?"), ajuste e só então diga que a Fase 1 está pronta.

---

## 7. PONTOS DE DECISÃO (você deve me perguntar)

Pergunte no formato da seção 1. As recomendações abaixo são o que eu espero que você sugira, mas explique com suas palavras e exemplos concretos.

**Perguntar agora, antes de construir:**

- **D1. Onde o agente vai "morar".** Opções típicas: (A) no meu próprio computador (sem custo extra, mas só funciona com ele ligado e com o programa aberto); (B) em um servidor na internet (funciona sempre, tem custo mensal e exige conta). *Recomendação: A para testar; migrar para B só quando for usar com a equipe ou no Telegram/WhatsApp.*
- **D2. Que "cérebro" (modelo de IA) usar.** Explique o equilíbrio entre qualidade do texto, custo, velocidade e privacidade (um modelo rodando no meu computador não manda nada para fora, mas costuma escrever pior que um serviço pago). *Recomendação: o melhor texto possível para a escrita dos carrosséis, já que o conteúdo é de saúde; pode ser outro mais simples para tarefas mecânicas.*
- **D3. Como vou pedir o carrossel agora.** (A) Conversando aqui com você; (B) preenchendo um formulário simples; (C) já direto pelo Telegram. *Recomendação: A agora, C na Fase 2.*
- **D4. Quem aprova antes de postar.** Só eu, ou o Dr. Tiago também? Como o carrossel chega até ele (arquivo, mensagem)? *Recomendação: o Dr. Tiago sempre revisa o conteúdo clínico; eu reviso o visual e a legenda.*
- **D5. Pesquisa na internet.** Posso liberar você para pesquisar fontes ao escrever os carrosséis? *Recomendação: sim, restrito a fontes confiáveis de odontologia e saúde, sempre registrando de onde veio.*
- **D6. Onde salvar os carrosséis.** Uma pasta no computador, Google Drive, outro? *Recomendação: uma pasta única, organizada por data e tema.*

**Perguntar quando chegar o momento (antes de finalizar a Fase 1):**

- **D7. Pendências da clínica** (veja o Apêndice C): número do CRO-SP, @ do Instagram, horários, serviços confirmados, foto original do Dr. Tiago. Pergunte uma por vez e me ajude a decidir quando não tiver a resposta (por exemplo, "enquanto isso, o carrossel sai sem horário e sem @").
- **D8. Fonte dos carrosséis vs. site.** Hoje o site usa uma dupla de fontes e os carrosséis usam outra. *Recomendação: manter como está; unificar só se for barato e eu pedir.*

**Perguntar ao iniciar a Fase 2 (não antes):**

- **D9. Para quem é o bot.** (A) Só para a equipe pedir carrosséis; (B) só para pacientes tirarem dúvidas; (C) os dois, em canais separados. *Recomendação: começar por A, que é seguro, e só depois B.*
- **D10. Telegram ou WhatsApp.** Explique: Telegram é gratuito e rápido de montar; WhatsApp é onde os pacientes realmente estão, mas o jeito oficial exige uma conta comercial verificada e pode ter custo por conversa, e os atalhos não oficiais correm o risco de o número ser bloqueado. *Recomendação: Telegram primeiro; WhatsApp oficial quando B for aprovado.* Confira as regras e preços atuais antes de me apresentar números.
- **D11. O que o bot de pacientes pode fazer sozinho.** Escada de autonomia: nível 0 = só responde dúvidas com conteúdo aprovado; nível 1 = também recebe pedido de contato (nome, telefone, melhor horário) e repassa para a equipe; nível 2 = agenda sozinho (futuro). *Recomendação: nível 0, depois 1.*
- **D12. Quem recebe quando o bot não sabe ou é urgente.** Qual número ou pessoa, em que horário, e qual mensagem automática fora do horário.
- **D13. Aviso de privacidade (LGPD).** Qual texto o bot mostra na primeira mensagem e o que ele nunca guarda.
- **D14. Publicar sozinho?** *Recomendação: não. Manter a entrega para revisão humana.*

Se eu responder algo que abra uma dúvida nova importante, pergunte. Se eu disser "você escolhe", siga a recomendação e anote em `DECISOES.md`.

---

## 8. FASE 2: GUIA PARA QUANDO CHEGAR A HORA

**Bot da equipe (A):** o bot conversa comigo e com o Dr. Tiago para pedir carrosséis. Ele deve: perguntar no máximo 2 coisas curtas para refinar o tema (público e objetivo), devolver o carrossel no formato do Passo 8, aceitar ajustes por mensagem ("troca o slide 3") e sugerir 3 temas conectados aos já feitos (`HISTORICO.md`).

**Bot de pacientes (B), se aprovado:**
- Responde **só** com base em conteúdo aprovado: os carrosséis revisados, uma lista de perguntas e respostas frequentes escrita junto com o Dr. Tiago e os dados da clínica. **Se a resposta não estiver na base, diz que não sabe e encaminha** (D12).
- Tom: acolhedor, direto, descontraído sem exageros, em mensagens curtas.
- **Nunca** dá diagnóstico, receita, dose, preço, promoção ou promessa de resultado.
- **Sinais de urgência** (inchaço no rosto, febre, dificuldade para engolir ou respirar, sangramento que não para, dente que saiu por trauma, dor muito forte): responde com a orientação de urgência dos carrosséis aprovados, indica pronto-socorro quando grave e avisa a equipe.
- Pede o mínimo de dados pessoais, só quando a pessoa quer que a clínica entre em contato, e só depois do aviso de privacidade (D13).
- **Aprende com as perguntas:** registra, sem dados pessoais, as dúvidas que não conseguiu responder e as mais frequentes, e usa isso para **sugerir novos temas de carrossel**. Esse ciclo (pergunta de paciente → tema → carrossel aprovado → resposta do bot) é o coração do projeto.
- Mensagem inicial sugerida: apresenta-se como assistente virtual da clínica (não finge ser o dentista), mostra o aviso de privacidade e diz que não substitui consulta.

---

## 9. QUANDO A FASE 1 ESTÁ "PRONTA" (testes que você deve rodar e me mostrar)

1. **Tema comum** ("Escovação: 5 erros comuns"): em uma resposta, você entrega os slides, o .zip, a legenda e a lista de conferência. Nenhum texto cortado; identidade igual à dos exemplos.
2. **Tema fora do permitido** ("promoção de clareamento este mês", "como saber se tenho cárie"): você recusa ou reescreve, explicando em linguagem simples por quê.
3. **Tema que depende de serviço não confirmado** ("implante dentário"): você escreve de forma geral e me avisa que precisa de confirmação.
4. **Ajuste pontual** ("troca o slide 3 por um exemplo mais simples"): refaz só o slide pedido.
5. **Informação faltando** (CRO, @, horário): o carrossel sai sem esses itens e você me avisa quais faltam, sem travar.
6. **Registro:** `DECISOES.md` e `HISTORICO.md` atualizados e coerentes.

Quando todos passarem, me entregue um resumo de **até 10 linhas**: o que está pronto, como pedir um carrossel, onde ficam os arquivos, o que ainda depende de mim ou do Dr. Tiago e qual é o próximo passo recomendado.

---

**Comece agora pelo passo 1 da seção 6.**
````


---

## Apêndice A: exemplo completo de arquivo de conteúdo

Este é o carrossel "Siso" (`specs/siso.json`). O Hermes deve gerar arquivos exatamente neste formato.

```json
{
  "slug": "siso",
  "tema": "Cirurgia de siso: 5 perguntas e respostas",
  "objetivo": "Captar quem tem dúvida sobre cirurgia (especialidade do Dr. Tiago)",
  "slides": [
    {
      "type": "cover",
      "tag": "Cirurgia de siso",
      "title": [
        "Siso: tudo o",
        "que você precisa",
        "saber antes",
        "de tirar"
      ],
      "sub": "5 perguntas, 5 respostas."
    },
    {
      "type": "content",
      "badge": "Pergunta",
      "icon": "question",
      "color": "gold",
      "title": "Todo mundo precisa tirar o siso?",
      "headline": "Não.",
      "text": "Se o siso nasce completo, bem posicionado e dá para higienizar bem, ele pode ser mantido. A indicação depende da avaliação do dentista e, em geral, de uma radiografia.",
      "action": "Só a avaliação diz se o seu precisa sair."
    },
    {
      "type": "content",
      "badge": "Pergunta",
      "icon": "question",
      "color": "gold",
      "title": "Quando é indicado tirar?",
      "headline": "Quando ele traz risco ou problema.",
      "text": "Costuma ser indicado quando o siso está inclinado, preso no osso ou na gengiva, causa inflamações repetidas ou cárie, ou dificulta a limpeza.",
      "action": "A decisão é sempre caso a caso."
    },
    {
      "type": "content",
      "badge": "Pergunta",
      "icon": "question",
      "color": "gold",
      "title": "A cirurgia dói?",
      "headline": "Ela é feita com anestesia.",
      "text": "Durante o procedimento você não sente dor, apenas pressão. Depois pode haver desconforto e inchaço, e o dentista orienta como controlar.",
      "action": "Siga as orientações e os medicamentos indicados pelo dentista."
    },
    {
      "type": "content",
      "badge": "Pergunta",
      "icon": "question",
      "color": "gold",
      "title": "Como é a recuperação?",
      "headline": "Alguns dias de cuidado.",
      "text": "Inchaço e desconforto são esperados nos primeiros dias. Repouso, alimentação macia e higiene cuidadosa ajudam. O tempo varia de pessoa para pessoa.",
      "action": "Evite esforço e siga as instruções do pós-operatório."
    },
    {
      "type": "content",
      "badge": "Pergunta",
      "icon": "question",
      "color": "gold",
      "title": "Dá para esperar se não está doendo?",
      "headline": "Nem sempre.",
      "text": "Um siso mal posicionado pode causar inflamação e cárie no dente vizinho sem dar sintoma. Acompanhar com o dentista evita surpresas.",
      "action": "Mesmo sem dor, vale uma avaliação."
    },
    {
      "type": "cta",
      "title": "Ficou com dúvida sobre o siso?",
      "actions": [
        {
          "icon": "comment",
          "text": "Deixe sua dúvida nos comentários"
        },
        {
          "icon": "send",
          "text": "Envie para quem está com siso nascendo"
        },
        {
          "icon": "save",
          "text": "Agende uma avaliação para saber se o seu precisa sair"
        }
      ]
    }
  ]
}
```

---

## Apêndice B: checklist de revisão do Dr. Tiago

O Hermes entrega esta lista, adaptada ao tema, junto com cada carrossel (no máximo 5 itens). Modelo:

1. Todas as afirmações clínicas estão corretas e atualizadas? (marque as que quiser mudar)
2. Alguma frase pode soar como **promessa de resultado**, sensacionalismo ou autopromoção?
3. Há menção a **preço, desconto ou serviço gratuito**? (não deve haver)
4. Os serviços citados são **realmente oferecidos** pela clínica?
5. A orientação de urgência (quando houver) está de acordo com o que você recomenda aos pacientes?
6. Nome, CRO, telefone e endereço estão corretos?
7. Nenhuma imagem de paciente foi usada (só a foto do próprio Dr. Tiago)?

---

## Apêndice C: pendências com o cliente

| # | Item | Quem resolve | Como o Hermes lida enquanto não há resposta |
|---|------|--------------|---------------------------------------------|
| 1 | Número do CRO-SP | Dr. Tiago | Pergunta uma vez; carrossel sai sem o número e com aviso |
| 2 | @ do Instagram | Dr. Tiago | Sai sem o @ |
| 3 | Horários de atendimento | Dr. Tiago | Sai sem horário ("combine pelo WhatsApp") |
| 4 | Serviços confirmados (limpeza, restaurações, implantes, estética, crianças, ortodontia) | Dr. Tiago | Escreve de forma geral e avisa |
| 5 | Nome oficial ("de Odontologia" ou "Odontológica") | Dr. Tiago | Usa "Clínica Binhame" |
| 6 | Foto original em boa resolução | Dr. Tiago / fotógrafo | Usa o recorte atual |
| 7 | Posicionamento sobre "avaliação gratuita" e posts antigos | Dr. Tiago + CRO-SP | **Não usa** |
| 8 | Paleta do Instagram (teal) x logo (verde-oliva e dourado) | Dono do projeto | Segue o logo |
| 9 | Hospedagem e endereço do site | Dono do projeto | Não se aplica ao Hermes na Fase 1 |

---

## Apêndice D: glossário em linguagem simples (para o Hermes usar ao falar comigo)

| Em vez de dizer... | Diga... |
|--------------------|---------|
| API | uma conexão com outro serviço |
| Deploy / publicar o sistema | colocar no ar |
| Nuvem, VPS, servidor | um computador na internet que fica sempre ligado |
| Token / chave de API | uma senha que autoriza o programa a usar um serviço |
| Modelo / LLM | o "cérebro" de IA que escreve os textos |
| Prompt | as instruções que eu dou para a IA |
| Pipeline / workflow | o passo a passo automático |
| Repositório | a pasta onde ficam os arquivos do projeto |
| JSON | um arquivo de texto organizado, com os textos de cada slide |
| Render / renderizar | transformar o texto em imagem |
| Webhook / bot | um robô que conversa por mensagem |
| LGPD | a lei de proteção de dados pessoais |
| Log | o diário de tudo que o programa fez |
| Dependência | um programa auxiliar que precisa estar instalado |
| Instância | uma cópia do programa rodando |

---

## Apêndice E: mapa dos arquivos do pacote

```
pacote/
├── LEIA-ME.md                       resumo de 1 minuto
├── BRIEFING_E_PROMPT_HERMES.md      este documento
├── PROMPT_HERMES.md                 só o prompt, para copiar e colar
├── legendas-carrosseis.md           legendas e calendário dos 7 carrosséis
├── assets/
│   ├── logo.jpeg                    logo oficial (414x414)
│   ├── tiago_cut.webp               foto recortada do Dr. Tiago (usada pelo gerador)
│   └── tiago_cut.png                a mesma foto em PNG
├── engine/
│   ├── build_carousel.py            gerador de carrosséis (arquivo .json -> imagens PNG)
│   ├── carousel.css                 estilo visual dos slides
│   ├── clinic.json                  nome, WhatsApp e endereço da clínica
│   └── LEIA-ME.md                   como rodar o gerador
├── specs/                           os 7 carrosséis em arquivo de conteúdo (.json)
│   ├── habitos.json  higiene-bucal-sinais.json  medo-de-dentista.json
│   ├── clareamento-mitos.json  siso.json  dente-faltando.json  urgencia.json
├── exemplos/                        as imagens geradas a partir de cada .json
├── referencias/                     prints do Instagram usados como referência
└── site/
    └── clinica-binhame-landing.html landing page (arquivo único)
```
