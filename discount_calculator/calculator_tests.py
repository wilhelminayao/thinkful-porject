from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", type="float", help="price of meal")
parser.add_option("-t", "--tax", dest="tax_percent", type="float", help="rate of the tax",default = 0.035 )
parser.add_option("-t", "--tip", dest="tip_percent", type="float",help="percent tip you want to leave")

(options, args) = parser.parse_args()
if not options.meal:
    parser.error("Please enter the price of meal")
if not options.tip_percent:
    parser.error("Please leave tips")

tax_value = options.meal * options.tax_percent
meal_with_tax = tax_value + options.meal
tip_value = meal_with_tax * options.tip_percent
total = meal_with_tax + tip_value

print "The initial price of the meal was ${0:.2f}.".format(options.meal)
print "The tax is ${0:.2f} for tax.".format(tax_value)
print "${1:.2f} tips you left".format(int(100*options.tax_percent), tax_value)
print "The total of your meal is ${0:.2f}.".format(total)


