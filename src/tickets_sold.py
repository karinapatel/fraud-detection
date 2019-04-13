import matplotlib.pyplot as plt
def get_num_tickets_sold(df):
    # Input is a dataframe
    # Output is a list
    tickets_sold = [] # Create new list to add tickets sold
    # Itterate through each event
    for row in df['ticket_types']:
        sold = []
        # Get the quantity sold for each price level
        for price in row:
            sold.append(price['quantity_sold'])
        # Add tickets sold to the list
        if len(sold) > 0:
            tickets_sold.append(sum(sold))
        # If there are no events make tickets sold = 0
        else:
            tickets_sold.append(0)
    # returns list of number of tickets sold
    return tickets_sold

def plot_tickets_sold(tickets_sold,df):
    # Make scatter plot of tickets sold against the target value
    plt.scatter(tickets_sold,df['Target'])
    # Add title to the plot
    plt.title('Tickets Sold vs Fraud')
    # Add labels to x and y axis
    plt.xlabel('Number of Tickets Sold')
    plt.ylabel('Fraud or Not Fraud')