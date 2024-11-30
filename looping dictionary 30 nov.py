transaction_data ={
    "ID" : 1,
    "Source_Country" : "United Kingdom",
    "Target_Country" : "Indonesia",
    "Currency" : "GBP",
    "amount" : 1000.00,
    "Target_Currency" : "Yen",
    "fx_rate" : "199775,2",
    "Platform" : "Mobile"
}
print(transaction_data)
print()
for key in transaction_data:
    print(key,":",transaction_data[key])