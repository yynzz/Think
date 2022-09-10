import random

cash = 8000

#1.樂透號碼:開6個不重複數字介於1-49
def create_lot_num():
  lot_num = set()
  while len(lot_num)<6:
    lot_num.add(random.randint(1,49))
  return lot_num

#2.玩家買券:一張$50選6個數字
def buy_lot_ticket():
   global cash
   cash -= 50
   enter_num = input('Enter 6 numbers: ')
   enter_num_list = enter_num.split(',')
   ticket_num = {int(i) for i in enter_num_list}
   return ticket_num

#3.開獎:兌獎
def draw_result(ticket_num, lot_num):
  print('Winning numbers are {}'.format(lot_num))
  match_num = ticket_num.intersection(lot_num)
  prize_list = [0, 0, 10, 500, 3000, 50000, 100000000] #遊戲規則:中0個得0元,中6個得1億
  prize = prize_list[len(match_num)] #玩家中獎金額
  if prize > 0:
    global cash
    cash += prize
    return f'Congrats! You match {len(match_num)} numbers and win ${prize}!!!'
  else:
    return 'Better luck next time!'

#main
def run():
  while True:
    cmd = input('Welcome to YY Lottery Store. \nDo you want to [b]uy lottery ticket, [c]heck balance, or [l]eave?')
    if cmd == 'b':
      ticket_num = buy_lot_ticket()
      lot_num = create_lot_num()
      msg = draw_result(ticket_num, lot_num)
      print(msg)
    elif cmd == 'c':
      print(cash)
    elif cmd == 'l':
      break
      
if __name__ == '__main__':
    run()
