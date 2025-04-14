from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime, timedelta

def draw_line(c, x1, y1, x2, y2):
    c.setStrokeColor(colors.black)
    c.line(x1, y1, x2, y2)

opcoes_pagamento = {
    '1': 'Pix',
    '2': 'Crédito',
    '3': 'Débito',
    '4': 'Dinheiro Físico'
}

data_e_hora_atuais = datetime.now()
data_e_hora_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

c = canvas.Canvas("teste.pdf", pagesize=letter)
width, height = letter

c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 50, "Registro de Ordem de Serviço")
draw_line(c, 75, height - 55, 500, height - 55)

try:
    c.drawImage("logo.png", width - 100, height - 50, width=50, height=50, preserveAspectRatio=True)
except:
    pass

numero_os = input("Digite o número da OS: ")
c.setFont("Helvetica", 10)
c.drawString(100, height - 70, f'OuriPrata - Ourivesaria')
c.drawString(100, height - 85, f'CNPJ: 00.000.000/0000-00')
c.drawString(350, height - 70, f'Número da OS: {numero_os}')
c.drawString(350, height - 85, f'Data de Emissão: {data_e_hora_texto}')

c.setFont("Helvetica-Bold", 14)
c.drawString(100, height - 120, "DADOS DO CLIENTE")
draw_line(c, 100, height - 125, 500, height - 125)

nome_cliente = input("Digite o nome do cliente: ")
telefone_cliente = input("Digite o telefone do cliente: ")

c.setFont("Helvetica", 10)
c.drawString(100, height - 140, f'Nome: {nome_cliente}')
c.drawString(100, height - 155, f'Telefone: {telefone_cliente}')

modelo_produto = input("Informe o modelo do produto: ")
detalhes_produto = input("Informe os detalhes do produto: ")

c.setFont("Helvetica-Bold", 14)
c.drawString(100, height - 180, "DADOS DO PRODUTO")
draw_line(c, 100, height - 185, 500, height - 185)
c.setFont("Helvetica", 10)
c.drawString(100, height - 200, f'Modelo: {modelo_produto}')
c.drawString(100, height - 215, f'Detalhes: {detalhes_produto}')

c.setFont("Helvetica-Bold", 14)
c.drawString(100, height - 240, "ORÇAMENTO")
draw_line(c, 100, height - 245, 500, height - 245)

valor_estimado = input("Digite o valor estimado: ")
while True:
    forma_pagamento = input("Digite a forma de pagamento (1 - Pix / 2 - Crédito / 3 - Débito / 4 - Dinheiro Físico): ")
    if forma_pagamento in opcoes_pagamento:
        forma_pagamento = opcoes_pagamento[forma_pagamento]
        break
    else:
        print("Opção inválida. Digite uma opção válida.")

c.setFont("Helvetica", 10)
c.drawString(100, height - 260, f'Valor estimado: {valor_estimado}')
c.drawString(100, height - 275, f'Forma de pagamento: {forma_pagamento}')

c.setFont("Helvetica-Bold", 14)
c.drawString(100, height - 300, "PRAZOS")
draw_line(c, 100, height - 305, 500, height - 305)

quantidade_dias_entrega = input("Digite a quantidade de dias para entrega (Se vazio será 30):").strip()
quantidade_dias_entrega = int(quantidade_dias_entrega) if quantidade_dias_entrega.isdigit() else 30
data_de_entrega = data_e_hora_atuais + timedelta(days=quantidade_dias_entrega)
data_de_entrega = data_de_entrega.strftime('%d/%m/%Y')

c.setFont("Helvetica", 10)
c.drawString(100, height - 320, f'Prazo estimado para entrega: {data_de_entrega}')
c.drawString(100, height - 335, f'Política de retirada: Peças não retiradas em 30 dias serão revendidas para o estoque.')

c.showPage()
c.save()

print("PDF gerado com sucesso")