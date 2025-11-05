from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Orders, OrderDetails, Employee

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                product_name=form.cleaned_data['product_name'],
                unit_price=form.cleaned_data['unit_price'],
                discounted=form.cleaned_data.get('discounted', False),
                image=form.cleaned_data.get('image')
            )
            messages.success(request, 'Mahsulot muvaffaqiyatli qoshildi')
            return redirect('add_product')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            Orders.objects.create(
                order_date=form.cleaned_data['order_date'],
                required_date=form.cleaned_data['required_date'],
                shipped_date=form.cleaned_data.get('shipped_date')
            )
            messages.success(request, 'Buyurtma muvaffaqiyatli qoshildi!')
            return redirect('add_order')
    else:
        form = OrdersForm()

    return render(request, 'add_order.html', {'form': form})

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def add_orderdetails(request):
    if request.method == 'POST':
        form = OrderDetailsForm(request.POST)
        if form.is_valid():
            OrderDetails.objects.create(
                order=form.cleaned_data['order'],
                product=form.cleaned_data['product'],
                unit_price=form.cleaned_data['unit_price'],
                quantity=form.cleaned_data['quantity'],
                discounted=form.cleaned_data['discounted'],
            )
            messages.success(request, "OrderDetails muvaffaqiyatli qo‘shildi!")
            return redirect('add_orderdetail')
    else:
        form = OrderDetailsForm()

    return render(request, 'add_orderdetails.html', {'form': form})

def orderdetails_list(request):
    orderdetails = OrderDetails.objects.all()
    return render(request, 'orderdetails_list.html', {'orderdetails': orderdetails})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            Employee.objects.create(
                employee_id=form.cleaned_data['employee_id'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
            )
            messages.success(request, "Xodim muvaffaqiyatli qo‘shildi!")
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def delete_product(request):
    product=get_object_or_404(Product,id=pk)
    product.delete()
    messages.success(request,"mahsulot qoshildi")
    return redirect('product_list')

def delete_order(request):
    order=get_object_or_404(Orders,id=pk)
    order.delete()
    messages.success(request,"order qoshildi")
    return redirect('order_list')

def delete_orderdetails(request):
    orderdetails=get_object_or_404(OrderDetails,id=pk)
    orderdetails.delete()
    messages.success(request,"OrderDetails qoshildi")
    return redirect('orderdetails_list')

def delete_employee(request):
    employee=get_object_or_404(Employee,id=pk)
    employee.delete()
    messages.success(request,"Employee qoshildi")
    return redirect('employee_list')

def update_product(request,pk):
    product=get_object_or_404(Product,id=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,"Product qoshildi")
            return redirect('product_list')
    else:
        form=ProductForm(instance=product)
    context = {
        'form': form,
        'product': product,
    }
    return render(request,'update_product.html',context)

def update_order(request,pk):
    order=get_object_or_404(Orders,id=pk)
    if request.method=='POST':
        form=OrdersForm(request.POST,request.FILES, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,"Order qoshildi")
            return redirect('order_list')
    else:
        form=OrdersForm(instance=order)

    return render(request, 'update_order.html', {'form': form, 'order': order})

def update_orderdetails(request,pk):
    orderdetails=get_object_or_404(OrderDetails,id=pk)
    if request.method=='POST':
        form=OrderDetailsForm(request.POST,request.FILES, instance=orderdetails)
        if form.is_valid():
            form.save()
            messages.success(request,"OrderDetails qoshildi")
            return redirect('orderdetails_list')
    else:
        form=OrderDetailsForm(instance=orderdetails)
    return render(request, 'update_orderdetails.html', {'form': form, 'order': orderdetails})

def update_employee(request,pk):
    employee=get_object_or_404(Employee,id=pk)
    if request.method=='POST':
        form=EmployeeForm(request.POST,request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee qoshildi")
            return redirect('employee_list')
    else:
        form=EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form, 'employee': employee})
