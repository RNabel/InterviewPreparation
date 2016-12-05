import collections
import sys

# PARAMETERS.
INSIDER_CUTOFF_PROFIT = 5000000
DAY_CUTOFF = 3

# GLOBALS.
# ========
# Maps name to set of inside trader names.
inside_traders = collections.defaultdict(set)
current_stock_price = -1
trades = []


def evict_old_dates(new_day):
    global trades

    num_evicted = 0

    # Undo all trades that lie more than 3 days in the past.
    for el in trades:
        day, name, diff = el  # Destructure tuple.

        # Undo all trades that lie more than 3 days behind the current day.
        if day >= new_day - DAY_CUTOFF:
            break
        else:
            num_evicted += 1

    # Delete all evicted trades.
    if num_evicted:
        # Remove out-of-range trades and inside trader entries.
        trades = trades[num_evicted:]


def process_new_line(line):
    trade = get_details(line)
    day = trade[0]
    price = trade[]
    trades.append(trade)


def process_new_stock_price(line):
    global current_stock_price
    day, new_price = line.split("|")
    day, new_price = int(day), int(new_price)

    evict_old_dates(day)

    # Insert new stock price.
    current_stock_price = new_price

    # Check if any transaction in last 3 days exceeded 5M.
    for trade in trades:
        day, name, amount, is_buy = trade

        if is_buy and current_stock_price >= amount:
            inside_traders[day].add(name)
        elif not is_buy and current_stock_price <= amount:
            inside_traders[day].add(name)


# HELPERS.
# ========
def get_details(line):
    elements = line.split("|")
    day = int(elements[0])
    name = elements[1]
    is_buy = elements[2] == "BUY"
    amount = int(elements[3])

    price_diff = 5000000 / amount

    if is_buy:
        new_price = current_stock_price + price_diff
    else:
        new_price = current_stock_price - price_diff

    return day, name, new_price, is_buy


def output_results():
    sorted_keys = sorted(inside_traders.keys())

    for day in sorted_keys:
        names = sorted(inside_traders[day])
        for name in names:
            yield "{day}|{name}".format(day=day, name=name)


def findPotentialInsiderTraders(datafeed):
    num_of_lines = datafeed[0]

    for line in datafeed[1:]:
        is_stock = line.count("|") == 1
        if is_stock:
            process_new_stock_price(line)
        else:
            process_new_line(line)
    # Print remaining inside traders.
    return output_results()
