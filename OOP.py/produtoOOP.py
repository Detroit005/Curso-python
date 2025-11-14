class Produto:
    # Atributos
    nome:str 
    preco:float 
    saldo=int 
    # metodos
    def valorte(self)->float:
        return self.preco * self.saldo
    def adicionarp(self,quantidade)->int:
        self.saldo = self.saldo+quantidade 
        return self.saldo
    def removerpro(self, quantidade)->int:
        self.saldo = self.saldo - quantidade