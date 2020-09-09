from rest_framework import viewsets
from .serializers import ExpenseSerializer
from .models import Expense


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('created_at')
    serializer_class = ExpenseSerializer
