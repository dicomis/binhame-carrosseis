# Gerador de carrosséis

Transforma um arquivo de conteúdo (`.json`, veja a pasta `../specs`) em imagens PNG de 1080x1350 (formato vertical do Instagram), no padrão visual da Clínica Binhame.

## Preparar (uma vez)
```
pip install playwright
playwright install chromium
```
As fontes **Lora** e **Poppins** carregam do Google Fonts quando há internet. Sem internet, instale as duas no computador.

## Usar
```
python build_carousel.py ../specs/urgencia.json --out ../saida/urgencia
```
Saída: `slide-01.png`, `slide-02.png`, ... na pasta indicada.

- O programa **avisa** se algum texto não couber. Nesse caso, encurte o texto do slide indicado e rode de novo.
- Dados da clínica (nome, WhatsApp, endereço): `clinic.json`.
- Cores, fontes e tamanhos: `carousel.css`. **Não alterar** sem aprovação (identidade visual).
- Foto e logo: pasta `../assets` (`tiago_cut.webp`, `logo.jpeg`). Para trocar a foto, mantenha o mesmo nome e o formato com fundo transparente.
