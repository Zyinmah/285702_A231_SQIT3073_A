#SQIT3073 Group Assignment 1
#Title:  Commercial Banks and Islamic Banks: Impaired Loans and Impairment Provisions
#MAH ZHI YIN 285702
#CHEOK LI EN 285942

import matplotlib.pyplot as plt
import pandas as pd
import os

# Clear the terminal screen
os.system('cls')

# Excel file path
excel_file = "C:\\Users\\louis\\Documents\\Python\\CLASS\\GRP1\\1.21.2a.xlsx"

# Number of rows to skip based on your Excel file structure
skip_rows = 4

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file, skiprows=skip_rows, na_values=[''])

# Assuming df is your DataFrame
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')

# Forward fill NaN values in the 'Year' column
df['Year'] = df['Year'].ffill()

# Identify the correct column name for the period
periods_column = 'End of period'  # Update with the correct column name

# Convert 'Period' to a string format (e.g., 'January', 'February', etc.)
df[periods_column] = df[periods_column].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))

# Combine 'Year' and 'Period' columns
df['Year-Period'] = df['Year'].astype(str) + '-' + df[periods_column]

# Drop 'Year' and 'End of period' columns
df = df.drop(['Year', periods_column], axis=1)

# Move 'Year-Period' column to the first position
df = df[['Year-Period'] + [col for col in df.columns if col != 'Year-Period']]

# Define short forms for each column
short_forms = {
    'Year-Period': 'Year-Period',
    'Impaired loans': 'IL',
    'Individual impairment provisions': 'IndIP',
    'Collective Impairment provisions': 'ColIP',
    'Ratio of net impaired loans to net total loans(%)': 'RN.IL(%)',
    'Ratio of individual and collective impairment provisions to total impaired loans(%)': 'R.Ind&ColIP(%)'
}

# Rename columns with short forms for terminal display
df_terminal = df.rename(columns=short_forms)

# Set display option to show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Set display format for floating-point numbers to two decimal places
pd.options.display.float_format = '{:.2f}'.format
def display_dataset():
    print("-----------------------------------------------------------------------------------------")
    print("Data set for Commercial Banks and Islamic Banks: Impaired Loans and Impairment Provisions")
    print("-----------------------------------------------------------------------------------------")

# Display the DataFrame with NaN values replaced by '-'
    print(df_terminal)

def line_IL_IndIP_ColIP() :   
    # Plotting

    # Exclude 'Ratio' columns from the scatter plot
    columns_to_plot = [col for col in df.columns if 'Ratio' not in col]

    for column in columns_to_plot[1:]:  # Exclude 'Year-Period'
        plt.plot(df['Year-Period'], df[column], label=column)

    plt.xlabel('Year-Period')
    plt.ylabel('RM million')
    plt.title('Impaired loans, Individual impairment provisions & Collective Impairment provisions')
    unique_years = df['Year-Period'].apply(lambda x: x.split('-')[0]).unique().astype(str)  # Get unique years
    plt.xticks([f"{year}-January" for year in unique_years], rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()

def scatter_RatioIL():
    # Select the specific columns for the line plot
    ratios_to_plot = ['Ratio of net impaired loans to net total loans(%)']

    for column in ratios_to_plot:
        plt.scatter(df['Year-Period'], df[column],color='red')

    plt.ylim(0, 100)
    plt.xlabel('Year-Period')
    plt.ylabel('Ratio (%)')
    plt.title('Ratio of net impaired loans to net total loans')
    unique_years = df['Year-Period'].apply(lambda x: x.split('-')[0]).unique().astype(str)  # Get unique years
    plt.xticks([f"{year}-January" for year in unique_years], rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def histogram_ratioIND_COLIP():
    # Select the column for the histogram
    column_to_plot = 'Ratio of individual and collective impairment provisions to total impaired loans(%)'

    # Plot histogram
    plt.bar(df['Year-Period'], df[column_to_plot], alpha=0.7)

    # Plot distribution line (KDE)
    plt.plot(df['Year-Period'], df[column_to_plot], color='red')


    plt.xlabel('Year-Period')
    plt.ylabel('Ratio(%)')
    plt.title('Ratio of individual and collective impairment provisions to total impaired loans')
    unique_years = df['Year-Period'].apply(lambda x: x.split('-')[0]).unique().astype(str)  # Get unique years
    plt.xticks([f"{year}-January" for year in unique_years], rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

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

# Run the main function
if __name__ =="__main__":
    main()    
    
