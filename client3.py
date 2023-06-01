################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    if quote is None:
        return None, None, None, None
    stock = quote.get('stock')
    bid_price = quote.get('top_bid', {}).get('price')
    ask_price = quote.get('top_ask', {}).get('price')
    if stock is None or bid_price is None or ask_price is None:
        return None, None, None, None
    price = (float(bid_price) + float(ask_price)) / 2
    return stock, bid_price, ask_price, price





def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    if price_b != 0:
        return price_a / price_b
    return 1


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in range(N):
        try:
            quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        except Exception as e:
            print("Error retrieving quotes:", e)
            continue

        """ ----------- Update to get the ratio --------------- """
        prices = {}  # Dictionary to store stock prices
        for quote in quotes:
            if quote is None:
                continue
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store the price for each stock
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        if 'ABC' in prices and 'DEF' in prices:
            ratio = getRatio(prices['ABC'], prices['DEF'])  # Compute the ratio of stock prices
            print("Ratio %s" % ratio)
        else:
            print("Error: Missing stock prices")

