from survey import AnonymousSurvey
import unittest

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
            """Create a survey and a set of responses for use in all test methods."""
            cityQuestion = "Enter 4 cities."
            popQuestion = "Enter their populations."
            self.my_survey = AnonymousSurvey(cityQuestion, popQuestion)
            self.cityResponses = ['Cary', 'Raleigh', 'Morrisville', 'Wake Forest']
            self.popResponses = ['300000', '500000', '100000', '200000']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_cityResponse(self.cityResponses[0])
        self.assertIn(self.cityResponses[0], self.my_survey.cityResponses)
        self.my_survey.store_popResponse(self.popResponses[0])
        self.assertIn(self.popResponses[0], self.my_survey.popResponses)

    def test_store_four_responses(self):
        """Test that four individual responses are stored properly."""
        for response in self.cityResponses:
            self.my_survey.store_cityResponse(response)
        for response in self.cityResponses:
            self.assertIn(response, self.my_survey.cityResponses)
        for response in self.popResponses:
            self.my_survey.store_popResponse(response)
        for reponse in self.popResponses:
            self.assertIn(response, self.my_survey.popResponses)

unittest.main()
