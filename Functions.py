from binance.client import Client
import matplotlib.pyplot as plt
import Key

client = Client(api_key=Key.key, api_secret=Key.secret_key, tld='us')


def get_prices(how_many, timeframe, symbol):
    """ Get's historical prices how_many timeframe back for which symbol.
    Ex: 24 hours back for BTCUSDT
    :param how_many: How long you want to go back with the timeframe
    :param timeframe: options are hour, minute, day
    :param symbol: Crypto pair Ex: BTCUSDT
    :return: List of historical data
    """

    how_many = str(how_many)
    time_ago = how_many + ' ' + timeframe + 's ago UTC'
    if timeframe == 'day':
        timeframe = '1d'
    elif timeframe == 'hour':
        timeframe = '1h'
    elif timeframe == 'minute':
        timeframe = '1m'
    else:
        raise Exception('Timeframe \'' + timeframe + '\' is not valid!')

    # Get the klines over the specified time period and length
    klines = client.get_historical_klines(symbol, timeframe, time_ago)

    # Clean up the data so we just have the closing price from the klines
    price_list = []
    # Assign the kline close values to an array fo current prices
    for i in range(len(klines)):
        price_list.append(float(klines[i][4]))

    return price_list


def graph_list(list, name):
    """ Graphs the provided list as the y values and the index of the list as the x values.
    The title of the graph is the name provided
    :param list: The data to be graphed
    :param name: The name of the graph
    :return: A graph of the list
    """
    x = []
    for i in range(len(list)):
        x.append(i)

    y = list

    plt.plot(x, y)
    plt.title(label=name)
    plt.show()
