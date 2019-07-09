from django.db import models

#Cadastro de todas graduações, para informar no cadastro do militar via foreignKey
class Graduacoes(models.Model):
    graduacao = models.CharField("Graduação", max_length=15, )

    class Meta:
        verbose_name_plural = "Graduações"

    def __str__(self):
        return self.graduacao

#Cadastro das 3 categorias dos militares, para informar no cadastro do militar via foreignKey
class Categoria(models.Model):
    categoria = models.CharField("Categoria", max_length=15)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria

#Cadastro das companhias do batalhão, para informar no cadastro do militar via foreignKey
class Companhia(models.Model):
    companhia = models.CharField("Companhia", max_length=15)

    class Meta:
        verbose_name_plural = "Companhia"

    def __str__(self):
        return self.companhia

#Cadastro do militar, onde recebe 3 foreignKey
class Cadastro(models.Model):
    nome = models.CharField("Nome de Guerra", max_length=100)
    companhia = models.ForeignKey(Companhia, on_delete=models.CASCADE)
    graduacao = models.ForeignKey(Graduacoes, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Militares Cadastrados"

    def __str__(self):
        return self.nome

#Cadastra os dias da semana para informar no cardapio via foreignKey
class Dias(models.Model):
    dias_semana = models.CharField("Dia da Semana",max_length=15)

    class Meta:
        verbose_name_plural = "Dias da Semana"
    def __str__(self):
        return self.dias_semana

#Cadastra o cardapio, recebe 1 foreignKey
class Cardapio(models.Model):
    data = models.DateTimeField("Data")
    dia_semana = models.ForeignKey(Dias, on_delete=models.CASCADE)
    cafe = models.CharField("Café", max_length=300)
    almoco = models.CharField("Almoço", max_length=300)
    janta = models.CharField("Jantar", max_length=300)

    class Meta:
        verbose_name_plural = "Cardápio"

    def __int__(self):
        return self.dia_semana
    #
    # def __str__(self):
    #     return self.dia_semana


#Arranchamento individual
class Arranchar(models.Model):
    militar = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    dia_semana = models.ForeignKey(Dias, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Militar Arranchado"
    # def __str__(self):
    #     return self.militar

class OutrosArranchados(models.Model):
    #dia_semana = models.ForeignKey(Dias, on_delete=models.CASCADE)
    baixados = models.IntegerField("Militares Baixados")
    servico = models.IntegerField("Militares de Serviço")
    outro_batalhao = models.IntegerField("Militares de Outro Batalhão")

    class Meta:
        verbose_name_plural = "Outros Arranchados"

    # def __str__(self):
    #     return self.dia_semana

class TotalArranchados(models.Model):
    # dia_semana = models.ForeignKey(Dias, on_delete=models.CASCADE)
    data = models.DateTimeField("Data")
    arranchar = models.ForeignKey(Arranchar, on_delete=models.CASCADE)
    outros_arranchados = models.ForeignKey(OutrosArranchados, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Total de Arranchados"



