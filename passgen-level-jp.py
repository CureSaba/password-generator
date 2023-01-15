import random
keta=int(input("桁数: "))
level=int(input("Level: "))
kaisuu=int(input("回数: "))
kigou=[33,95,47,96,40,41,43,45,61,36,35,38,64,126]
#levelは0~3の範囲で指定する
#0は数字のみ
#1は数字と英語小文字
#2は数字と英語小文字大文字
#3は数字と英語小文字大文字と記号
level0=[]
for i in range(10):#forで1~10の数字をlevel0に挿入する
    level0.append(i)
level1=[]
level1.extend(level0)#level0の値をlevel1に追加する
for i in range(97, 123):#小文字のアルファベッット「a」はASCIIコードポイントの「97」、小文字の「z」は「122」なので、rangeコンストラクタの引数に「97」と「123」を指定して、97から122の整数を生成し、for文の中で組み込み関数chrの引数に、順番に指定する
    level1.append(chr(i))
level2=[]
level2.extend(level1)
for i in range(65, 91):#大文字のアルファベッット「A」はASCIIコードポイントの「65」、大文字の「Z」は「90」なので、rangeコンストラクタの引数に「65」と「91」を指定して、65から90の整数を生成し、for文の中で組み込み関数chrの引数に、順番に指定する
    level2.append(chr(i))
level3=[]#!_/`()+-=$#&@~が記号
level3.extend(level2)
for i in range(14):
    level3.append(chr(kigou[i]))#kigou内の数字を文字に変換して挿入する(文字で書くとバグってしまうため)
password=[]
for ewsdtf in range(kaisuu):
    for asdwrz in range(keta):
        if level==0:
            password.append(level0[random.randint(0,9)])#level0の0~9までの値をpasswordに追加する(計10個)
        if level==1:
            password.append(level1[random.randint(0,35)])#level1の0~35までの値をpasswordに追加する(計36個)
        if level==2:
            password.append(level2[random.randint(0,61)])#level2の0~61までの値をpasswordに追加する(計62個)
        if level==3:
            password.append(level3[random.randint(0,75)])#level3の0~75までの値をpasswordに追加する(計76個)
    password=str(password)#strに変換
    password=password.replace(", ", "")#, を削除(スペースに置き換え)
    password=password.replace("[", "")#[を削除(スペースに置き換え)
    password=password.replace("]", "")#]を削除(スペースに置き換え)
    password=password.replace("'", "")#'を削除(スペースに置き換え)
    print(password)
    password=[]#リセット
    
    #参考にさせていただいたサイト・ツール
    # 
    # https://www.relief.jp/docs/python-create-a-to-z.html
    # https://rakko.tools/tools/76/