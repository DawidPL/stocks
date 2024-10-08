from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from API.polygon import stock_detailed


class StockInfo(models.Model):


    def get_list_of_sectors():
        sectors = ['IT', 'Agro', 'Oil & Gas']
        return {i: i for i in sectors}
    
    ticket = models.CharField(max_length=4, unique=True)
    full_name = models.CharField(max_length=250, blank=True)
    sector = models.CharField(choices=get_list_of_sectors)

    def __str__(self) -> str:
        return self.ticket


@receiver(post_save, sender=StockInfo)
def _auto_add_stock_data(sender, instance, **kwargs):
    instance.full_name = stock_detailed(instance.ticket)
    instance.save()
    