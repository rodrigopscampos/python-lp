#Infinitamente, some os valores digitados e imprima a média

n = 0
c = 0

while True:
    n = n + int(input("Informe um número: "))
    c = c + 1

    print("Soma: " + str(n) + " Quantidade: " + str(c) +  " Média: " + "{:.2f}".format(n / c))


'''
Number	Format	Output	Description
3.1415926	{:.2f}	3.14	2 decimal places
3.1415926	{:+.2f}	+3.14	2 decimal places with sign
-1	{:+.2f}	-1.00	2 decimal places with sign
2.71828	{:.0f}	3	No decimal places
5	{:0>2d}	05	Pad number with zeros (left padding, width 2)
5	{:x<4d}	5xxx	Pad number with x’s (right padding, width 4)
10	{:x<4d}	10xx	Pad number with x’s (right padding, width 4)
1000000	{:,}	1,000,000	Number format with comma separator
0.25	{:.2%}	25.00%	Format percentage
1000000000	{:.2e}	1.00e+09	Exponent notation
13	{:10d}	        13	Right aligned (default, width 10)
13	{:<10d}	13	Left aligned (width 10)
13	{:^10d}	    13	Center aligned (width 10)
'''