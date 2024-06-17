import csv
import os

def main():
    with open('data/train_labels.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for row in csvFile:
            print(row['filename'][:-5])

            # Getting all the data
            fileName = row['filename']
            width = float(row['width'])
            height = float(row['height'])
            xMin = float(row['xmin'])
            xMax = float(row['xmax'])
            yMin = float(row['ymin'])
            yMax = float(row['ymax'])
            X = str((xMin + xMax) / (2 * width))
            Y = str((yMin + yMax) / (2 * height))
            W = str((xMax - xMin) / width)
            H = str((yMax - yMin) / height)

            # Creating the new label txt file
            txtFilePath = "data/labels/train/" + fileName[:-5] + ".txt"
            print(txtFilePath)


            if os.path.exists(txtFilePath):
                print("T")
                with open(txtFilePath, "a") as f:
                    f.write("0 " + X + " " + Y + " " + W + " " + H + "\n")
            else:
                print("F")
                with open(txtFilePath, "w") as f:
                    f.write("0 " + X + " " + Y + " " + W + " " + H + "\n")

main()