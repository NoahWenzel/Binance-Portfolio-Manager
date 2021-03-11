import Portfolio
import Functions

# Adjustable variables
how_long = 577
timeframe = 'hour'

# Get desired portfolio
portfolio = Portfolio.Portfolio()

# Fill historical price data
for i in range(len(portfolio)):
    portfolio[i][1] = Functions.get_prices(how_long, timeframe, str(portfolio[i][0] + 'USD'))

    # This can be uncommented for troubleshooting. Sometimes a particular coin will not have as much data
    # so here you can see how much was gotten for each coin.

    print('Symbol: ' + str(portfolio[i][0] + 'USD'))
    print('How far back received: ' + str(len(portfolio[i][1])))
    print()

# Now add all the coin values in the portfolio to measure the total value of the portfolio over time.
total_portfolio = []
timeframe_total = 0

for y in range(how_long):
    # Get the timeframe's total
    for x in range(len(portfolio)):
        timeframe_total = timeframe_total + (portfolio[x][1][y] * portfolio[x][2])
    # Add timeframe_total to total_portfolio
    total_portfolio.append(timeframe_total)
    # Clear timeframe_total for next datapoint calculation
    timeframe_total = 0

# Graph portfolio in detail
Functions.graph_list(total_portfolio, "Total Portfolio")

for i in range(len(portfolio)):
    Functions.graph_list(portfolio[i][1], portfolio[i][0] + 'USD')
