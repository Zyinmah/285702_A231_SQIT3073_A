import os
import math
os.system('cls')
#os.system('clear')

#LIst to store loan calculations
loan_calculation=[]

#default DSR threshold
dsr_threshold=70

#Function to calculate a new loan
def calculate_loan():
    while True:
        try:
            while True:
                applicant_monthly_income=input("Enter monthly income (type 'menu' to return main menu)  : RM ")
                if applicant_monthly_income.lower() == 'menu':
                    return  # Return to the main menu
                else:
                    applicant_monthly_income = float(applicant_monthly_income)

                principal_loan_amount=float(input("Enter principal loan amount                             : RM "))
                annual_interest_rate=float(input("Enter annual interest rate(in %)                        : "))
                loan_term=int(input("Enter loan term(in years)                               : "))
                house_loan=float(input("Enter monthly housing loan                              : RM "))
                other_financial_commitments=float(input("Enter other monthly financial commitments               : RM "))
                print()

                if principal_loan_amount<=0 or annual_interest_rate<=0 or loan_term<=0 or applicant_monthly_income<=0 or house_loan<0 or other_financial_commitments<0:
                    print()
                    print("Input error: All values must be positive. Please enter all valid input again.")                    
                else:
                    monthly_installment=float(calculate_monthly_installment(annual_interest_rate,loan_term,principal_loan_amount))
                    total_payable=float(calculate_total_payable(loan_term,monthly_installment))
                    dsr=float(calculate_DSR([monthly_installment,other_financial_commitments,house_loan],applicant_monthly_income))
                    
                    if dsr<=dsr_threshold:
                        eligibility=str("Eligible ")           
                    else :
                        eligibility=str("Not Eligible")
                    
                    # Create a dictionary to store the loan details
                    loan_details = {
                    "Monthly Income":applicant_monthly_income,
                    "Principal Loan Amount": principal_loan_amount,
                    "Annual Interest Rate": annual_interest_rate,
                    "Loan Term": loan_term,
                    "Monthly Installment": monthly_installment,
                    "Total Payable": total_payable,
                    "DSR": dsr,
                    "Eligibility": eligibility
                    }       

                    # Append the loan details dictionary to the list
                    loan_calculation.append(loan_details)
                    
                    print(f"Monthly Installment                                     : RM {monthly_installment:.2f}")
                    print(f"Total Payable                                           : RM {total_payable:.2f}")
                    print(f"DSR                                                     : {dsr:.2f}%"+"- "+str(eligibility)+"\n")
                    return  
        except ValueError as e:
            print("\nInput error: Only integers and floating-point number are allowed. Please input all value again.")

#Function to calculate the monthly installment based on loan details
def calculate_monthly_installment(annual_interest_rate,loan_term,principal_loan_amount):
    monthly_interest_rate=float((annual_interest_rate/12)/100)
    number_payments=int(loan_term*12)
    monthly_installment= float(principal_loan_amount * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_payments)) / (math.pow(1 + monthly_interest_rate, number_payments) - 1))
    return monthly_installment

#Function to calculate the total payable amount over the loan tern
def calculate_total_payable(loan_term,monthly_installment):
    number_payments=int(loan_term*12)
    total_payable=float(monthly_installment*number_payments)
    return total_payable

#Function to calculate the Debt-Servie Ratio(DSR)
def calculate_DSR(debt_commitments,monthly_income):
    dsr=(sum(debt_commitments)/monthly_income)*100
    return dsr

# Function to display all previous loan calculations
def display_all_previous_loan_calculations():
    if not loan_calculation:
        print("No previous loan calculations.")
    else:
        print("------------------------------------------------------------------------")
        print("                  Display All Previous Loan Calculations")
        print("------------------------------------------------------------------------")
        for i, loan_details in enumerate(loan_calculation):
            print(f"Loan Calculation {i + 1}")
            print(f"Monthly Income          : RM {loan_details['Monthly Income']:.2f}")
            print(f"Principal Loan Amount   : RM {loan_details['Principal Loan Amount']:.2f}")
            print(f"Annual Interest Rate    : {loan_details['Annual Interest Rate']:.2f}%")
            print(f"Loan Term               : {loan_details['Loan Term']}")
            print(f"Monthly Installment     : RM {loan_details['Monthly Installment']:.2f}")
            print(f"Total Payable           : RM {loan_details['Total Payable']:.2f}")

            if loan_details['DSR']<=dsr_threshold:
                print(f"DSR                     : {loan_details['DSR']:.2f}% - Eligible")
                print("------------------------------------------------------------------------")
            else:
                 print(f"DSR                     : {loan_details['DSR']:.2f}% - Not Eligible")
                 print("------------------------------------------------------------------------")
            

# Function to modify the DSR threshold
def modify_dsr_threshold():
    global dsr_threshold
    print(f"The current DSR threshold is set at {dsr_threshold}%")
    while True:
        new_threshold = input("Enter the new DSR threshold (type 'menu' to return to main menu ): ")
        if new_threshold.lower() == 'menu':
            return  # Return to the main menu
        try:
            new_threshold = float(new_threshold)
            if new_threshold > 0:
                dsr_threshold = new_threshold
                print(f"DSR threshold updated to {dsr_threshold}%.")
                break
            else:
                print("Invalid threshold. Please enter a positive value")
        except ValueError:
            print("Invalid input. Please enter number or 'menu'")
    return dsr_threshold

# Function to delete a previous loan calculation
def delete_calculation():
    while True:
        try:
            if not loan_calculation:
                print("No previous loan calculations.")
                return
            else:
                display_all_previous_loan_calculations()
                index_to_delete=(input("Enter the calculation number to delete(type 'menu' to return to main menu ): "))
                if index_to_delete.lower() == 'menu':
                    return  # Return to the main menu
                index_to_delete = int(index_to_delete)
                if 1 <= index_to_delete <= len(loan_calculation):
                    del loan_calculation[index_to_delete - 1]
                    print(f"Calculation {index_to_delete} deleted successfully.")
                    return
                else:
                    print("\nInvalid calculation number.Please enter a valid calculation number.\n")            
        except ValueError:
             print("\nInvalid input. Please enter a valid calculation number.\n")

# Main function for user choices
def main():
    while True:
        try:            
            choice=0
            while choice!=5:
                print("************************************************************************")
                print("                       Welcome to the Loan Calculator                   ")
                print("************************************************************************")
                print("1. Calculate New Loan")
                print("2. Display All Previous Loan Calculations")
                print("3. Modify DSR Threshold")
                print("4. Delete a Previous Calculation")
                print("5. Exit")

                choice=int(input("Enter your choice\t\t\t\t\t: "))
                print()

                if choice==1:
                    calculate_loan()
                elif choice==2:
                    display_all_previous_loan_calculations()
                elif choice==3:
                    dsr_threshold=modify_dsr_threshold()
                elif choice==4:
                    delete_calculation()
                elif choice==5:
                    print("************************************************************************")
                    print("                   Thanks for using our loan calculator.")
                    print("************************************************************************")
                    break
                else :
                    print("Invalid number, enter your choice again.\n")
            break                    
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

# Run the main function
if __name__ =="__main__":
    main()    
