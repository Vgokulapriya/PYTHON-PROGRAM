# collect the necessary: principal,apr,years
# calculat the monthly payment


def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the amount interest rate: "))
    years = int(input("Input the amount of years:"))

    monthly_intrest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = (
        principal
        * monthly_intrest_rate
        / (1 - (1 + monthly_intrest_rate) ** (-amount_of_months))
    )

    print("print the amount name for this loan is : %.2f " % monthly_payment)


main()
