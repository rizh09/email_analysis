import csv
from operator import itemgetter
import matplotlib.pyplot as plt

def read_and_order_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Read the CSV data into a list of dictionaries

    # Extract the sender's activities and dates
    sender_activities = {}
    receiver_activities = {}
    for row in data:
        sender = row['From: (Name)']
        receiver = row['To: (Name)']

        # Count sender activities
        if sender not in sender_activities:
            sender_activities[sender] = 1
        else:
            sender_activities[sender] += 1

        # Count receiver activities
        if receiver not in receiver_activities:
            receiver_activities[receiver] = 1
        else:
            receiver_activities[receiver] += 1

    # Sort sender activities by count
    sorted_sender_activities = sorted(sender_activities.items(), key=itemgetter(1), reverse=True)

    # Select the top ten senders
    top_senders = dict(sorted_sender_activities[:10])

    # Sort receiver activities by count
    sorted_receiver_activities = sorted(receiver_activities.items(), key=itemgetter(1), reverse=True)

    # Select the top ten receivers
    top_receivers = dict(sorted_receiver_activities[:10])

    # Prepare data for plotting
    sender_labels = list(top_senders.keys())
    sender_counts = list(top_senders.values())

    receiver_labels = list(top_receivers.keys())
    receiver_counts = list(top_receivers.values())

    # Plot the top senders' activities
    plt.subplot(2, 1, 1)
    plt.bar(sender_labels, sender_counts)
    plt.xlabel('Sender')
    plt.ylabel('Number of Emails Sent')
    plt.title('Top Ten Senders by Number of Emails Sent')

    # Plot the top receivers' activities
    plt.subplot(2, 1, 2)
    plt.bar(receiver_labels, receiver_counts)
    plt.xlabel('Receiver')
    plt.ylabel('Number of Emails Received')
    plt.title('Top Ten Receivers by Number of Emails Received')

    plt.tight_layout()  # Adjust the spacing between subplots
    plt.xticks(rotation=45)
    plt.show()

# Usage example
filename = 'real_data.csv'
read_and_order_csv(filename)
