from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

X =  float(input())
print(Decimal(str(X)).quantize(Decimal('0'), ROUND_HALF_UP))

