from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category.name} - {self.amount}'


class BudgetLimit(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budget_limit')
    month = models.PositiveSmallIntegerField()
    year = models.PositiveIntegerField()
    limit_amount = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('category', 'month', 'year')

    def __str__(self):
        return f'{self.category.name} - {self.month}/{self.year}'


class Alert(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='alerts')
    month = models.PositiveSmallIntegerField()
    year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return f'Alert - {self.category.name} - {self.month}/{self.year}'


class MonthlySpending(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='monthly_spending')
    month = models.PositiveSmallIntegerField()
    year = models.PositiveIntegerField()
    total_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        unique_together = ('category', 'month', 'year')

    def __str__(self):
        return f'{self.category.name} - {self.month}/{self.year} = {self.total_spent}'
