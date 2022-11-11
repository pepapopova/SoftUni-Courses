bitcoin_to_lev = 1168
uan_to_to_dollar = 0.15
dollar_to_lev = 1.76
euro_to_lev = 1.95

number_bitcoin = float(input())
uan_amount = float(input())
commission = float(input())

bitcoins_eur = number_bitcoin * bitcoin_to_lev / euro_to_lev
uan_eur = uan_amount * uan_to_to_dollar * dollar_to_lev / euro_to_lev
total_money = bitcoins_eur + uan_eur
total_money = (100 - commission) / 100 * total_money
print(f"{total_money:.2f}")