def convert_attribute(value, attribute):
    if attribute == 'age':
        if value < 30:
            return "young"
        elif value < 50:
            return "middle-aged"
        elif value < 70:
            return "senior"
        else:
            return "old"
    elif attribute == 'capital-gain':
        if value <= 0:
            return "none"
        elif value < 2000:
            return "small"
        elif value < 5000:
            return "medium"
        else:
            return "high"
    elif attribute == 'capital-loss':
        if value <= 0:
            return "none"
        elif value < 2000:
            return "small"
        elif value < 5000:
            return "medium"
        else:
            return "high"
    elif attribute == 'hours-per-week':
        if value <= 25:
            return "half-time"
        elif value <= 40:
            return "full-time"
        elif value <= 60:
            return "overtime"
        else:
            return "too-many"
    else:
        return value


with open('adult.data', 'r') as data_file:
    lines = data_file.readlines()

converted_lines = []

for line in lines:
    attributes = line.strip().split(',')

    if len(attributes) < 15:
        continue

    converted_line = []

    try:
        converted_line.append("age=" + convert_attribute(int(attributes[0].strip()), 'age'))
        converted_line.append("workclass=" + attributes[1].strip())
        converted_line.append("education=" + attributes[2].strip())
        converted_line.append("edu_num=" + attributes[3].strip())
        converted_line.append("marital=" + attributes[4].strip())
        converted_line.append("occupation=" + attributes[5].strip())
        converted_line.append("relationship=" + attributes[6].strip())
        converted_line.append("race=" + attributes[7].strip())
        converted_line.append("sex=" + attributes[9].strip())
        converted_line.append("gain=" + convert_attribute(int(attributes[10].strip()), 'capital-gain'))
        converted_line.append("loss=" + convert_attribute(int(attributes[11].strip()), 'capital-loss'))
        converted_line.append("hours=" + convert_attribute(int(attributes[12].strip()), 'hours-per-week'))
        converted_line.append("country=" + attributes[13].strip())
        converted_line.append("salary=" + attributes[14].strip())


    except ValueError:
        continue

    converted_lines.append(" ".join(converted_line))

with open('adult_transaction.data', 'w') as output_file:
    output_file.write('\n'.join(converted_lines))

