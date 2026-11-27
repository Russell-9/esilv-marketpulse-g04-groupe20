def index_by_date(prices):
    return {
        row["date"]: row
        for row in prices
    }

def align_series(instrument_prices, benchmark_prices):
    pass


def calculate_period_return(prices):
    pass


def calculate_relative_performance(instrument_return, benchmark_return):
    pass


def calculate_base_100(prices):
    pass