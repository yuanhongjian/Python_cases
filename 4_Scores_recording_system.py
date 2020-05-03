class scores():

    @classmethod
    def input_scores(self):
        self.name = input('Please tell me the name: ')
        self.chinese_scores = int(input('Please tell me chinese scores: '))
        self.math_scores = int(input("Please tell me math scores: "))

    @classmethod
    def print_scores(self):
        print(self.name + '的成绩单如下：')
        print('Chinese scores：'+ str(self.chinese_scores))
        print('Math scores: ' + str(self.math_scores))

    @classmethod
    def print_mean_scores(self):
        self.mean_scores = (self.chinese_scores + self.math_scores) / 2
        print("The mean score is: " + str(self.mean_scores))

    @classmethod
    def rating(self):
        if self.mean_scores >= 90:
            print("Very good")
        elif self.mean_scores >= 80:
            print("good")
        elif self.mean_scores >= 60:
            print("Not bad")
        else:
            print("FAIL")

scores.input_scores()
scores.print_scores()
scores.print_mean_scores()
scores.rating()