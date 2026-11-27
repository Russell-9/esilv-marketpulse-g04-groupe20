def index_by_date(prices):
    pass


def align_series(instrument_prices, benchmark_prices):
    pass


def calculate_period_return(prices):
    pass


def calculate_relative_performance(instrument_return, benchmark_return):
     return instrument_return - benchmark_return


def calculate_base_100(prices):
    first_close = prices[0].["close"]
    result = []

    for row in prices:
        result.append({
            "date": row["date"],
            "ticker": row["ticker"],
            "value": row["close"] / first_close * 100,
        })
    
    return result