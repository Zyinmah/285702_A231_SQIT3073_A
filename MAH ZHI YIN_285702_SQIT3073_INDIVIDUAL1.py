import os
import math
os.system('cls')

#LIst to store loan calculations
loan_calculation=[]

#default DSR threshold
dsr_threshold=70

#Function to calculate a new loan
def calculate_loan():
    
    applicant_monthly_income=float(input("Enter applicant monthly income   : RM "))
    principal_loan_amount=float(input("Enter principal loan amount      : RM "))
    annual_interest_rate=float(input("Enter annual interest rate(in %) : "))
    loan_term=int(input("Enter loan term(in years)        : "))
    house_loan=float(input("Enter house loan                 : RM "))
    other_financial_commitments=float(input("Enter other financial commitments: RM "))
    print()
    if principal_loan_amount<=0 or annual_interest_rate<=0 or loan_term<=0 or applicant_monthly_income<=0 :
        print("All values must be positive. Please enter valid inputs")
        
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
        
        print(f"Monthly Installment: RM {monthly_installment:.2f}")
        print(f"Total Payable     : RM {total_payable:.2f}")
        print(f"DSR               : {dsr:.2f}%"+"- "+str(eligibility))
        
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
        print("\nNo previous loan calculations.")
    else:
        for i, loan_details in enumerate(loan_calculation):
            print(f"Loan Calculation {i + 1}")
            print(f"Principal Loan Amount   : RM {loan_details['Principal Loan Amount']:.2f}")
            print(f"Annual Interest Rate    : {loan_details['Annual Interest Rate']:.2f}%")
            print(f"Loan Term               : {loan_details['Loan Term']}")
            print(f"Monthly Installment     : RM {loan_details['Monthly Installment']:.2f}")
            print(f"Total Payable           : RM {loan_details['Total Payable']:.2f}")
            print(f"DSR                     : {loan_details['DSR']:.2f}% - {loan_details['Eligibility']}")
            print()

# Function to modify the DSR threshold
def modify_dsr_threshold():
    global dsr_threshold
    print(f"The current DSR threshold is set at {dsr_threshold}%")
    new_threshold=float(input("Enter the new DSR thresold: "))
    if new_threshold>0:
        dsr_threshold=new_threshold
        print(f"DSR threshold updated to {dsr_threshold}%.")
    else:
        print("Invalid thresold.Please enter a positive value")

# Function to delete a previous loan calculation
def delete_calculation():
    if not loan_calculation:
        print("\nNo previous loan calculations.")
    else:
        display_all_previous_loan_calculations()
        index_to_delete=int(input("Enter the calculation number to delete: "))
        if 1 <= index_to_delete <= len(loan_calculation):
            del loan_calculation[index_to_delete - 1]
            print(f"Calculation {index_to_delete} deleted successfully.")
        else:
            print("Invalid calculation number.")

# Main function for user choices
def main():
    choice=0
    while choice!=5:
        print("\n1. Calculate New Loan")
        print("2. Display All Previous Loan Calculations")
        print("3. Modify DSR Threshold")
        print("4. Delete a Previous Calculation")
        print("5. Exit")

        choice=int(input("Enter your choice\t\t : "))

        if choice==1:
            calculate_loan()
        elif choice==2:
            display_all_previous_loan_calculations()
        elif choice==3:
            modify_dsr_threshold()
        elif choice==4:
            delete_calculation()
        elif choice==5:
            print("Thanks for using our loan calculator.")
        else :
            print("Invalid number, enter your choice again.")

# Run the main function
if __name__ =="__main__":
    main()    
