class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, cityQuestion, popQuestion):
        """Store a question, and prepare to store responses."""
        self.cityQuestion = cityQuestion
        self.popQuestion = popQuestion
        self.cityResponses = []
        self.popResponses = []
        
    def store_cityResponse(self, new_response):
        """Store a single response to the survey."""
        self.cityResponses.append(new_response)

    def store_popResponse(self, new_response):
        """Store a single response to the survey."""
        self.popResponses.append(new_response)
