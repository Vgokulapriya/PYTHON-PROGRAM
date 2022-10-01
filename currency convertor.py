# currency convertor
def main():
    print("convert US dollars to pounds sterling")
    print()

    dollars = eval(input("Enter the amonut in Dollars :"))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "pounds.")


convert_to_pounds = lambda dollars: dollars * 0.82

main()
