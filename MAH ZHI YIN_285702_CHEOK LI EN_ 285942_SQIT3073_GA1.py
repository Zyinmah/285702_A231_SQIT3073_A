#Group Assignment 1:
#Title: Commercial Banks and Islamic Banks: Impaired Loans and Impairment Provisions
#Mah Zhi Yin_285702
#Cheok Li En_285942

import matplotlib.pyplot as plt
import pandas as pd
import os
os.system('cls')

excel_file = "C:\\Users\\louis\\Documents\\Python\\CLASS\\GRP1\\1.21.2a.xlsx"
skip_rows = 4
try:
    df = pd.read_excel(excel_file, skiprows=skip_rows, na_values=[''])
    print("Excel file read successfully!")
except Exception as e:
    print("Program terminated, because an error occurred while reading the Excel file. Please ensure that the file exists and the path is correct.")
    exit()

#Convert Year to integer and fill in missing value in Year column
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')
df['Year'] = df['Year'].ffill()
#Convert End of period to string(Example: 1=January,2=February and so on)
df['End of period'] = df['End of period'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))
#Create Year-Period by combining Year and End of period and reorder Year-Period column to first column
df['Year-Period'] = df['Year'].astype(str) + '-' + df['End of period']
df = df[['Year-Period'] + [col for col in df.columns if col != 'Year-Period']]
#Drop Year and End of period column
df = df.drop(['Year', 'End of period'], axis=1)
#display max row and column 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

short_forms = {
    'Year-Period': 'Year-Period',
    'Impaired loans': 'IL',
    'Individual impairment provisions': 'IndIP',
    'Collective Impairment provisions': 'ColIP',
    'Ratio of net impaired loans to net total loans(%)': 'RN.IL(%)',
    'Ratio of individual and collective impairment provisions to total impaired loans(%)': 'R.Ind&ColIP(%)'
}
df_terminal = df.rename(columns=short_forms)
pd.options.display.float_format = '{:.2f}'.format
def display_dataset():
    print("-----------------------------------------------------------------------------------------")
    print("Data set for Commercial Banks and Islamic Banks: Impaired Loans and Impairment Provisions")
    print("-----------------------------------------------------------------------------------------")
    print(df_terminal)

#Line Graph for Impaired loans, Individual impairment provisions & Collective Impairment provisions
def line_IL_IndIP_ColIP() :   
    columns_to_plot = [col for col in df.columns if 'Ratio' not in col]#
    for column in columns_to_plot[1:]:  
        plt.plot(df['Year-Period'], df[column], label=column)
    plt.xlabel('Year-Period')
    plt.ylabel('RM million')
    plt.title('Impaired loans, Individual impairment provisions & Collective Impairment provisions')
    unique_years = df['Year-Period'].apply(lambda x: x.split('-')[0]).unique().astype(str) 
    plt.xticks([f"{year}-January" for year in unique_years], rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()
#Scatter Plot for Ratio of net impaired loans to net total loans
def scatter_RatioIL():
    ratios_to_plot = ['Ratio of net impaired loans to net total loans(%)']
    for column in ratios_to_plot:
        plt.scatter(df['Year-Period'], df[column],color='red')
    plt.ylim(0, 100)
    plt.xlabel('Year-Period')
    plt.ylabel('Ratio (%)')
    plt.title('Ratio of net impaired loans to net total loans')
    unique_years = df['Year-Period'].apply(lambda x: x.split('-')[0]).unique().astype(str) 
    plt.xticks([f"{year}-January" for year in unique_years], rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
#Histogram for Ratio of individual and collective impairment provisions to total impaired loans
def histogram_ratioIND_COLIP():
    plt.bar(df['Year-Period'], df['Ratio of individual and collective impairment provisions to total impaired loans(%)'], alpha=0.7, width=1, edgecolor='black')
    plt.xlabel('Year-Period')
    plt.ylabel('Ratio(%)')
    plt.title('Ratio of individual and collective impairment provisions to total impaired loans')
    unique_years = df['Year-Period'].apply(lambda x: x.split('-')[0]).unique().astype(str)  
    plt.xticks([f"{year}-January" for year in unique_years], rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
#Main function
def main():
    while True:
        try:            
            choice=0
            while choice!=5:
                print("*****************************************************************************************************************")
                print("  Welcome to Graph Application for Commercial Banks and Islamic Banks: Impaired Loans and Impairment Provisions  ")
                print("*****************************************************************************************************************")
                print("1. Display data set")
                print("2. Line Graph for Impaired loans, Individual impairment provisions & Collective Impairment provisions")
                print("3. Scatter Plot for Ratio of net impaired loans to net total loans")
                print("4. Histogram for Ratio of individual and collective impairment provisions to total impaired loans")
                print("5. Exit")

                choice=int(input("Enter your choice\t\t: "))
                print()

                if choice==1:
                    display_dataset()
                elif choice==2:
                    line_IL_IndIP_ColIP()
                elif choice==3:
                    scatter_RatioIL()
                elif choice==4:
                    histogram_ratioIND_COLIP()
                elif choice==5:
                    print("*****************************************************************************************************************")
                    print("                                    Thanks for using our Graph Application.")
                    print("*****************************************************************************************************************")
                    break
                else :
                    print("Invalid number, enter your choice again.\n")
            break                    
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
#Run main function
if __name__ =="__main__":
    main()    
    
