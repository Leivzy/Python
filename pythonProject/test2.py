name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth = 1.2
growth_days = 7
print(f"公司:{name},股票代码{stock_code},当前股价:{stock_price}")
print(f"每日增长系数是:{stock_price_daily_growth},经过{growth_days}天的增长后,股价达到了:{stock_price * stock_price_daily_growth ** growth_days:.2f}")