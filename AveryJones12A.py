# Create a program that reads a CSV file of student exam grades and calculates various statistics (mean, median, standard deviation, min, max) for each exam, and calculates pass/fail statistics.

import csv
import numpy as np


# Step 1: Load the data from the CSV file into a numpy array
def load_data_from_csv(file_name):
    data = []

    # Open the CSV file and read the data
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        # Read each row and append to the data list
        for row in reader:
            first_name, last_name, exam1, exam2, exam3 = row
            # Convert the exam grades to integers
            data.append([int(exam1), int(exam2), int(exam3)])

    # Convert the data list to a numpy array
    return np.array(data)


# Step 2: Calculate statistics for each exam
def calculate_exam_statistics(data):
    # Calculate mean, median, standard deviation, min, and max for each exam (columns)
    exam_stats = {
        'Mean': np.mean(data, axis=0),
        'Median': np.median(data, axis=0),
        'Standard Deviation': np.std(data, axis=0),
        'Minimum': np.min(data, axis=0),
        'Maximum': np.max(data, axis=0)
    }

    return exam_stats


# Step 3: Calculate overall statistics for all exams combined
def calculate_overall_statistics(data):
    # Flatten the data and calculate overall statistics
    all_grades = data.flatten()

    overall_stats = {
        'Mean': np.mean(all_grades),
        'Median': np.median(all_grades),
        'Standard Deviation': np.std(all_grades),
        'Minimum': np.min(all_grades),
        'Maximum': np.max(all_grades)
    }

    return overall_stats


# Step 4: Calculate pass/fail statistics for each exam
def calculate_pass_fail(data, passing_grade=60):
    pass_fail_stats = {
        'Passed Exam 1': np.sum(data[:, 0] >= passing_grade),
        'Failed Exam 1': np.sum(data[:, 0] < passing_grade),
        'Passed Exam 2': np.sum(data[:, 1] >= passing_grade),
        'Failed Exam 2': np.sum(data[:, 1] < passing_grade),
        'Passed Exam 3': np.sum(data[:, 2] >= passing_grade),
        'Failed Exam 3': np.sum(data[:, 2] < passing_grade)
    }

    return pass_fail_stats


# Step 5: Calculate overall pass percentage across all exams
def calculate_overall_pass_percentage(data, passing_grade=60):
    # Count the number of passing grades across all exams
    total_grades = data.size
    passed_grades = np.sum(data >= passing_grade)

    # Calculate the pass percentage
    pass_percentage = (passed_grades / total_grades) * 100
    return pass_percentage


# Main function to run the analysis
def main():
    # Load the data from grades.csv
    file_name = 'grades.csv'
    data = load_data_from_csv(file_name)

    # Step 2: Calculate statistics for each exam
    exam_stats = calculate_exam_statistics(data)
    print("Statistics for each exam:")
    print("Exam 1 - Mean:", exam_stats['Mean'][0], " Median:", exam_stats['Median'][0], " Standard Deviation:",
          exam_stats['Standard Deviation'][0], " Min:", exam_stats['Minimum'][0], " Max:", exam_stats['Maximum'][0])
    print("Exam 2 - Mean:", exam_stats['Mean'][1], " Median:", exam_stats['Median'][1], " Standard Deviation:",
          exam_stats['Standard Deviation'][1], " Min:", exam_stats['Minimum'][1], " Max:", exam_stats['Maximum'][1])
    print("Exam 3 - Mean:", exam_stats['Mean'][2], " Median:", exam_stats['Median'][2], " Standard Deviation:",
          exam_stats['Standard Deviation'][2], " Min:", exam_stats['Minimum'][2], " Max:", exam_stats['Maximum'][2])

    # Step 3: Calculate overall statistics across all exams
    overall_stats = calculate_overall_statistics(data)
    print("\nOverall Statistics for all exams combined:")
    print("Mean:", overall_stats['Mean'])
    print("Median:", overall_stats['Median'])
    print("Standard Deviation:", overall_stats['Standard Deviation'])
    print("Minimum:", overall_stats['Minimum'])
    print("Maximum:", overall_stats['Maximum'])

    # Step 4: Calculate pass/fail statistics for each exam
    pass_fail_stats = calculate_pass_fail(data)
    print("\nPass/Fail Statistics:")
    print(f"Passed Exam 1: {pass_fail_stats['Passed Exam 1']} | Failed Exam 1: {pass_fail_stats['Failed Exam 1']}")
    print(f"Passed Exam 2: {pass_fail_stats['Passed Exam 2']} | Failed Exam 2: {pass_fail_stats['Failed Exam 2']}")
    print(f"Passed Exam 3: {pass_fail_stats['Passed Exam 3']} | Failed Exam 3: {pass_fail_stats['Failed Exam 3']}")

    # Step 5: Calculate overall pass percentage across all exams
    overall_pass_percentage = calculate_overall_pass_percentage(data)
    print("\nOverall Pass Percentage across all exams:", '{:,.2f}'.format(overall_pass_percentage))


# Run the program
main()