class GameOver(Exception):
  

    def __init__(self, some_obj):
        super().__init__()
        self.pl_name = str(some_obj.pl_name)
        self.pl_score = str(some_obj.score)


class EnemyDown(Exception):
    
    #class EnemyDown. Needed for implement enemy dying
    