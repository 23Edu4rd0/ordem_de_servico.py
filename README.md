# Ordem de Serviço - Geração de PDF

Este projeto tem como objetivo gerar ordens de serviço em formato PDF para uma loja de joias ou outro comércio que atue com controle de atendimento, orçamento e garantia de produtos/serviços. Foi usado focado em uma loja de joias somente para servir de exemplo.

## Funcionalidades

- Geração de PDF com os dados da empresa, cliente e produto
- Cálculo de valores e inserção da forma de pagamento
- Inclusão de termos e condições personalizáveis
- Layout estruturado com campos bem posicionados
- Uso de bibliotecas profissionais como ReportLab

## Tecnologias utilizadas

- Python 3.10+
- [ReportLab](https://www.reportlab.com/) para geração de PDFs
- Flask (opcional) caso queira servir a aplicação via web
- Instaloader (opcional) se houver integração com Instagram ou automação

## Instalação

Clone o repositório:

```bash
git clone https://github.com/23Edu4rd0/ordem_de_servico.py.git
cd ordem_de_servico.py
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Instale as dependências mínimas:

```bash
pip install -r requirements.txt
```

## Como usar

Você pode executar o script principal para gerar um PDF com os dados desejados:

```bash
python main.py
```

O PDF será gerado com os dados de cliente, produto e forma de pagamento, além dos termos de garantia e condições definidos no próprio código.

## Estrutura do Projeto

```
ordem_de_servico.py/
├── cliente.py
├── main.py
├── ordem_servico.py
├── produto.py
├── test.py
├── requirements.txt
```

- `cliente.py`: define a estrutura e dados do cliente.
- `produto.py`: define os dados do produto ou serviço prestado.
- `ordem_servico.py`: classe principal que gera o PDF.
- `main.py`: exemplo de uso e execução.
- `test.py`: arquivo auxiliar para testes rápidos.


