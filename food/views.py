from django.shortcuts import render
from .services import PricingService

def my_view(request):
    print(request)
    if request.method == 'POST':
        zone = request.POST.get('zone')
        organization_id = request.POST.get('organization_id')
        total_distance = request.POST.get('total_distance')
        item_type = request.POST.get('item_type')
        total_price = PricingService.calculate_price(zone, organization_id, total_distance, item_type)
        if total_price != None:
            total_price *= 100
            total_price = int(total_price)
        print("Total Price", total_price)
        return render(request, 'output1.html', {'total_price': total_price})
    else:
        return render(request, 'input1.html')
