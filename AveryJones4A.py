# Create a program that has a user enter an email and determines its spam likelihood by checking a list of common spam
# words and phrases

import time
import re

def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2 - t1)
        return ret_val
    return wrapper

def count_nums(n):
    for i in range(n):
        for j in range(1000):
            pass
count_nums = make_timer(count_nums)

# Create a list of common occurring spam words and phrases
spam_keywords = [
    "free", "100% free", "additional income", "be your own boss", "cash bonus", "consolidate debt", "earn money",
    "eliminate bad credit", "extra credit", "no fees", "free gift", "free access", "free hosting", "free preview",
    "full refund", "giveaway", "get paid", "lower rates", "lowest price", "apply now", "act now", "instant",
    "dont delete", "this won't last", "winner", "you have been selected", "no catch", "passwords", "weight loss", "debt"
]

# Create a function to calculate the spam score of the user imputed email (count the number of spam words/phrases)
def calc_spam_score(email):
    score = 0
    found_keywords = []

    # for every keyword from the list found in the email add 1 to the score count
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', email, re.IGNORECASE):
            score += 1
            found_keywords.append(keyword)

    return score, found_keywords

# Using the score determine the spam likelihood of the email being spam
def determine_spam_likelihood(score):
    if score >= 20:
        return "Very Likely"
    elif score >= 15:
        return "likely"
    elif score >= 10:
        return "Somewhat Likely"
    elif score >= 5:
        return "Unlikely"
    else:
        return "Very Unlikely"

# Create an Email function that has the user input an email and creates the calc_spam_score and determine_spam_likelihood
# functions
def Email():
    user_email = input("Enter email message: ")

    spam_score, found_keywords = calc_spam_score(user_email)

    spam_likelihood = determine_spam_likelihood(spam_score)

    print(f"\n Spam Score: {spam_score}")
    print(f"Likelihood that the message is spam: {spam_likelihood}")
    if found_keywords:
        print("keywords/Phrases found: ")
        for keyword in found_keywords:
            print(f" - {keyword}")
    else:
        print("No Spam keywords/phrases detected.")

# Run the program
Email()
count_nums(33000)