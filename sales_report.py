"""Generate sales report showing total melons each salesperson sold."""

##Creates corresponding lists salespeople and melons_sold
salespeople = []
melons_sold = []

##opens a set file path
f = open('sales-report.txt')
##goes over each line in the file, reads it and separates into a list
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    ##sets variables from split line to correspond with salesperson names 
    ##and melons sold
    salesperson = entries[0]
    melons = int(entries[2])

    ##checks if salesperson has already been added to sales list
    if salesperson in salespeople:
        ##gets the index for the salesperson
        position = salespeople.index(salesperson)

        ##updates the corresponding entry in the melons list
        melons_sold[position] += melons
    ##adds salesperson and melon initial values if not already in lists
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

##prints your lists 
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

##This would be easier done saving the info in a dictionary with salespeople
##as they keys and melons sold as the values 
