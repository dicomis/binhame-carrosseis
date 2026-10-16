# DECISÕES DO PROJETO - FÁBRICA DE CARROSSÉIS BINHAME

- **Data:** 16/10/2026
- **D1 (Onde o agente/motor vai rodar):** Escolhido rodar no host da VPS (ambiente Ubuntu), onde os arquivos, assets e engine já estão centralizados.
- **D2 (Cérebro/Modelo de IA):** Gemini 3.7 Flash para escrita e orquestração (preciso, cota free, contexto longo para conformidade ética).
- **D3 (Como pedir carrosséis na Fase 1):** Via Hermes (conversa direta aqui no terminal).
- **D4 (Aprovação):** Dr. Tiago revisa o conteúdo clínico; Diego revisa visual e legenda.
- **D5 (Pesquisa na internet):** Liberada quando necessário para checagem de fatos odontológicos em fontes confiáveis.
- **D6 (Onde salvar):** Em subpastas organizadas por data e tema dentro de `/home/ubuntu/pacote-hermes-binhame/saida/`.
- **D9 (Fase 2A - Bot da equipe no Telegram):** Escolhido Telegram com o bot compartilhado @binhameimagensbot (Diego + Dr. Tiago). O Tiago manda o tema pelo bot e recebe o carrossel pronto (imagens + legenda + checklist) direto no chat. Autonomia nível 0: nada é publicado automaticamente, tudo sai como RASCUNHO para aprovação humana.
- **D2-atualização (Modelo de IA):** gemini-2.0-flash-exp foi descontinuado pela API. Substituído por gemini-3.1-flash-lite (free tier Google AI). Testado em 16/10/2026: gera JSON dentro dos limites e sem termos vedados.
- **Parceria Diego + Dr. Tiago (16/10/2026):** Projeto Binhame é uma parceria real: Diego cuida da tecnologia (Hermes, bot, fábrica de carrosséis) e o Dr. Tiago Binhame assume a revisão clínica e a aprovação final de todo conteúdo antes de publicar no Instagram da clínica. O bot compartilhado @binhameimagensbot é o canal de trabalho entre os dois. Pendências D7 continuam com o Tiago: CRO-SP, @ do Instagram, horários, serviços confirmados e foto original.
