# retailer_ex_rate=float(input('ENTER EX RATE:'))
# pp_ex_rate = float(input('ENTER PP EX RATE:'))
# local_bank_rate=float(input('ENTER AMOUNT:'))
 
 
class calculator:
 
   def __init__(self,ebay_fees,pp_fees,pp_flat_fee,all_fees,profit_usd):
       self.ebay_fees=ebay_fees
       self.pp_fees=pp_fees
       self.pp_flat_fee=pp_flat_fee
       self.all_fees=all_fees
       self.profit_usd=profit_usd
 
 
sell_p=float(input('ENTER SELLING PRICE:'))
source_p=float(input('ENTER SOURCE PRICE:'))
promo_fees=float(input('ENTER PROMOTION RATE:'))
 
 
ebay_fees=float(0.1)
 
pp_fees=float(0.044)
 
pp_flat_fee=float(0.3)
 
all_fees = sell_p*(ebay_fees+pp_fees)+pp_flat_fee + promo_fees
 
profit_usd = sell_p-all_fees-source_p
 
 
calc_usd=calculator(ebay_fees,pp_fees,pp_flat_fee,all_fees,profit_usd)
 
print(calc_usd.profit_usd)
 
 
 
class currency_calc(calculator):
   def __init__(self,retailer_ex_rate,pp_ex_rate,local_bank_rate,local_bank_fees,profit_currency):
       super().__init__(ebay_fees,pp_fees,pp_flat_fee,all_fees,profit_usd)
       self.retailer_ex_rate=retailer_ex_rate
       self.pp_ex_rate=pp_ex_rate
       self.local_bank_rate=local_bank_rate
       self.local_bank_fees=local_bank_rate
       self.profit_currency=profit_currency
 
 
 
 
 
retailer_ex_rate=float(input('ENTER EX RATE:'))
pp_ex_rate = float(input('ENTER PP EX RATE:'))
local_bank_rate=float(input('ENTER AMOUNT:'))
local_bank_fees=float(source_p*retailer_ex_rate)*float(local_bank_rate)
 
profit_currency= float((sell_p-all_fees)*pp_ex_rate)-float((source_p*retailer_ex_rate)-local_bank_fees)
 
calc_currency=currency_calc(retailer_ex_rate,pp_ex_rate,local_bank_rate,local_bank_fees,profit_currency)