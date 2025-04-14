
class Produto:
    def __init__(self):
        self.nome = None
        self.material = None
        self.preco = None
        self.descricao = None
        self.quantidade = None
        self.prazo = None
        self.opcoes_pagamento = {
                                '1': 'Pix',
                                '2': 'Crédito',
                                '3': 'Débito',
                                '4': 'Dinheiro'
                                }
        
    def informacoes_produto(self):
        self.nome = input('Digite o tipo do produto: ').title().strip()
        self.material = input ('Digite o material do produto: ').title().strip()
        self.descricao = input ('Digite o tipo de serviço a ser prestado: ').title().strip()
        
        return self.nome, self.material, self.descricao
    
    def prazo_servico(self):
        try:
            prazo = int(input('Digite o prazo de entrega do produto (em dias):'))

            if prazo <= 0:
                raise ValueError('O prazo não pode ser negativo.')
            
            self.prazo = prazo
            return self.prazo
        
        except ValueError:
            print('Valor inválido. Por favor, digite o número de dias.')

    def preco_produto(self):
        try:
            self.preco = float(input('Digite o preço do produto: '))
            
            if self.preco <= 0:
                raise ValueError('O preço não pode ser negativo.')
            return self.preco
        
        except ValueError:
            print('Valor inválido. Por favor, digite um número.')
    
    def forma_pagamento(self):
        while True: 
            print('Formas de pagamento: ')
            for key, value in self.opcoes_pagamento.items():
                print(f'{key} - {value}')

            pagamento = input('Escolha a forma de pagamento (1-4):' ).strip()
            if pagamento in self.opcoes_pagamento:
                    return self.opcoes_pagamento[pagamento]

            print('Opção inválida. Por favor, escolha uma opção válida.')
            
           