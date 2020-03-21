# Encephalo Investments Coding Pre-Test - main.py
import pandas as pd


def main():
    # main function.
    # Return the top 10 companies with the highest market cap.
    df = pd.read_csv(r"C:\Users\Lenovo\Desktop\data.csv")#, column =['ticker', 'industry', 'market_cap']) # read csv using pandas
    #print(df)
    dict={}
    list1=[]
    #print(len(df))
    #df.market_cap.apply(type)
    for i in range(len(df)):
        if isinstance(df.iloc[i,2] , str):
            df.iloc[i,2] = df.iloc[i,2].replace("$","")
            if "B" in df.iloc[i,2]:
                print(df.iloc[i,2])
                df.iloc[i,2] = df.iloc[i,2].replace("B","")
                df.iloc[i,2]=float(df.iloc[i,2])
                dict[i] = df.iloc[i,2]
    #print(dict)
    list1 = sorted(dict.values())[-10:]
    #print(list(dict.keys())[list(dict.values()).index(list1[0])])
    print(list1)
    print("1st largest")
    x= list(dict.keys())[list(dict.values()).index(list1[9])]
    print(x)
    print(df.loc[x,:])
    print("--------------------")
    print("2nd largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[8])],:])
    print("--------------------")
    print("3rd largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[7])],:])
    print("--------------------")
    print("4th largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[6])],:])
    print("--------------------")
    print("5th largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[5])],:])
    print("--------------------")
    print("6th largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[4])],:])
    print("--------------------")
    print("7th largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[3])],:])
    print("--------------------")
    print("8th largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[2])],:])
    print("--------------------")
    print("9th largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[1])],:])
    print("--------------------")
    print("10th largest")
    print(df.loc[list(dict.keys())[list(dict.values()).index(list1[0])],:])
        
        

if __name__ == "__main__":
    main()