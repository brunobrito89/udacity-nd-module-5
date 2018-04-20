#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    aux = []

    for x in range(len(predictions)):
        aux.append(
            {
                'ages': ages[x][0],
                'net_worths': net_worths[x][0],
                'error': predictions[x][0] - net_worths[x][0], }
        )

    aux = sorted(aux, key=lambda k: k['error'])
    cleaned_data = []

    for val in aux:
        cleaned_data.append((val['ages'], val['net_worths'], val['error']))

    print("Valor do cleaned data")
    print(cleaned_data)

    return cleaned_data[:81]
