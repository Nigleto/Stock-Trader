import json
from urllib.request import urlopen

# TODO: make sure it checks if the input is really a stock
# TODO: make it print 'come again' every time the user doesn't have a valid answer
# TODO: make sure it prints only one of the lines instead of 3 and make sure it only prints price and not the other
#  things
# TODO: add a dictionary with all valid stocks, check input against the dictionary to see if real
# TODO:
# ctrl shift alt j

profile_url = "https://financialmodelingprep.com/api/v3/profile/TSLA?apikey=9e32e1c117e9206264ef7c63453dca84"
quote_url = "https://financialmodelingprep.com/api/v3/quote/TSLA?apikey=9e32e1c117e9206264ef7c63453dca84"


def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


def welcome():
    print('Welcome to the retracement tool.')
    banana = input('What are you going to do? (ex: Stock or Crypto)\n')
    while banana != 'Stock' and banana != 'Crypto':
        banana = input('Come Again?')
    print('Good choice.')


def getRightPunctuation(my_choice, my_stock):
    global quote_url
    quote_url = "https://financialmodelingprep.com/api/v3/quote/TSLA?apikey=9e32e1c117e9206264ef7c63453dca84"
    quote_url = quote_url.replace('TSLA', my_stock)
    if my_choice in ('price', 'Price'):
        my_choice = 'price'
        quote_url = quote_url.replace('quote', 'profile')
    if my_choice in ('CEO', 'ceo', 'Ceo'):
        my_choice = 'ceo'
        quote_url = quote_url.replace('quote', 'profile')
    if my_choice in ('employees', 'Employees'):
        my_choice = 'fullTimeEmployees'
        quote_url = quote_url.replace('quote', 'profile')
    if my_choice in ('grossprofit', 'GrossProfit', 'grossProfit', 'Grossprofit'):
        my_choice = 'grossProfit'
        quote_url = quote_url.replace('quote', 'income-statement')
    elif my_choice in ('daylow', 'DayLow', 'Daylow'):
        my_choice = 'dayLow'
    elif my_choice in ('DayHigh', 'dayhigh', 'dayHigh'):
        my_choice = 'dayHigh'
    #else:
    #    print('invalid input')
    #    exit
    return my_choice




def getSomething(my_choice, my_stock):
    my_choice = getRightPunctuation(my_choice, my_stock)
    my_data2 = get_jsonparsed_data(quote_url)[0]
    print(my_data2)
    print(my_choice)
    high = my_data2.get(my_choice)
    print(my_choice, ": ", high)


def getStock():
    my_stock = input("What stock would you like? ('end' to finish)\n")
    return my_stock


def getChoice():
    my_choice = input('What would you like to look at from that stock? (ex: Price, DayHigh, DayLow, etc)\n')
    return my_choice


def keepStock():
    global my_stock
    change_this_stock = input("Change stock (yes,no,end)?\n")
    if change_this_stock == 'yes':
        my_stock = getStock()
    elif change_this_stock == 'end':
        exit()
    if change_this_stock != 'yes' or change_this_stock != 'no' or change_this_stock != 'end':
        print('\n invalid input')
        keepStock()
        #FIX THIS PART ASAP!
    return my_stock


welcome()

my_stock = getStock()

stock_list_url = "https://financialmodelingprep.com/api/v3/stock/list?apikey=9e32e1c117e9206264ef7c63453dca84"
# my_data = get_jsonparsed_data(stock_list_url)
# print("My data:", my_data)

while my_stock != 'end':
    my_choice = getChoice()
    getSomething(my_choice, my_stock)
    my_stock = keepStock()
