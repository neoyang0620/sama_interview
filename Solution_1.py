__author__ = 'Neo Yang'

"""
Question 1

Usage:
    Solution_1.py --source <data_path> --save_path <save_path>

Options:
    <data_path>                     annotation file path
    <save_path>                     output path
    -h --help                       help
"""

import argparse
import json
import os
from PIL import Image, ImageDraw, ImagePalette, ImageColor
import random
import time


def label_analysis(data):
    unique_shape_list = {}
    unique_label_list = {}
    unique_pair_list = {}

    for item in data:
        labels = item['taggable image']
        for label in labels:
            label_name = label['tags']['label']
            shape_name = label['type']
            pair = (shape_name, label_name)
            if shape_name not in unique_shape_list:
                unique_shape_list[shape_name] = 0
            if label_name not in unique_label_list:
                unique_label_list[label_name] = 0
            if pair not in unique_pair_list:
                unique_pair_list[pair] = 0

            unique_shape_list[shape_name] += 1
            unique_label_list[label_name] += 1
            unique_pair_list[pair] += 1
    unique_shape_list = {k: unique_shape_list[k] for k in sorted(unique_shape_list)}
    unique_label_list = {k: unique_label_list[k] for k in sorted(unique_label_list)}
    unique_pair_list = {k: unique_pair_list[k] for k in sorted(unique_pair_list)}
    return unique_shape_list, unique_label_list, unique_pair_list


def visualize_annotations(data):
    shape_list = {}
    label_list = {}
    for item in data:
        labels = item['taggable image']
        for label in labels:
            label_name = label['tags']['label']
            shape_name = label['type']
            if shape_name not in shape_list:
                shape_list[shape_name] = []
            if label_name not in label_list:
                label_list[label_name] = {}
            if shape_name not in label_list[label_name]:
                label_list[label_name][shape_name] = []

            shape_list[shape_name].append(label['points'])
            label_list[label_name][shape_name].append(label['points'])

    # draw output_1.jpg
    img_1 = Image.new("RGB", (3840, 2160), "black")
    cmap = ImageColor.colormap
    shape_color_mapping = {k: i for i, k in enumerate(shape_list.keys())}
    colors = random.sample(cmap.keys(), len(shape_color_mapping))
    output_1_colors = {}
    draw = ImageDraw.Draw(img_1)
    for i, label in enumerate(label_list.keys()):
        bboxes_dict = label_list[label]
        for shape in bboxes_dict.keys():
            if shape == 'rect':
                bboxes = bboxes_dict[shape]
                color = colors[shape_color_mapping[shape]]
                if color not in output_1_colors:
                    output_1_colors[color] = shape
                for box in bboxes:
                    box = [box[0], box[3]]
                    points_list = [(point[0], point[1]) for point in box]
                    points_list = tuple(points_list)
                    draw.rectangle(points_list, fill=color)
            elif shape == 'line':
                bboxes = bboxes_dict[shape]
                color = colors[shape_color_mapping[shape]]
                if color not in output_1_colors:
                    output_1_colors[color] = shape
                for box in bboxes:
                    points_list = [(point[0], point[1]) for point in box]
                    points_list = tuple(points_list)
                    draw.line(points_list, fill=color)
            elif shape == 'polygon':
                bboxes = bboxes_dict[shape]
                color = colors[shape_color_mapping[shape]]
                if color not in output_1_colors:
                    output_1_colors[color] = shape
                for box in bboxes:
                    points_list = [(point[0], point[1]) for point in box]
                    points_list = tuple(points_list)
                    draw.polygon(points_list, fill=color)
            else:
                print('the shape is not included, please contact the developer')

    # draw output_2.jpg
    # Colors
    img_2 = Image.new("RGB", (3840, 2160), "black")
    cmap = ImageColor.colormap
    colors = random.sample(cmap.keys(), len(label_list))
    output_2_colors = {}
    draw = ImageDraw.Draw(img_2)
    for i, label in enumerate(label_list.keys()):
        color = colors[i]
        output_2_colors[color] = label
        bboxes_dict = label_list[label]
        for shape in bboxes_dict.keys():
            if shape == 'rect':
                bboxes = bboxes_dict[shape]
                for box in bboxes:
                    box = [box[0], box[3]]
                    points_list = [(point[0], point[1]) for point in box]
                    points_list = tuple(points_list)
                    draw.rectangle(points_list, fill=color)
            elif shape == 'line':
                bboxes = bboxes_dict[shape]
                for box in bboxes:
                    points_list = [(point[0], point[1]) for point in box]
                    points_list = tuple(points_list)
                    draw.line(points_list, fill=color)
            elif shape == 'polygon':
                bboxes = bboxes_dict[shape]
                for box in bboxes:
                    points_list = [(point[0], point[1]) for point in box]
                    points_list = tuple(points_list)
                    draw.polygon(points_list, fill=color)
            else:
                print('the shape is not included, please contact the developer')
    return img_1, img_2, output_1_colors, output_2_colors


def solution_1(data_path, save_path):
    start_time = time.time()
    print("-" * 65)
    print('Start Processing:')
    # load the dataset
    data = json.load(open(data_path))
    # create new save folder if not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # analyze the frequency of each label and each shape
    unique_shape_list, unique_label_list, unique_pair_list = label_analysis(data)
    print("-" * 65)
    print('There are {} unique shape types in the dataset with distribution as: {}'.format(len(unique_shape_list),
                                                                                           unique_shape_list))
    print("-" * 65)
    print('Frequency of each shape and all labels associated with the shapes is:')
    for pair in unique_pair_list:
        print("'{}' - '{}': {}".format(pair[0], pair[1], unique_pair_list[pair]))

    # visualize all the annotations in two different images
    # - output_1.jpg: Colors are based on shape types
    # - output_2.jpg: Colors are based on annotation label

    img_1, img_2, color_map_1, color_map_2 = visualize_annotations(data)
    print("-" * 65)
    print('color mapping of {}:'.format(os.path.join(save_path, 'output_1.jpg')))
    for item in color_map_1:
        print('{} - {}'.format(color_map_1[item], item))
    print("-" * 65)
    print('color mapping of {}:'.format(os.path.join(save_path, 'output_2.jpg')))
    for item in color_map_2:
        print('{} - {}'.format(color_map_2[item], item))
    img_1.save(os.path.join(save_path, 'output_1.jpg'))
    img_2.save(os.path.join(save_path, 'output_2.jpg'))

    # save results in a json file
    results = {
        'number of unique shape': len(unique_shape_list),
        'frequency of unique label-shape pair': {"'{}' - '{}'".format(key[0], key[1]): unique_pair_list[key] for key in
                                                 unique_pair_list.keys()},
        'color map for output1': color_map_1,
        'color map for output2': color_map_2,
    }
    with open(os.path.join(save_path, 'results.json'), 'w') as f:
        f.write(json.dumps(results))
    end_time = time.time()
    print("-" * 65)
    print('Finished the task in {} seconds'.format(end_time - start_time))
    print("-" * 65)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load necessary inputs for question 1.')

    parser.add_argument('--source', help='the path to the original json file', required=True)
    parser.add_argument('--save_path', default='./Question_1_Output', help='the path to the output folder')
    args = parser.parse_args()

    output_path = args.save_path
    annotation_path = args.source
    solution_1(annotation_path, output_path)
