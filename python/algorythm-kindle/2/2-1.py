"""配列の必要性"""
# 配列の必要性

# 例えば次の例を考える
# 学生のテスト結果の集計をする。人数は5人。合計と平均点を求めるプログラムを実装する。
# tensu1 = int(input("1番の点数:"))
# tensu2 = int(input("2番の点数:"))
# tensu3 = int(input("3番の点数:"))
# tensu4 = int(input("4番の点数:"))
# tensu5 = int(input("5番の点数:"))

# total = 0
# total += tensu1
# total += tensu2
# total += tensu3
# total += tensu4
# total += tensu5

# print(f"合計は{total}点です")
# print(f"平均は{total / 5}点です")

# ここで、以下の機能をさらに実装したい
# ①人数を可変にする
# ②特定の学生の点数を調べる/書き換える
# ③最低点/最高点を求める/ソートする

# 結論無理
# 配列にして各要素をひとまとめにする必要がある、なお配列内の各要素の型がそろう必要はない

"""リストとタプル"""
# どちらも高機能なデータのコンテナ（格納庫）

# リスト

# ミュータブル（変更可能）なlist型のオブジェクト　　　豆：最後の要素の後にも,が置けるなぜかはわからない
# 組み込み関数のlist()を使うことで様々な型のオブジェクトをもとに配列を生成できる 様々といったが正確にはイテラブルを取れる
print(list((1,3))) # 数字から配列を
print(list((1,2,"3"))) # 数値と文字列から配列を

# 要素数が決まっているものの要素の値は未定、といった場合のリスト生成の決まり文句があります。Noneで生成することです
print([None] * 5) # [None] , [None], ...となるわけでないので注意しっかり覚えておこう

# タプル

# 要素を順序付けて組み合わせたもの
# 式結合演算子()で囲む　なお文脈上の曖昧さｎがなければ()は省略できる

# 注意：要素が1個の場合は末尾に,をつける出ないと単一の値とみなされる
print(1)
print(1,) # あれこれ変だな FIXME
print((1,))

# アンパック

# リストやタプルの各要素をばらばらにして何かに代入したりする操作

# アクセス方法

# インデックスとスライス

# インデックス
# イテラブルオブジェクト.[インデックス番号]でアクセスする、なお変更も可能

# スライス
# 注意点として未満ね、あと3津引数の場合最後のは何個飛ばしでやるか,2なら1個飛ばし3なら2こ飛ばし
# インデックスアクセスと違い、len(list)分を超えてもエラーとならない
list1 = [1,2,3,4,5]
print(list1[:100:1]) # 1個飛ばしなのでまぁいらんけど解説のため
# -1で最後の要素-2に最後から2番目の要素というアクセスの仕方もできる

# 個人的な参照実験　コラム2-1要
a = 111
b = 111
print(f"aのID:{id(a)}") # 同じ
print(f"bのID:{id(b)}") # 同じ

"""データ構造"""

# 以下のような配列の各要素を順になぞっていく手続きのことを走査という
ls = [1,2,44,66,32,8,100]
def max_e_of(ls):
    maximum = ls[0]
    for i in range(len(ls)):
        if maximum <= ls[i]:
            maximum = ls[i]
    print(maximum)
max_e_of(ls)