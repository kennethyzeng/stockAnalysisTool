#1 output stock sympboll in set format after reading stocklist.txt 
def read_stocklist_to_set(filename="stocklist.txt"):
    stock_list_set = set()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            # Split by comma and strip each item
            items = [item.strip() for item in line.split(",") if item.strip()]
            stock_list_set.update(items)
    return stock_list_set


#2 Single Stock Excel File Initialization Parameter Setup
single_stock_excel_sheet_titles=["Summary","PriceData","Analysis", "Finance_Analysis"]
#2a for finance analysis worksheet
single_stock_excel_finance_analysis_parameters_dicts={
    #parameters to set related columns
    "column_dimensions": [('A',27), ('C', 27),('E', 27),('G', 27), ('I', 27)],
    
    #parameters to set each cell
    "A1":["#1 Moving Average Analysis Section", "FFFF00"], #yellow

    "A2":["Current_Price", "ADD8E6"], #light blue
    "C2":["5_Days_Average_Price", "ADD8E6"], 
    "E2":["10_Days_Average_Price", "ADD8E6"], 
    "G2":["20_Days_Average_Price", "ADD8E6"], 
    "I2":["30_Days_Average_Price", "ADD8E6"], 

    "A3":["Current_Volumn", "ADD8E6"], 
    "C3":["5_Days_Average_Volumn", "ADD8E6"], 
    "E3":["10_Days_Average_Volumn", "ADD8E6"], 
    "G3":["20_Days_Average_Volumn", "ADD8E6"], 
    "I3":["30_Days_Average_Volumn", "ADD8E6"], 

    "C5":["Above_5_Days_Average_Price?", "ADD8E6"], 
    "E5":["Above_10_Days_Average_Price?", "ADD8E6"], 
    "G5":["Above_20_Days_Average_Price?", "ADD8E6"], 
    "I5":["Above_30_Days_Average_Price?", "ADD8E6"], 
    "K5":["Above_60_Days_Average_Price?", "ADD8E6"], 

    "C6":["By Percentage", "ADD8E6"], 
    "E6":["By Percentage", "ADD8E6"],
    "G6":["By Percentage", "ADD8E6"], 
    "I6":["By Percentage", "ADD8E6"], 
    "K6":["By Percentage", "ADD8E6"], 

    "C7":["Above_5_Days_Average_Volumn?", "ADD8E6"], 
    "E7":["Above_10_Days_Average_Volumn?", "ADD8E6"],
    "G7":["Above_20_Days_Average_Volumn?", "ADD8E6"], 
    "I7":["Above_30_Days_Average_Volumn?", "ADD8E6"], 
    "K7":["Above_60_Days_Average_Volumn?", "ADD8E6"], 

    "C8":["By Percentage", "ADD8E6"], 
    "E8":["By Percentage", "ADD8E6"],
    "G8":["By Percentage", "ADD8E6"], 
    "I8":["By Percentage", "ADD8E6"], 
    "K8":["By Percentage", "ADD8E6"], 

    "A10":["5_Days_Average_Price_above_10_days?", "ADD8E6"], 
    "C10":["10_Days_Average_Price_above_20_days?", "ADD8E6"], 
    "E10":["20_Days_Average_Price_above_30_days?", "ADD8E6"], 
    "G10":["5_Days >10_Days>20_Days?", "ADD8E6"], 
   
    "A12":["Received Value/Total Value(by %):", "ADD8E6"], 
    "C12":["Received Value:", "ADD8E6"], 
    "E12":["Total Estimated Value:", "ADD8E6"], 
    "F12":[ 8, "ADD8E6"], 
}
