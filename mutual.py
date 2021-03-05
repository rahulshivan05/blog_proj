from mftool import Mftool
# print(dir(Mftool))
obj = Mftool()
# print(obj)

data = obj.get_scheme_quote('119551')
# print(data)
data2 = obj.get_scheme_details("119551")
# print(data2)

# data3 = mf.get_scheme_historical_nav('119551') 
# print(data3)

# data['fund_house']
# print(data['data'])

data4 = obj.get_scheme_codes()
# print(data4)


data5 = obj.get_open_ended_equity_scheme_performance(True) 
# print(data5)

value = obj.get_open_ended_debt_scheme_performance(True) 
# print(value)

data6 = obj.get_all_amc_profiles(True) 
print(data6)