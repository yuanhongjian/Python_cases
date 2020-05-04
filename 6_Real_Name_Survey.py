class RealNameSurvey():
    def __init__(self, question):
        self.question = question
        self.response = {}
        self.show_question()
        self.store_response()

    # show the question
    def show_question(self):
        print(self.question)

    # store the responses
    def store_response(self):
        while True:
            self.new_response = input("Please answer the question or enter 'q' to quit： ")
            if self.new_response == "q":
                for key, value in self.response.items():
                    print(key + ": " + value)
                break
            else:
                self.name = input("Please enter the name of the respondent：")
                self.response[self.name] = self.new_response


survey = RealNameSurvey('Where is your birth place? ')