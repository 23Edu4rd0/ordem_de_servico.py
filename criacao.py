from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from datetime import datetime, timedelta
import textwrap
import cliente
import produto
import ordem_servico
import os
import sys

# Registro da fonte Arial
pdfmetrics.registerFont(TTFont('Arial', './fonts/ARIAL.TTF'))
pdfmetrics.registerFont(TTFont('Arial-Bold', './fonts/ARIBLK.TTF'))
dourado = HexColor('#bfa32f')

class CriarOrdemServico:
    def __init__(self):
        self.dados_empresa = {
            'nome': "Prata Nobre Joias",
            'endereco': "Rua das Artes, 120 - Loja 03 - Centro - Belo Horizonte - MG",
            'cnpj': "45.678.912/0001-33",
            'telefone': "(31) 98234-1122"
        }
        self.os = ordem_servico.OrdemServico()
        self.numero_os = self.os.numero_os()
        self.cliente = cliente.DadosCliente()
        self.nome_cliente = self.cliente.nome_cliente()
        self.cpf_cliente = self.cliente.documento_cliente()
        self.telefone_cliente = self.cliente.telefone_cliente()
        self.produto = produto.Produto()
        self.info_produto, self.material, self.descricao = self.produto.informacoes_produto()
        self.prazo = self.produto.prazo_servico()
        self.preco_produto = self.produto.preco_produto()
        self.forma_pagamento = self.produto.forma_pagamento()

    def draw_line(self, c, y, cor=colors.black, espessura=0.5):
        c.setStrokeColor(cor)
        c.setLineWidth(espessura)
        c.line(5*mm, y, 75*mm, y)

    def gerar_nota(self):
        try:
            nome_arquivo = "Teste.pdf"
            c = canvas.Canvas(nome_arquivo, pagesize=(80*mm, 250*mm))
            width, height = 80*mm, 250*mm
            y = height - 10*mm

            # Cabeçalho
            c.setFont("Arial-Bold", 9)
            c.drawCentredString(width/2, y, self.dados_empresa['nome'])
            y -= 4*mm
            c.setFont("Arial", 6)
            c.drawCentredString(width/2, y, f"CNPJ: {self.dados_empresa['cnpj']}")
            y -= 3*mm
            c.drawCentredString(width/2, y, self.dados_empresa['endereco'])
            y -= 3*mm
            c.drawCentredString(width/2, y, f"Tel: {self.dados_empresa['telefone']}")
            y -= 3*mm
            self.draw_line(c, y)
            y -= 5*mm

            # Ordem de Serviço
            c.setFont("Arial-Bold", 8)
            c.setFillColor(dourado)
            c.drawString(5*mm, y, "ORDEM DE SERVIÇO Nº")
            c.setFillColor(colors.black)
            c.setFont("Arial", 8)
            c.drawString(55*mm, y, self.numero_os.zfill(4))
            y -= 4*mm
            data_emissao = datetime.now().strftime('%d/%m/%Y %H:%M')
            c.drawString(5*mm, y, f"Data: {data_emissao}")
            y -= 2*mm
            self.draw_line(c, y)
            y -= 5*mm

            # Cliente
            c.setFont("Arial-Bold", 8)
            c.setFillColor(dourado)
            c.drawString(5*mm, y, "CLIENTE")
            c.setFillColor(colors.black)
            y -= 4*mm
            c.setFont("Arial", 7)
            c.drawString(5*mm, y, f"Nome: {self.nome_cliente}")
            y -= 4*mm
            c.drawString(5*mm, y, f"CPF: {self.cpf_cliente}")
            y -= 4*mm
            c.drawString(5*mm, y, f"Tel: {self.telefone_cliente}")
            y -= 2*mm
            self.draw_line(c, y)
            y -= 5*mm

            # Peça
            c.setFont("Arial-Bold", 8)
            c.setFillColor(dourado)
            c.drawString(5*mm, y, "PEÇA / JÓIA")
            c.setFillColor(colors.black)
            y -= 4*mm
            c.setFont("Arial", 7)
            c.drawString(5*mm, y, f"Tipo: {self.info_produto}")
            y -= 4*mm
            c.drawString(5*mm, y, f"Material: {self.material}")
            y -= 4*mm
            c.drawString(5*mm, y, f"Serviço: {self.descricao}")
            y -= 2*mm
            self.draw_line(c, y)
            y -= 5*mm

            # Prazo
            c.setFont("Arial-Bold", 8)
            c.setFillColor(dourado)
            c.drawString(5*mm, y, "PRAZO DE ENTREGA")
            c.setFillColor(colors.black)
            y -= 4*mm
            c.setFont("Arial", 7)
            data_entrega = (datetime.now() + timedelta(days=self.prazo)).strftime('%d/%m/%Y')
            c.drawString(5*mm, y, f"Previsão: {data_entrega}")
            y -= 4*mm
            c.drawString(5*mm, y, f"Prazo: {self.prazo} dias úteis")
            y -= 2*mm
            self.draw_line(c, y)
            y -= 5*mm

            # Orçamento
            c.setFont("Arial-Bold", 8)
            c.setFillColor(dourado)
            c.drawString(5*mm, y, "ORÇAMENTO")
            c.setFillColor(colors.black)
            y -= 4*mm
            c.setFont("Arial", 7)
            c.drawString(5*mm, y, f"Valor: R$ {float(self.preco_produto):.2f}".replace(".", ","))
            y -= 4*mm
            c.drawString(5*mm, y, f"Forma: {self.forma_pagamento}")
            y -= 2*mm
            self.draw_line(c, y)
            y -= 5*mm

            # Termos
            c.setFont("Arial-Bold", 8)
            c.setFillColor(dourado)
            c.drawString(5*mm, y, "TERMOS E CONDIÇÕES")
            c.setFillColor(colors.black)
            y -= 4*mm
            c.setFont("Arial", 5.5)

            termos = [
                '1. Peças não retiradas no prazo de 30 (trinta) dias serão consideradas propriedade da empresa.',
                '2. Garantia de 90 dias aplicável à mão de obra, conforme CDC.',
                '3. Valor pode variar conforme material e complexidade do serviço.',
                '4. Não aceitamos devoluções após 7 dias da entrega.',
                '5. Prazos podem mudar por aprovação ou falta de material.',
                '6. Alterações após início implicam novo prazo e valor.',
                '7. A garantia só é válida com este documento.'
            ]
            for termo in termos:
                linhas = textwrap.wrap(termo, width=70)
                for linha in linhas:
                    c.drawString(5*mm, y, linha)
                    y -= 3.5*mm
                y -= 1.5*mm
            self.draw_line(c, y, espessura=0.8)
            
            c.save()
            
            # Verificar se o arquivo foi criado
            if os.path.exists(nome_arquivo):
                print(f"\n OS gerada com sucesso: {nome_arquivo}")
                print(f" Tamanho do arquivo: {os.path.getsize(nome_arquivo)/1024:.2f} KB")
            else:
                print("\n❌ Erro: O arquivo PDF não foi criado")

        except Exception as e:
            print(f"\nErro ao gerar PDF: {str(e)}")
            sys.exit(1)
            
