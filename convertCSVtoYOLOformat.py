import csv

def main():
    with open('capybara_dataset/data/test_labels.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for row in csvFile:
            print(row['filename'])
            fileName = row['filename']
            width = row['width']
            height = row['height']
            xMin = row['xmin']
            xMax = row['xmax']
            yMin = row['ymin']
            yMax = row['ymax']

main()