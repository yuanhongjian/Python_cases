class scores():

    @classmethod
    def input_scores(cls):
        cls.name = input('Please tell me the name: ')
        cls.chinese_scores = int(input('Please tell me chinese scores: '))
        cls.math_scores = int(input("Please tell me math scores: "))

    @classmethod
    def print_scores(cls):
        print(cls.name + '的成绩单如下：')
        print('Chinese scores：'+ str(cls.chinese_scores))
        print('Math scores: ' + str(cls.math_scores))

    @classmethod
    def print_mean_scores(cls):
        cls.mean_scores = (cls.chinese_scores + cls.math_scores) / 2
        print("The mean score is: " + str(cls.mean_scores))

    @classmethod
    def rating(cls):
        if cls.mean_scores >= 90:
            print("Very good")
        elif cls.mean_scores >= 80:
            print("good")
        elif cls.mean_scores >= 60:
            print("Not bad")
        else:
            print("FAIL")

scores.input_scores()
scores.print_scores()
scores.print_mean_scores()
scores.rating()
