def index_by_date(prices):
    pass


def align_series(instrument_prices, benchmark_prices):
    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)

    common_dates = sorted(
        set(instrument_by_date)
        & set(benchmark_by_date)
    )

    aligned_instrument = [
        instrument_by_date[date]
        for date in common_dates
    ]

    aligned_benchmark = [
        benchmark_by_date[date]
        for date in common_dates
    ]

    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):
    first_close = prices[0]["close"]
    last_close = prices[-1]["close"]

    return (last_close / first_close - 1) * 100
    


def calculate_period_return(prices):
    pass


def calculate_relative_performance(instrument_return, benchmark_return):
    pass


def calculate_base_100(prices):
    pass