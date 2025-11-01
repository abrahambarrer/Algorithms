total_litres = int(input())
litres_per_badge = int(input())
money_per_badge = int(input())

money_bage = (total_litres // litres_per_badge) * money_per_badge
leftover = total_litres % litres_per_badge

print(money_bage + leftover)