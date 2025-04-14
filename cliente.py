import re


class DadosCliente:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.telefone = None
        
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False
        
        return True
    
    @staticmethod
    def validar_cnpj(cnpj: str) -> bool:
        if not re.match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj):
            return False

        # Obtém apenas os números do CNPJ, ignorando pontuações
        numbers = [int(digit) for digit in cnpj if digit.isdigit()]

        # Validação do primeiro dígito verificador
        sum_of_products = sum(a * b for a, b in zip(numbers[0:12], range(5, 1, -1)))
        digit1 = (sum_of_products * 10 % 11) % 10
        if numbers[12] != digit1:
            return False

        # Validação do segundo dígito verificador
        sum_of_products = sum(a * b for a, b in zip(numbers[0:13], range(6, 1, -1)))
        digit2 = (sum_of_products * 10 % 11) % 10
        if numbers[13] != digit2:
            return False

        return True
    

    
    def nome_cliente(self):
        while True:
            self.nome = str(input('Digite o nome do cliente: ')).title().strip()
            
            if len(self.nome) >= 3 and self.nome.isalpha():
                return self.nome
            
            else:
                print('Nome inválido. Informe um nome valido.')
        
    
    def documento_cliente(self):
        while True:
            self.documento = str(input('Digite o Cpf ou Cnpj do cliente (Insira a potuação) ')).strip()
            
            if len(self.documento) == 14 and DadosCliente.validar_cpf(self.documento):
                return self.documento
            elif len(self.documento) == 18 and DadosCliente.validar_cnpj(self.documento):
                return self.documento

            
            
            
            else:
                print('Documento inválido. Informe um valido.')
            
            
    def telefone_cliente(self):
        while True:
            telefone = str(input('Digite o numero do telefone do cliente:')).strip()
            
            if len(telefone) >= 10 and telefone.isdigit():
                self.telefone = telefone
                return self.telefone
            else:
                print('Telefone inváliido. Informe um numero valido;')