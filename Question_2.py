import csv
import os
import sys

from PIL import Image

color_key = [(1, 1, 1), (0, 0, 0)]
rejected_img = []


def iterate_folder(directory, directory_in_str):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        taskid = filename.split('_')[1]
        if filename.endswith('.png'):
            check_colors(directory_in_str, filename)


def check_colors(directory_in_str, filename):
    corrected_path = os.path.join(directory_in_str, filename)
    img = Image.open(corrected_path)
    colors = img.getcolors()
    if colors:
        for color in colors:
            if color[1] not in color_key:
                if filename not in rejected_img:
                    rejected_img.append(filename)


def create_csv(directory_in_str, rejected_img):
    with open(directory_in_str + '_reporting.csv', 'w') as outputcsv:
        csv_output = csv.writer(outputcsv)
        csv_output.writerow(['filename'])
        for img in rejected_img:
            csv_output.writerow(img)


if __name__ == '__main__':
    directory_in_str = sys.argv[1]
    directory = os.fsencode(directory_in_str)
    iterate_folder(directory, directory_in_str)
    create_csv(directory_in_str, rejected_img)
    print(rejected_img)
