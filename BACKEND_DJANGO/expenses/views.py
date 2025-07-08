from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Expense, BudgetLimit, Alert, MonthlySpending
from .serializers import (
    CategorySerializer,
    ExpenseSerializer,
    BudgetLimitSerializer,
    AlertSerializer,
    MonthlySpendingSerializer
)

# ==========================
# CATEGORY VIEWS
# ==========================
@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {'error': 'Invalid data', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {'error': 'Category not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {'error': 'Invalid data', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        category.delete()
        return Response(
            {'message': 'Category deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

# ==========================
# EXPENSE VIEWS
# ==========================
@api_view(['GET', 'POST'])
def expense_list_create(request):
    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {'error': 'Invalid data', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'PUT', 'DELETE'])
def expense_detail(request, pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(
            {'error': 'Expense not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ExpenseSerializer(expense, data=request.data)
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
               serializer.save()  

        return Response(
            {'error': 'Invalid data', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        expense.delete()
        return Response(
            {'message': 'Expense deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

# ==========================
# BUDGET LIMIT VIEWS
# ==========================
@api_view(['GET', 'POST'])
def budget_list_create(request):
    if request.method == 'GET':
        limits = BudgetLimit.objects.all()
        serializer = BudgetLimitSerializer(limits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BudgetLimitSerializer(data=request.data)
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()  # 👈 assign user from request

        return Response(
            {'error': 'Invalid data', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'PUT', 'DELETE'])
def budget_detail(request, pk):
    try:
        limit = BudgetLimit.objects.get(pk=pk)
    except BudgetLimit.DoesNotExist:
        return Response(
            {'error': 'Budget limit not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = BudgetLimitSerializer(limit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BudgetLimitSerializer(limit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {'error': 'Invalid data', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        limit.delete()
        return Response(
            {'message': 'Budget limit deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

# ==========================
# ALERT VIEWS (READ & DELETE ONLY)
# ==========================
@api_view(['GET'])
def alert_list(request):
    alerts = Alert.objects.all()
    serializer = AlertSerializer(alerts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def alert_detail(request, pk):
    try:
        alert = Alert.objects.get(pk=pk)
    except Alert.DoesNotExist:
        return Response(
            {'error': 'Alert not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = AlertSerializer(alert)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        alert.delete()
        return Response(
            {'message': 'Alert deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

# ==========================
# MONTHLY SPENDING VIEWS (READ ONLY)
# ==========================
@api_view(['GET'])
def spending_list(request):
    records = MonthlySpending.objects.all()
    serializer = MonthlySpendingSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def spending_detail(request, pk):
    try:
        record = MonthlySpending.objects.get(pk=pk)
    except MonthlySpending.DoesNotExist:
        return Response(
            {'error': 'Spending record not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = MonthlySpendingSerializer(record)
    return Response(serializer.data)
