from class_bucket import Bucket
from class_fisher import Fisher
from class_pond import Pond


print('Привет! Добро пожаловать на рыбалку!')
choice = input("Чтобы начать ловить рыбу нажмите 'y'\n"
               "Если вы хотите завершить рыбалку, нажмите 'n'\n")

if choice == 'n':
    print('Очень жаль. Приходите к нам еще!')
if choice == 'y':
    print('Ловись рыбка большая и маленькая...')
    pond = Pond()
    pond.create_shoal()
    bucket = Bucket()
    fisher = Fisher(bucket)
    zero_list = bucket.make_thread(pond.fish_list)
    pond.fish_list = zero_list
    print(pond.fish_list)
    bucket.get_fish_amount()
    print(f'Отлично! У вас в ведерке {bucket.fish_amount} рыбок! Вы выловили всех!\n'
          f'Спасибо за рыбалку и удачи вам!')

