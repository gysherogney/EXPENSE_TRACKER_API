# expenses/serializers.py
from rest_framework import serializers
from .models import Category, Expense, BudgetLimit, Alert, MonthlySpending

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['user'] 

class BudgetLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetLimit
        fields = '__all__'
        read_only_fields = ['user'] 

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

class MonthlySpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlySpending
        fields = '__all__'
