import data_prep as dp
import pandas as pd


def main():
    
    # Initialise portfolio_choice variable
    portfolio_choice = ""
    while portfolio_choice not in [1, 2]:
        try:
            portfolio_choice = int(input(         
                "To analyse an existing portfolio, type 1\n"
                "To analyse a hypothetical portfolio - type 2\n"
            )
                                  )
        except Exception:
            print('Error: Invalid Choice.\n')

    # Get portfolio data from user depending on choice:
    if portfolio_choice == 1:
        existing_portfolio = dp.get_existing_portfolio()
        ticker_list = []
        for key, value in existing_portfolio.items():
            ticker_list.append(key)
        ticker_list = pd.DataFrame(columns=ticker_list).add_suffix('-USD').columns.tolist()
    elif portfolio_choice == 2:
        ticker_list = dp.get_hypothetical_portfolio()
        # Request investment amount from user
        investment_amount = dp.get_investment_amt()

    # Fetch data from yfinance for each ticker, and create pandas dataframe
    portfolio_df = dp.get_ticker_data(ticker_list)
    portfolio_df.dropna(inplace = True)

    # Print portfolio data for visual confirmation
    if portfolio_choice == 1: 
        print(f"--------------------------")                      
        print(f"Existing Portfolio:")
        total_value = int()
        for ticker, units in existing_portfolio.items():
            value = portfolio_df[f"{ticker}-USD"].iloc[-1, 3] * units
            print(f"Value of {units} {ticker}: ${value:.2f} ")
            total_value += value
        print(f"\nTotal portfolio value: ${total_value:.2f}\n")        
        print(f"--------------------------")
    elif portfolio_choice == 2:
        print(f"--------------------------")                      
        print(f"Hypothetical Portfolio:")
        print(f"{[ticker.replace('-USD', '') for ticker in ticker_list]}")                   
        print(f"Investment amount:")
        print(f"${investment_amount:.2f}")
        print(f"--------------------------")

if __name__ == '__main__':
    main()
    