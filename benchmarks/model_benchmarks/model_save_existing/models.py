from django.db import models

from ...utils import bench_setup

bench_setup()


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
