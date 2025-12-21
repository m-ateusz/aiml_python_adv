class PriceCalculator:

   def final_price(self, base: float, discount_type: str) -> float:
       if discount_type == "none":
           return base
       elif discount_type == "student":
           return base * 0.9
       elif discount_type == "black_friday":
           return base * 0.7
       elif discount_type == "xmas":
           return base * 0.8
       raise ValueError("Unknown discount")

print(f'{PriceCalculator().final_price(100.0, 'xmas') = }')