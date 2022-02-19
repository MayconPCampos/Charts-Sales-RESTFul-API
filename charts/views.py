from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.models import User


def index(request, username):

    user_account = User.objects.get(username=username)

    # informações sobre total de numeros e valores de vendas
    sales = user_account.sales.all().order_by("date")
    number_of_sales = len(sales)
    prices = [float(sale.price) for sale in sales]
    total_price_values = sum(prices)
    
    # informações das vendas semanais
    week_sales_sum = user_account.sales.all().values('date').annotate(Sum('price'))
    week_days = [str(sale.get("date")) for sale in week_sales_sum]
    week_prices = [float(sale.get("price__sum")) for sale in week_sales_sum]
    
    # Vendas agrupadas por tipos produtos
    sale_products_sum = user_account.sales.all().values('product').annotate(Sum('price'))
    products = [sale.get("product") for sale in sale_products_sum]
    product_values = [float(sale.get("price__sum")) for sale in sale_products_sum]

    # vendas agrupadas por tipos de clientes
    client_sales = user_account.sales.all().values('client').annotate(Sum('price'))
    clients = [str(sale.get("client")) for sale in client_sales]
    client_values = [float(sale.get("price__sum")) for sale in client_sales]

    context = {
        "sales": sales,
        "number_of_sales": number_of_sales,
        "dates": week_days,
        "week_prices": week_prices,
        "total_price_values": total_price_values,
        "products": products,
        "product_values": product_values,
        "clients": clients,
        "client_values": client_values,
        "user_account": user_account
    }
    return render(request, "charts/index.html", context)
