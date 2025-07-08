# expense/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Category
    path('categories/', views.category_list_create, name='category-list-create'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),

    # Expense
    path('expenses/', views.expense_list_create, name='expense-list-create'),
    path('expenses/<int:pk>/', views.expense_detail, name='expense-detail'),

    # Budget Limit
    path('budget-limits/', views.budget_list_create, name='budget-limit-list-create'),
    path('budget-limits/<int:pk>/', views.budget_detail, name='budget-limit-detail'),

    # Alerts
    path('alerts/', views.alert_list, name='alert-list'),
    path('alerts/<int:pk>/', views.alert_detail, name='alert-detail'),

    # Monthly Spending
    path('spending/', views.spending_list, name='spending-list'),
    path('spending/<int:pk>/', views.spending_detail, name='spending-detail'),
]
