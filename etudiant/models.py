from django.db import models
from django.urls import reverse

# Create your models here.


class Niveau(models.Model):
    libelle = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.libelle

    def __repr__(self):
        return 'Niveau : ' + self.libelle

class Classe(models.Model):

    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    nom_classe = models.CharField(blank=False, max_length=150)
    description_classe = models.CharField(blank=True, max_length=150)

    def __str__(self):
        return self.nom_classe

    def __repr__(self):
        return 'Classe : ' + self.nom_classe


class Filiere(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    Intitu_filiere = models.CharField(max_length=100)


    def __str__(self):
        return self.Intitu_filiere

    def __repr__(self):
        return 'Filiere : ' + self.Intitu_filiere


class Etudiant(models.Model):

    CHOICES = (('1', ' '),
               ('Garcon', 'Garcon'),
               ('Fille', 'Fille'))

    classe_courant = models.ForeignKey(
        Classe,
        on_delete=models.CASCADE,
    )
    id = models.AutoField(primary_key=True)
    #date = models.DateField()
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    sexe = models.CharField(max_length=10, choices=CHOICES)
    address = models.CharField(max_length=150)
    CNE = models.CharField(max_length=30)
    date_naissance = models.DateField()
    est_etudiant = models.BooleanField(default=True)

    def full_name(self):
        return '{} {}'.format(self.nom, self.prenom).capitalize()

    full_name.admin_order_field = 'first_name'

    @property
    def get_detail(self):
        return '{} Class - {}'.format(self.classe_courant, self.full_name)

    def __str__(self):
        return self.full_name()

    @property
    def generate_CNE(self):
        return '{}EM-{}'.format(self.classe_courant, self.full_name)

    def get_absolute_url(self):
        return reverse('etudiant:student_create', kwargs={'pk': self.pk})