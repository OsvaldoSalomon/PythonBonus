import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
result = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string)
print(result)
print(['STOX ', 'STOXX '])
result = re.findall(r"([A-Z]{5})\s(?=[0-9]{3})", string)
print(result)
print(['STOXX', 'STOXX'])
result = re.findall(r"Euro(?=[a-z]+)", string)
print(result)
print(['Euro'])