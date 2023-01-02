import requests


api_key = 'your api key'

company = ['RJF', 'WY', 'AVB']

years = 5

for ticker in company:

    income_statement = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={years}&datatype=csv&apikey={api_key}')

    with open(f'{ticker}_income_statement.csv', 'wb') as f:
        f.write(income_statement.content)

    balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit={years}&datatype=csv&apikey={api_key}')

    with open(f'{ticker}_balance_sheet.csv', 'wb') as f:
        f.write(balance_sheet.content)

    cash_flow = requests.get(f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit={years}&datatype=csv&apikey={api_key}')

    with open(f'{ticker}_cash_flow.csv', 'wb') as f:
        f.write(cash_flow.content)

    enterprise_value = requests.get(f'https://financialmodelingprep.com/api/v3/enterprise-value/{ticker}?limit={years}&datatype=csv&apikey={api_key}')

    with open(f'{ticker}_enterprise_value.csv', 'wb') as f:
        f.write(cash_flow.content)



