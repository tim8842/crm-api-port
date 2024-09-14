from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    last_contact_date = models.DateField()


class Deal(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="deals"
    )
    deal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deal_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.client.name} - {self.deal_amount}"
