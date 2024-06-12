"""
Level 8 Final Exersice: Customer Support Chat Log Analysis

Objective

You've been hired by and e-commerce company to analyze their customer support chat. They want you to create a tool that summarizes the types of cupport issues raised by customers.
The tool should also allow for keys searches with the logs.

Introduction:

1.  Create a function categorize_issues that takes the chat_logs list return disctionary categorizing the issued by type.
2.  Create a function keyword_search that takes a keyword and the chat_logs list and return all messages containing the keyword, ignoring case.
3.  Display the categorized issues and allow the user to perform keyword searches.


"""

chat_logs = [
    "my order is delayed",
    "I want to return my purchase",
    "The app is crushing frequently",
    "Payment issues, please help",
    "Need help with account recovery",
    "Delivery was incomplete",
    "Can't login to my account",
    "Having trouble with checkout"
]
print(type(chat_logs))
chat_logs = str(chat_logs)

categories = {'Order': 0, "App": 0,"Payment": 0,"Account": 0, "Delivery": 0}


def categorize_issues(chat_log):
    for log in chat_log:
        log_lower = log.lower()
        for category in categories.keys():

            if category.lower() in log.lower():
                categories[category] +=1


def keyword_search(keyword, logs):
    keyword = keyword.lower()
    results = []
    for log in logs:
        if keyword in log.lower():
            results.append(log)
    return results



print(categories)
categorize_issues(chat_logs)
print(categories)
print(categories)

keyword = input('Enter the search keyword: ')
print(keyword_search(keyword,chat_logs))

#
#
# def categorize_issues(chat_logs):
#     categories = {'Order': 0, "App": 0, "Payment": 0, "Account": 0, "Delivery": 0}
#
#     for log in chat_logs:
#         if "order" in log.lower():
#             categories['Order'] += 1
#         if "app" in log.lower():
#             categories['App'] += 1
#         if "payment" in log.lower():
#             categories['Payment'] += 1
#         if "account" in log.lower():
#             categories['Account'] += 1
#         if "delivery" in log.lower():
#             categories['Delivery'] += 1
#
#     return categories
#
#
# def keyword_search(chat_logs, keyword):
#     matching_logs = [log for log in chat_logs if keyword.lower() in log.lower()]
#     return matching_logs
#
# # Categorize issues
# categories = categorize_issues(chat_logs)
# print("Categorized Issues:")
# for category, count in categories.items():
#     print(f"{category}: {count}")
#
# # Perform keyword search
# search_word = "app"
# matching_logs = keyword_search(chat_logs, search_word)
# print(f"\nLogs containing '{search_word}':")
# for log in matching_logs:
#     print(log)
