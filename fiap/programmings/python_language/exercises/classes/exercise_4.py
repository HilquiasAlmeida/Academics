"""
Módulo: Calculadora de Notas - FIAP
Descrição: Script orientado a objetos para cálculo de médias acadêmicas 
           de Computational Thinking, respeitando as restrições de lógica.
Autor: Seu Nome
"""

class CalculadoraNotasFIAP:
    """Classe responsável por gerenciar e calcular as médias semestrais."""
    
    def __init__(self, cp1: float, cp2: float, cp3: float, sp1: float, sp2: float, gs: float) -> None:
        self.cp1 = cp1
        self.cp2 = cp2
        self.cp3 = cp3
        self.sp1 = sp1
        self.sp2 = sp2
        self.gs = gs
        
        # Atributos de saída calculados posteriormente
        self.menor_cp: float = 0.0
        self.media_final: float = 0.0
        self.media_peso: float = 0.0

    def _identificar_menor_cp(self) -> float:
        """Método privado para identificar a menor nota de CP sem usar min()."""
        if self.cp1 <= self.cp2 and self.cp1 <= self.cp3:
            return self.cp1
        elif self.cp2 <= self.cp1 and self.cp2 <= self.cp3:
            return self.cp2
        else:
            return self.cp3

    def processar_calculos(self) -> None:
        """Executa todas as regras de negócio para o cálculo das médias."""
        self.menor_cp = self._identificar_menor_cp()
        
        # Cálculo da média das atividades (descartando o menor checkpoint)
        soma_atividades = (self.cp1 + self.cp2 + self.cp3 - self.menor_cp) + self.sp1 + self.sp2
        media_cs = soma_atividades / 4
        
        # Médias finais
        self.media_final = (media_cs * 0.4) + (self.gs * 0.6)
        self.media_peso = self.media_final * 0.4

    def exibir_resultados(self) -> None:
        """Exibe os resultados formatados de forma amigável no console."""
        print("\n" + "="*35)
        print("      📊 RESULTADOS DO SEMESTRE      ")
        print("="*35)
        print(f"🔹 Menor Checkpoint descartado: {self.menor_cp:.1f}")
        print(f"🔹 Média do semestre sem peso:  {self.media_final:.1f}")
        print(f"🔹 Média do semestre com peso:  {self.media_peso:.1f}")
        print("="*35)


def obter_nota_valida(mensagem: str) -> float:
    """
    Função utilitária para garantir que o usuário digite um valor numérico válido,
    evitando que o programa quebre por erro de digitação.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite um número decimal (ex: 8.5).")


# Bloco de execução principal (Padrão Profissional)
if __name__ == "__main__":
    print("-----------------------------------------")
    print("  SISTEMA DE CÁLCULO DE MÉDIAS - FIAP   ")
    print("-----------------------------------------")

    # 1. Entrada de dados com validação profissional
    cp1 = obter_nota_valida("Digite a nota do Checkpoint 1: ")
    cp2 = obter_nota_valida("Digite a nota do Checkpoint 2: ")
    cp3 = obter_nota_valida("Digite a nota do Checkpoint 3: ")
    sp1 = obter_nota_valida("Digite a nota da Sprint 1: ")
    sp2 = obter_nota_valida("Digite a nota da Sprint 2: ")
    gs = obter_nota_valida("Digite a nota da Global Solution: ")

    # 2. Instanciação do objeto e processamento dos dados
    calculadora = CalculadoraNotasFIAP(cp1, cp2, cp3, sp1, sp2, gs)
    calculadora.processar_calculos()

    # 3. Saída dos dados
    calculadora.exibir_resultados()
