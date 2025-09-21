# 📦 QR Code Generator (CLI)

Um gerador de QR Codes simples e direto, feito em **Python** para rodar no terminal (CLI).  
Com ele, você pode transformar rapidamente qualquer texto ou URL em um QR Code, que será salvo automaticamente como uma imagem `.png`.

---

## 🚀 Funcionalidades
- Gera QR Codes a partir de **URLs ou textos**.
- Salva automaticamente os arquivos em formato **PNG** com a data no nome (`dia-mês-ano_qr_code.png`).
- Interface amigável em linha de comando.
- Opção para gerar múltiplos QR Codes em sequência.

---

## 📂 Estrutura do Projeto
```bash
📦 qr-code-generator
┣ 📜 main.py # Script principal com a interface CLI
┣ 📜 generate_qr.py # Lógica para criação e salvamento do QR Code
┣ 📜 utils.py # Funções utilitárias (ex: limpar_tela)
┣ 📜 README.md # Documentação do projeto
```

---

## ⚙️ Pré-requisitos

- **Python 3.8+** instalado.
- Biblioteca **qrcode** do Python.  
- Para instalar:
  
```bash
pip install qrcode[pil]
```

---

## ▶️ Como Usar

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/qr-code-generator.git
cd qr-code-generator
```

Execute o script principal:

```bash
python main.py
```

Insira uma URL ou texto quando solicitado:

🔗 Digite a URL ou texto para gerar o QR Code: `https://github.com`

O QR Code será salvo no diretório do projeto com o nome: `20-09-2025_qr_code.png`

---

## 📸 Exemplo de Saída

Após gerar, você terá um arquivo `.png` no diretório atual, contendo o QR Code correspondente.

---

## 👨‍💻 Autor

Feito com 💻 e ☕ por Dave G. Farias (o brabo)

---

## 📜 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar.