class AnonymousSurvey():
    """收集匿名问卷的答案"""
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到所有答案"""
        print('Survey results: ')
        for response in self.responses:
            print("_ " + response)
    