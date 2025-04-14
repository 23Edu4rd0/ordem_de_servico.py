import cliente
import produto

class OrdemServico:
    def __init__(self):
        pass
        
    
    def obter_input(self, mensagem, tipo=str, validador=None, padrao=None):
        while True:
            try:
                entrada = input(mensagem).strip()
                if not entrada and padrao is not None:
                    return padrao
                if validador and not validador(entrada):
                    raise ValueError("Entrada inválida")
                if tipo != str:
                    return tipo(entrada)
                return entrada
            except ValueError as e:
                print(f"Erro: {e}. Por favor, tente novamente.")
        
    def numero_os(self):
        numero_os = self.obter_input("Digite o número da OS: ", tipo=str, validador=lambda x: x.isdigit(), padrao="0000")
        return numero_os
    

