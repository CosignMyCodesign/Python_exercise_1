stockDict = {
  'CK': 'Coke',
  'MT': 'Mattress Firm',
  'DS': 'Death Star'
}


purchases = [
  ('CK', 250, '11-sep-2001', 50),
  ('MT', 400, '4-dec-1978', 40),
  ('DS', 24, '31-dec-1999', 32)
]


report = {}
for purchase in purchases:
  abbrev = purchase[0]
  full_name = stockDict[abbrev]
  no_of_shares = purchase[1]
  purchase_date = purchase[2]
  purchase_price = purchase[3]
  full_purchase_price = no_of_shares * purchase_price
  print(f"I purchased {full_name} stock on {purchase_date} for {full_purchase_price}")

  try:
    report[abbrev].append(purchase)
  except KeyError:
    report[abbrev] = list()
    report[abbrev].append(purchase)

for abbrev, purchases_list in report.items():
  print(f"------{abbrev}------")
  total_portfolio_stock_value = 0
  for purchase in purchases_list:
    total_portfolio_stock_value += purchase[1] * purchase[3]
    print(f"     {purchase}")
  print(f"Total value of stock in portfolio: ${total_portfolio_stock_value}\n\n")



