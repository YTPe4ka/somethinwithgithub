from django import forms
from .models import Product, Orders, OrderDetails, Employee


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'unit_price', 'discounted']
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mahsulot nomini kiriting'
            }),
            'unit_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Narxni kiriting'
            }),
            'discounted': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Chegirma foizini kiriting'
            }),
        }


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['order_date', 'required_date', 'shipped_date']
        widgets = {
            'order_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'required_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'shipped_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['order', 'product', 'unit_price', 'quantity', 'discounted']
        widgets = {
            'order': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'discounted': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'address', 'city']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }
