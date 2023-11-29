# Creating a program to enter and calculate insurance policy information.
# Date Written: Nov 26th, 2023 - End date: Nov 28th, 2023
# Author: Benjamin Follett

# Import any required libraries.

import datetime

# Setting up program constants.
NEXT_POLICY_NUMBER = 1944
THE_BASIC_PREMIUM = 869.00
DISCOUNT_FOR_ADDITIONAL_CARS = .25
COST_OF_EXTRA_LIABILITY_COVERAGE = 130.00
COST_OF_GLASS_COVERAGE = 86.00
COST_FOR_LOANER_CAR_COVERAGE = 58.00
HST_RATE = .15
PROCESSING_FEE_FOR_MONTHLY_PAYMENTS = 39.99

# Setting up program functions

def hello():
    name = str(input("Enter your name: "))
    if name:
        print("Hello " + str(name))
        return
    else:
        print("Hello World")
        return

print("Loading please wait...")   
def fakeloadingsim(num):
    if num<=0:
        print("Loading complete")
    else:
        print(num)
        fakeloadingsim(num-1)

def Welcome():
    print("welcome to One stop Insurance company :)")
    
    

# Start of the main program.
while True:
    fakeloadingsim(3)
    Welcome()
    hello()
    CustFirstName = input("Enter the Customers first name: ")
    CustLastName = input("Enter customers last name: ")
    Address = input("Enter customers address: ")
    City = input("Enter the city that the customer resides in: ")

    ProvinceLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK"]

    while True:
        Province = input("Enter the Province (XX): ").upper()
        if Province == "":
            print("Please re-enter province cannot be blank. ")
        elif len(Province) != 2:
            print("Province can only be 2 characters long please try again. ")
        elif Province not in ProvinceLst:
            print("Not a valid province please re-enter. ")
        else:
            break


    PostalCode = input("Enter the customers postal code: ")
    PhoneNumb = input("Enter the customers phone number: ")
    NumberOfCarsInsured = int(input("Enter the number cars being insured: "))
    ExtraLiability = input("Would you like extra liability? (Y OR N): ").upper()

    if ExtraLiability == "Y":
        ExtraLiabilityBenfit = 1000000.00
    else:
        ExtraLiabilityBenfit = 0

    OptGlassCost = input("Would you like optional glass coverage ? (Y or N): ").upper()

    if OptGlassCost == "Y":
        print("(Optional glass coverage granted.)")
    else:
        print("(No worries.)")

    OptLoanCar = input("Would you like to be provided with a loaner car ? (Y or N): ").upper()

    if OptLoanCar == "Y":
        print("(Loaner car granted)")
    else:
        print("(No worries)")
    
    PayMethLst = ["Full", "Monthly", "Down Pay"]
    
    while True:
        PayMeth = input("Enter payment method (Full - Monthly - Down Pay): ")
        if PayMeth == "":
            print("Cannot accept blank space - please try again.")
        elif PayMeth not in PayMethLst:
            print("Error - Not a valid payment method - please re-enter.")
        elif PayMeth == "Down Pay":
            DownPay = float(input("Enter down payment amount: "))
        break
            
    CostLst = []
    DateLst = []
    while True:
        CostOfPrevClaim = input("Enter the cost of the previous claim. (Press enter to finish): ")
        if CostOfPrevClaim =="":
            break
        DateOfPrevClaim = input("Enter date of previous claim (YYYY-MM-DD): ")
        DateOfPrevClaim = datetime.datetime.strptime(DateOfPrevClaim, "%Y-%m-%d")

        CostLst.append(CostOfPrevClaim)
        DateLst.append(DateOfPrevClaim)

    break
    

# Setting up program calculations.

InsurancePremium = THE_BASIC_PREMIUM + 1 * DISCOUNT_FOR_ADDITIONAL_CARS

if ExtraLiability =="Y":
    CostExtraLiability = COST_OF_EXTRA_LIABILITY_COVERAGE
else:
    CostExtraLiability = 0

if OptGlassCost == "Y":
    CostOptGlassCost =  COST_OF_GLASS_COVERAGE
else:
    CostOptGlassCost = 0

if OptLoanCar == "Y":
    CostOptLoanCar = COST_FOR_LOANER_CAR_COVERAGE
else:
    CostOptLoanCar = 0

TotalExtraCost = CostExtraLiability + CostOptGlassCost + CostOptLoanCar
TotalInsPrem = COST_OF_EXTRA_LIABILITY_COVERAGE + TotalExtraCost 
TaxOnInPrem = TotalInsPrem * HST_RATE
TotalCost = TotalInsPrem + TaxOnInPrem
MonthlyPay = PROCESSING_FEE_FOR_MONTHLY_PAYMENTS + (TotalCost / 8)
if PayMeth == "Down Pay":
    MonthlyPay = DownPay - PROCESSING_FEE_FOR_MONTHLY_PAYMENTS + (TotalCost / 8)
 
 


        
       
# Program outputs.
print(f"")
print(f"                                One Stop Insurance Company")
print(f"                                         Receipt")
print(f"                       ----------------------------------------------")
print(f"                        Client Name and Address:")
print(f"")
print(f"                        {CustFirstName:<10s}")
print(f"                        {CustLastName:<10s}")
print(f"                        {Address:<24s}")
print(f"                        {City:<15s}, {Province:<2s}, {PostalCode:<6s}")
print(f"")
print(f"                        Phone: {PhoneNumb:<10s}")
print(f"                       ----------------------------------------------")
print(f"                        # Of Cars Insured: {NumberOfCarsInsured:<2d}")
print(f"")
print(f"                        Extra Liability:                            {ExtraLiability:>1s}")
print(f"                        Glass Coverage:                             {OptGlassCost:>1s}")
print(f"                        Loaner Car:                                 {OptLoanCar:>1s}")
print(f"                        Payment Type:                        {PayMeth:>7s}")
print(f"                       ----------------------------------------------")
MonthlyPayDsp = "${:.2f}". format(MonthlyPay)
print(f"                        Monthly Payment:                      {MonthlyPayDsp:>6s}")
InsurancePremiumDsp = "${:.2f}". format(InsurancePremium)
print(f"                        Basic Insurance Premium Cost:         {InsurancePremiumDsp:>6s}")
TaxOnInPremDsp = "${:.2f}". format(TaxOnInPrem)
print(f"                        Tax On Insurance Premium:             {TaxOnInPremDsp:>6s}")
TotalInsPremDsp = "${:.2f}". format(TotalInsPrem)
print(f"                        Total Insurance Premimum:             {TotalInsPremDsp:>6s}")
TotalExtraCostDsp = "${:.2f}". format(TotalExtraCost)
print(f"                        Total Extra Cost:                     {TotalExtraCostDsp:>6s}")
print(f"")
print(f"")
TotalCostDsp = "${:.2f}". format(TotalCost)
print(f"                        Total:                                {TotalCostDsp:>6s}")
print(f"                       ----------------------------------------------")
print(f"")
print(f"Claim #  Claim Date        Amount")
print(f"---------------------------------")
for date in DateLst:
 CostandDatenum = 1
 for cost in CostLst:
    print(f"  {str(CostandDatenum)}. {date} ${cost}")
    CostandDatenum += 1
print()
print()