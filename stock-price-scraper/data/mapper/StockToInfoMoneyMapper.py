from data.model.StockInfoMoney import StockInfoMoney
from domain.model.Stock import Stock

def map_stock_to_info_money(company: Stock) -> StockInfoMoney:
    if company == Stock.VALE:
        return StockInfoMoney.VALE
    elif company == Stock.BANCO_DO_BRASIL:
        return StockInfoMoney.BANCO_DO_BRASIL