def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]  # Better practice to have intermittent values -> don't splice data inside with
    values = [float(i) for i in values]
    average_local = sum(values) / len(values) # Avoid having matching var names -> average
    return average_local


average = get_average()
print(average)