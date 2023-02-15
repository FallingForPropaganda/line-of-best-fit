def line_of_best_fit(coordinates):
    x_total = 0
    y_total = 0
    total = 0
    for item in coordinates:
        x_total += item[0]
        y_total += item[1]
        total += 1
    x_average = x_total/total
    y_average = y_total/total
    
    x_minus_x_average = []
    y_minus_y_average = []
    for item in coordinates:
        x_minus_x_average.append(item[0] - x_average)
        y_minus_y_average.append(item[1] - y_average)

    x_y = 0
    x_x = 0
    counter = 0
    while counter != len(coordinates):
        x_x += (x_minus_x_average[counter] * x_minus_x_average[counter])
        x_y += (x_minus_x_average[counter] * y_minus_y_average[counter])
        counter += 1
    slope = x_y/x_x
    
    b = y_average - slope*x_average

    return slope, b