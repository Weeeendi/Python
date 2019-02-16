from survey import AnonymousSurvey

"""定义一个问题，并创建一个表示调查的AnonymouSurvey对象"""
question = "what language did you first learn to speak?"
my_servey = AnonymousSurvey(question)

#show the question and stored the question
my_servey.show_question()
print("Enter 'q' at any time to quit\n ")
while True:
     reponse = input("language: ")
     if reponse == 'q':
        break
     my_servey.store_response(reponse)

# show results
print("\n Thank you to everyone who praticipated in the survey!")
my_servey.show_results()
