# Encephalo Investments Coding Pre-Test - main.py
import pandas as pd


def main():
    # main function.
    # Return the top 10 companies with the highest market cap.
    df = pd.read_csv(r"C:\Users\Lenovo\Desktop\data.csv")#, column =['ticker', 'industry', 'market_cap']) # read csv using pandas
    print(df)
    a=0
    b=0
    c=0
    a=float(a)
    b=float(b)
    b=float(c)
    print(len(df))
    #df.market_cap.apply(type)
    for i in range(len(df)):
        if isinstance(df.iloc[i,2] , str):
            df.iloc[i,2] = df.iloc[i,2].replace("$","")
            if "B" in df.iloc[i,2]:
                print(df.iloc[i,2])
                df.iloc[i,2] = df.iloc[i,2].replace("B","")
                df.iloc[i,2]=float(df.iloc[i,2])
                if df.iloc[i,2] >a:
                    c=b
                    b=a
                    a=i
                    
                elif df.iloc[i,2]> b:
                    c=b
                    b=i
                elif df.iloc[i,2]> c:
                    c= i

    print("1st largest")
    print(df.loc[a,:])
    print("--------------------")
    print("2nd largest")
    print(df.loc[b,:])
    print("--------------------")
    print("3rd largest")
    print(df.loc[c,:])
        
        

if __name__ == "__main__":
    main()