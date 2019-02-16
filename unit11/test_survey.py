import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    def setUp(self):
        """
        创建一个调查对象及一组答案，供使用的测试方法使用
        """
        question = 'what language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses=['English', 'Spnish', 'Chinese']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    
    def test_store_three_response(self):
     
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        
unittest.main()