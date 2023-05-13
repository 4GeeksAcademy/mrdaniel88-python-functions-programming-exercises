def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######
result_dollar_to_euro = dollar_to_euro(137)
result_euro_to_yen = euro_to_yen(result_dollar_to_euro)

print(result_euro_to_yen)