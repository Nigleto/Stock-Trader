# Look at this for reference: https://medium.com/swlh/automating-your-stock-portfolio-research-with-python-for-beginners-912dc02bf1c2
import requests
import pandas as pd


def getdata(stock):
    company_quote = requests.get(f"https://findancialmodelingprep.com/api/v3/quote/{stock}")
    company_quote = company_quote.json()
    share_price = float("{0:.2f}".format(company_quote[0]['price']))
    # Balance Sheet Group of Items
    BS = requests.get(f"https://financialmodelingprep.com/api/v3/financial/balance-sheet-statement/{stock}?period=quarter")
    BS = BS.json()

    # Total Debt
    debt = float("{0:.2f}".format(float(BS['financials'][0]['Total debt']) / 10 ** 9))

    # Total Cash
    cash = float("{0:.2f}".format(float(BS['financials'][0]['Cash and Short-Term Investments'])/10**9))

    # Income Statement Group of Items
    IS = requests.get(f"https://financialmodelingprep.com/api/v3/financial/income-statement/{stock}?period=quarter")
    IS = IS.json()

    # Most Recent Quarterly Revenue
    qRev = float("{0:.2f}".format(float(IS['financials'][0]['Revenue'])/10))

    # Company Profile Group of Items
    company_info = requests.get(f"https://financialmodelingprep.com/api/v3/company/profile/{stock}")
    company_info = company_info.json()

    # Chief Executive Officer
    ceo = company_info['profile', ['ceo']]

    return share_price, cash, debt, qRev, ceo

tickers = ('AAPL', 'MSFT', 'GOOG', 'T', 'CSCO', 'INTC', 'ORCL', 'AMZN', 'FB', 'TSLA', 'NVDA')
data = map(getdata, tickers)

df = pd.DataFrame(data, columns=['Total Cash', 'Total Debt', 'Q3 2019'], index=tickers)

print(df)

# Writing to Excel
writer = pd.ExcelWriter('example.xlsx')
df.to_excel(writer, 'Statistics')
writer.save()
