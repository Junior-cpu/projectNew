from django.db import models

# Create your models here.



class Magazine(models.Model):

     STATUS =(
        ('901','901'),
        ('902','902'),
        ('904','904'),
        ('913','913'),
        ('915','915'),
        ('917','917'),
        ('918','918'),
        ('919','919'),
        ('920','920'),
        ('932','932'),
        ('933','933'),
        ('935','935'),
        ('936','936'),
        ('937','937'),
        ('938','938'),
        ('939','939'),
    )

     numero = models.CharField(max_length=20)  
    
     bocal_1 = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    
     bocal_2 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_3 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_4 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_5 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_6 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_7 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_8 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_9 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_10 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_11 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
     bocal_12 = models.CharField(
        max_length=5,
        choices=STATUS,
    )  
   

     def __str__(self):
        return self.numero
    

class Nozzle(models.Model):
    modelo = models.CharField(max_length=10)
    quantidade = models.IntegerField()
    

    def __str__(self):
        return self.modelo


class Maquina(models.Model):
    descricao = models.CharField(max_length=10)  
     

    def __str__(self):
        return self.descricao
       

class Location(models.Model):
    loc = models.CharField(max_length=1)   
    magazine = models.ForeignKey(Magazine,on_delete=models.CASCADE)  

    def __str__(self):
        return self.loc

class Linha(models.Model):
    linha = models.CharField(max_length=2)  
    
    def __str__(self):
        return self.linha      

class Machine(models.Model):
    linha = models.ForeignKey(Linha,on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina,on_delete=models.CASCADE)
    loc = models.ForeignKey(Location,on_delete=models.CASCADE)
    
   

   
   