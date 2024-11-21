"""
Assignment:HW04
Student Name:Zhizhong Liu
Created Date:09/24/2024
"""

"""Excersice 7"""
def calculate_stats(numbers):
    """
    Goal:
    Calculate sum and the average of the list
    Return:
    A tuple included sum and the average of the list
    """

    total_sum = sum(numbers)
    """Avoid devide zero"""

    average = total_sum / len(numbers) if numbers else 0
    return total_sum, average


numbers_list = [10, 20, 30, 40, 50]
total_sum, average = calculate_stats(numbers_list)

"""Output"""
print(f"Total Sum: {total_sum}, Average: {average}")

"""Excersice 12"""

"""Word list"""
words = ["apple", "banana", "cherry", "date"]

"""using len() ti get word's length"""
word_lengths = [len(word) for word in words]
print(f"Word Lengths: {word_lengths}")

"use upper() to transfer to Upper case"
uppercase_words = [word.upper() for word in words]

"""Print Upper case word list"""
print(f"Uppercase Words: {uppercase_words}")
