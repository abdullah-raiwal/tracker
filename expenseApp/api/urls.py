from django.urls import path, include
from expenseApp.api import views

urlpatterns = [
    path('add-expense/', views.CreateExpenseView.as_view(), name='create-expense'),
    path('list/', views.ListExpenseView.as_view(), name='expense-list'),
    path('list/<int:pk>', views.DetailExpenseView.as_view(), name='expense-detail')
]