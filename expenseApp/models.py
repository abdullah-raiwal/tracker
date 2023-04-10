from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class ExpenseManager(models.Manager):
    def create_expense(self, expense_item, date, value):
        expense_ = Expense(expense_item = expense_item, date=date, value=value)
        expense_.save()

    def get_expense(self, given_id):
        return Expense.objects.get(id = given_id)
    
    def update_expense(self,expense_id ,exppense_item = None, date=None, value = None):
        expense_ = self.get_expense(expense_id)
        if exppense_item:
            expense_.expense_item= exppense_item
        if date:
            expense_.date = date
        if value:
            expense_.value = value
        
        expense_.save()

    def delete_expense(self, expense_id):
        expense_ = Expense.objects.get(id = expense_id)
        expense_.delete()
# Create your models here.
class Expense(models.Model):

    expense_item = models.CharField(max_length=200, default=None, blank = False)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    value = models.IntegerField(blank = False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')



    def __str__(self):
        return self.expense_item

