class Human:
    # コンストラクタの定義
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    # メソッドの定義
    def printinfo(self):
        print("私の名前は"+self.name+"です。")
        print("私の年齢は"+str(self.age)+"です。")
    
human = Human("侍太郎", 27)

human.printinfo()
