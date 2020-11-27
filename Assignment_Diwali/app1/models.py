from django.db import models

class plot_db(models.Model):
    plot_no = models.IntegerField(primary_key=True)
    road_no = models.IntegerField(max_length=3)
    survey_no = models.IntegerField(max_length=3)
    cost_per_sq_yard = models.IntegerField(max_length=8)
    other_expense = models.IntegerField(max_length=4)
    boundaries = models.IntegerField(max_length=2)
    