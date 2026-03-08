# 📸 MTHS.PUBLI - Portfólio Audiovisual
Este projeto é um site de portfólio dinâmico desenvolvido para o profissional de publicidade Matheus Rial. A aplicação utiliza Python com o microframework Flask para renderizar uma interface moderna que consome dados em tempo real diretamente de uma planilha do Google Sheets.
---
# 🚀 Funcionalidades
Gerenciamento Dinâmico: O conteúdo do site (fotos e vídeos) é atualizado instantaneamente através de uma planilha remota, sem necessidade de deploy ou alteração no código fonte.

Suporte Híbrido de Mídia: Sistema preparado para exibir imagens do ImgBB e vídeos integrados via YouTube (incluindo Shorts) e Google Drive.

Interface Responsiva: Layout "simples mas chamativo", totalmente otimizado para navegação em dispositivos móveis e desktop.

Efeitos Visuais: Implementação de animações fade-in ao rolar a página e filtros interativos nas imagens de perfil e portfólio.
---
# 🛠️ Tecnologias Utilizadas
Backend: Python 3 + Flask (Microframework).

Frontend: HTML5, CSS3 (CSS Grid e Flexbox).

Dados: Integração com Google Sheets via Pandas/CSV.

Hospedagem de Arquivos: Google Drive, YouTube e ImgBB.
---
# 📋 Estrutura da Planilha
(Google Sheets)Para que o sistema processe os dados corretamente, a planilha deve ser configurada com as seguintes colunas:Tipo (A)Link (B)Descriçãofotohttps://i.ibb.co/...Link direto da imagem (final .jpg ou .png).videohttps://www.youtube.com/embed/...Link de incorporação para vídeos/shorts do YouTube.videohttps://drive.google.com/file/d/.../previewLink de visualização (preview) para vídeos do Drive.
