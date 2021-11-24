bills = float(input())
bills_adjusted = int(bills * 100)  # this is how you adjust it. Not by doing int(bills) * 100. That ain't gonna work
coins_counter = 0

coins_counter += bills_adjusted//200
bills_adjusted = bills_adjusted % 200

coins_counter += bills_adjusted//100
bills_adjusted = bills_adjusted % 100

coins_counter += bills_adjusted//50
bills_adjusted = bills_adjusted % 50

coins_counter += bills_adjusted//20
bills_adjusted = bills_adjusted % 20

coins_counter += bills_adjusted//10
bills_adjusted = bills_adjusted % 10

coins_counter += bills_adjusted//5
bills_adjusted = bills_adjusted % 5

coins_counter += bills_adjusted//2
bills_adjusted = bills_adjusted % 2

coins_counter += bills_adjusted//1
bills_adjusted = bills_adjusted % 1
print(coins_counter)


#Yes, but I could not have done it on my own w/o losing hours. Judge approved