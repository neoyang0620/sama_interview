# Sama Solutions Engineering Technical Excercise

At Sama we provide [training data](https://www.samasource.com/blog/2017/12/18/what-is-training-data) for computer vision models. Whether we're dealing with [image annotation applications](https://www.samasource.com/blog/2018/12/04/training-your-ai-in-3d), metrics to benchmark how well our services perform, or tools to help integrate customer data pipelines, reporting and working with images is part of our DNA.


## Exercise 1 (Architecture & Design)

We anticipate this exercise should take about a couple hours. We are more interested in your approach than perfection. 

Write a program in Python that ingests a json (sample-json.json), and generates the following output:

- Number of unique shape types
- Frequency of each shape and all labels associated with the shapes (for example: 'rectangle' - 'car': 74)
- Two different images generated from the data, where:
  - Colors are based on shape types
  - Colors are based on annotation label

Check the 3 sets of samples in Question_1_Example_Images for reference. The dimensions of the original image were 3840 × 2160.


## Exercise 2 (Code review and Bug fix)

The python script "Question_2.py" is used to identify corrupt images in a folder. The user reports that the script is running incorrectly, and they are not sure what is causing the error. The folder they are running the script on is "Question_2_Images". Given the python script and 1 sample corrupt image (indexed_5d5da9038aa716043cb777f4_0e2ee618-dab5-48c1-b13f-13ca3f8326e6.png), can you diagnose and fix the error(s)?


## General instructions

Please clone this repository and share the response with abha2 and sveta-sama.
