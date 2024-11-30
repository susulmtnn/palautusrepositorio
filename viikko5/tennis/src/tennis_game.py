class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        self.score = ""
        self.temp_score = 0

        def scores_equal():
            equal_score_list=["Love-All", "Fifteen-All", "Thirty-All"]
            if self.m_score1 in range(0, 3):
                self.score = equal_score_list[self.m_score1]
            else:
                self.score = "Deuce"

        def score_more_or_equal_to_four():
            minus_result = self.m_score1 - self. m_score2
            if minus_result>2:
                minus_result=2
            dicti={-1:"Advantage player2", 1:"Advantage player1", 2:"Win for player1"}
            if minus_result in dicti:
                self.score=dicti[minus_result]
            else:
                self.score="Win for player2"
        
        def temp_score_updater():
            temp_score_list=["Love", "Fifteen", "Thirty", "Forty"]
            for i in range(1,3):
                if i ==1:
                    self.temp_score=self.m_score1
                else:
                    self.score+= "-"
                    self.temp_score=self.m_score2
                self.score=self.score + temp_score_list[self.temp_score]


        if self.m_score1 == self.m_score2:
            scores_equal()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score_more_or_equal_to_four()
        else:
            temp_score_updater()
        return self.score
