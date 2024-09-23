class Human:
    # コンストラクタの定義
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # check_adultメソッドを定義する
    def check_adult(self):
        # 年齢が20歳未満か判断
        if self.age < 20:
            print(self.name+"は大人ではありません。") # 20歳未満の場合は大人でない
        else:
            print(self.name+"は大人です。") # 20歳以上の場合は大人である
           
# 4人の名前と年齢のリストを作成 
humans_info = [{"name":"侍太郎", "age":20},
          {"name":"侍花子", "age": 18},
          {"name":"寺子屋次郎", "age":5},
          {"name":"寺子屋菊", "age":27}
          ]

# 4人のオブジェクトを格納するリスト（1-indexedにするために""を追加)
humans = [""]

# 4人の情報をもとにオブジェクトを作成
for human in humans_info:
    humans.append(Human(human["name"],human["age"]))

# カウンタ 
i = 1

#　カウンタが人数に一致するまで繰り返し処理を行う 
while i != len(humans):
    # i番目の人が大人かどうか判定
    humans[i].check_adult()
    # 番号を1増やす
    i += 1