# DOODLE_RPA_Envio_de_WhatsApp

![Badge de Automação](https://img.shields.io/badge/Automação-RPA-blue)
![Badge de Selenium](https://img.shields.io/badge/Selenium-WebDriver-brightgreen)
![Badge de Python](https://img.shields.io/badge/Python-3.x-yellow)

## 📝 Sobre o Projeto | About the Project

### Português 🇧🇷

#### Descrição
O DOODLE_RPA_Envio_de_WhatsApp é uma solução de automação RPA (Robotic Process Automation) que permite o envio automatizado de mensagens e arquivos via WhatsApp Web. Desenvolvido com Python e Selenium WebDriver, este projeto é ideal para comunicações em massa com personalização de mensagens por destinatário.

#### Principais Funcionalidades
- ✅ Envio automatizado de mensagens personalizadas para múltiplos contatos
- 📁 Suporte para anexos de diversos tipos: imagens, PDFs, áudios e vídeos
- 📊 Geração de relatórios de envio com status de cada mensagem
- 📋 Integração com planilhas Excel para gerenciamento de contatos e mensagens
- 🔄 Sistema de recuperação de sessão para continuidade de operação

#### Aplicações Práticas
Ideal para:
- Marketing digital e campanhas promocionais
- Comunicação com equipes ou clientes
- Divulgação de conteúdo informativo ou educacional
- Notificações e comunicados institucionais

### English 🇺🇸

#### Description
DOODLE_RPA_Envio_de_WhatsApp is an RPA (Robotic Process Automation) solution that enables automated sending of messages and files via WhatsApp Web. Developed with Python and Selenium WebDriver, this project is perfect for mass communications with personalized messages for each recipient.

#### Key Features
- ✅ Automated sending of personalized messages to multiple contacts
- 📁 Support for various attachment types: images, PDFs, audio files, and videos
- 📊 Generation of delivery reports with status for each message
- 📋 Integration with Excel spreadsheets for contact and message management
- 🔄 Session recovery system for continuous operation

#### Practical Applications
Ideal for:
- Digital marketing and promotional campaigns
- Communication with teams or clients
- Distribution of informative or educational content
- Institutional notifications and announcements

## 🛠️ Tecnologias Utilizadas | Technologies Used

### Português 🇧🇷
- **Python**: Linguagem de programação principal
- **Selenium WebDriver**: Automação do navegador e interação com o WhatsApp Web
- **Pandas**: Manipulação e processamento de dados
- **Chrome WebDriver**: Driver para controle do navegador Chrome
- **DatetTime**: Manipulação de datas e horários para registro de atividades
- **OS & Glob**: Gerenciamento de arquivos e diretórios
- **urllib.parse**: Formatação de URLs para envio de mensagens

### English 🇺🇸
- **Python**: Main programming language
- **Selenium WebDriver**: Browser automation and WhatsApp Web interaction
- **Pandas**: Data manipulation and processing
- **Chrome WebDriver**: Driver for Chrome browser control
- **DateTime**: Date and time handling for activity logging
- **OS & Glob**: File and directory management
- **urllib.parse**: URL formatting for message sending

## 📋 Pré-requisitos | Prerequisites

### Português 🇧🇷
- Python 3.x
- Google Chrome instalado
- Dependências listadas no arquivo `requirements.txt`
- Smartphone com WhatsApp instalado para autenticação inicial

### English 🇺🇸
- Python 3.x
- Google Chrome installed
- Dependencies listed in the `requirements.txt` file
- Smartphone with WhatsApp installed for initial authentication

## 🚀 Instalação e Uso | Installation and Usage

### Português 🇧🇷

#### Instalação
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/DOODLE_RPA_Envio_de_WhatsApp.git
cd DOODLE_RPA_Envio_de_WhatsApp
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

#### Estrutura de Diretórios
Certifique-se de que os seguintes diretórios existam no projeto:
- `mensagens/`: Contém o arquivo Excel com os destinatários e mensagens
- `imagens/`: Arquivos de imagem para envio
- `pdf/`: Documentos PDF para envio
- `audio/`: Arquivos de áudio para envio
- `video/`: Arquivos de vídeo para envio
- `relatorios/`: Armazena relatórios de envio
- `cache/`: Armazena dados de sessão do Chrome

#### Formato do Arquivo de Mensagens
Crie um arquivo Excel em `mensagens/mensagens.xlsx` com as seguintes colunas:
- `NUMERO`: Número do telefone (apenas dígitos)
- `NOME`: Nome do destinatário
- `TEXTO`: Conteúdo da mensagem

#### Execução
```bash
python main.py
```

Na primeira execução, escaneie o QR code com seu WhatsApp para autenticar.

### English 🇺🇸

#### Installation
1. Clone this repository:
```bash
git clone https://github.com/your-username/DOODLE_RPA_Envio_de_WhatsApp.git
cd DOODLE_RPA_Envio_de_WhatsApp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

#### Directory Structure
Make sure the following directories exist in the project:
- `mensagens/`: Contains the Excel file with recipients and messages
- `imagens/`: Image files for sending
- `pdf/`: PDF documents for sending
- `audio/`: Audio files for sending
- `video/`: Video files for sending
- `relatorios/`: Stores sending reports
- `cache/`: Stores Chrome session data

#### Message File Format
Create an Excel file in `mensagens/mensagens.xlsx` with the following columns:
- `NUMERO`: Phone number (digits only)
- `NOME`: Recipient name
- `TEXTO`: Message content

#### Execution
```bash
python main.py
```

On first execution, scan the QR code with your WhatsApp to authenticate.

## 📝 Funcionalidades Detalhadas | Detailed Features

### Português 🇧🇷
- **Personalização de Mensagens**: Concatena o nome do destinatário com o texto da mensagem
- **Verificação de Status**: Registra o status de cada envio (Enviada/Erro)
- **Manipulação de Exceções**: Tratamento robusto de erros para garantir continuidade da operação
- **Relatórios Detalhados**: Gera relatórios com timestamp para análise posterior
- **Cache de Sessão**: Evita a necessidade de escanear o QR code em cada execução

### English 🇺🇸
- **Message Customization**: Concatenates recipient name with message text
- **Status Verification**: Records the status of each delivery (Sent/Error)
- **Exception Handling**: Robust error handling to ensure operation continuity
- **Detailed Reports**: Generates timestamped reports for later analysis
- **Session Caching**: Avoids the need to scan the QR code on each execution

## 📊 Recursos Avançados | Advanced Features

### Português 🇧🇷
- Capacidade de lidar com diferentes tipos de mídia
- Sistema de logs para acompanhamento em tempo real
- Maximização automática da janela para melhor visualização
- Tratamento de diferentes XPATHs para adaptação a mudanças na interface do WhatsApp Web

### English 🇺🇸
- Capability to handle different media types
- Logging system for real-time monitoring
- Automatic window maximization for better visibility
- Handling of different XPATHs to adapt to changes in the WhatsApp Web interface

## 👥 Contribuição | Contributing

### Português 🇧🇷
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

### English 🇺🇸
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 Licença | License

### Português 🇧🇷
Este projeto está licenciado sob os termos da licença MIT.

### English 🇺🇸
This project is licensed under the terms of the MIT license.

---

⭐ Desenvolvido com foco em automação eficiente e confiável para comunicações em escala.

⭐ Developed with a focus on efficient and reliable automation for communications at scale.
