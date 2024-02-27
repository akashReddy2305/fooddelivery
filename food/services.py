from .models import Pricing
import decimal
class PricingService:
    @staticmethod
    def calculate_price(zone, organization_id, total_distance, item_type):
        pricing = Pricing.objects.filter(
            organization_id=organization_id,
            item_id=item_type,
            zone=zone
        ).first()
        print(Pricing.objects.all())
        if not pricing:
            return None
        base_price = pricing.fix_price
        total_distance = decimal.Decimal(total_distance)
        if total_distance > pricing.base_distance_in_km:
            additional_distance = total_distance - pricing.base_distance_in_km
            base_price += additional_distance * pricing.km_price

        return base_price