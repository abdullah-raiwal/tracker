from django.shortcuts import render
from expenseApp.api.serializers import ExpenseSerializer
from rest_framework import generics
from rest_framework.views import APIView
from expenseApp.models import Expense
from rest_framework.response import Response

class CreateExpenseView(generics.CreateAPIView):

   serializer_class = ExpenseSerializer
   
   queryset = Expense.objects.all()

class ListExpenseView(generics.ListAPIView):
   serializer_class = ExpenseSerializer

   def get_queryset(self):
    user = self.request.user
    if user.is_anonymous:
        return None
    return Expense.objects.filter(user=user.id)

class DetailExpenseView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = ExpenseSerializer
   queryset = Expense.objects.all()
   

