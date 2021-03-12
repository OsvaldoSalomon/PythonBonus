import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result = re.findall(r"\d(?![5-9]|\D)", string)
print(result)
print(['6', '0', '1', '6', '0'])
result = re.findall(r"\b\w+\b(?!\s)", string)
print(result)
print(['index', 'FTSE', '11', '48', '1998', '2', 'all', 'February'])