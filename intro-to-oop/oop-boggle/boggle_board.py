import pandas as pd
import random
class BoggleBoard:
  DICE_OLD = []
  DICE_NEW = []
  DICE_FILES_DICT = { 'old': 'data/old_boggle.csv', 'new': 'data/new_boggle.csv' }
  
  def __init__(self, dice_type='new'):
    self.board = ['-'] * 16 
    self.dice_type = dice_type
    BoggleBoard.load_dice_from_csv(dice_type)

  # load dice faces from csv file
  @classmethod
  def load_dice_from_csv(cls, key='new'):
    filepath = cls.DICE_FILES_DICT[key]
    df = pd.read_csv(filepath)
    df_list = df['dice'].tolist()
    for row in df_list:
      if key == 'new':
        cls.DICE_NEW.append(list(row))
      else:
        cls.DICE_OLD.append(list(row))
  
  # shake dice and set the board
  def shake(self, key='new'):
    dice_order = list(range(16))
    random.shuffle(dice_order)
    for idx in dice_order:
      face = random.choice(list(range(6)))
      if key == 'new':
        self.board[idx] = BoggleBoard.DICE_NEW[idx][face]
      elif key == 'old':
        self.board[idx] = BoggleBoard.DICE_OLD[idx][face]

  # print formatting
  def __str__(self):
    ret_str = ''
    count = 0
    for i in range(16):
      letter = self.board[i]
      if letter == 'Q':
        ret_str += 'Qu  '
      else:
        ret_str += letter + '   '
      count += 1
      if count == 4:
        ret_str += '\n'
        count = 0
    return ret_str
  
  def __contains__(self, value):
    return value in self.board