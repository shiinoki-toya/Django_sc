from django.db import models
from django.db import connection
# # モデル読込
# from django.db import model

# # モデルクラスを作成
# class People(models.Model):
# 	# 項目定義
#     Name     = models.CharField(max_length=100)           # 文字列
#     Tell     = models.IntegerField(blank=True, null=True) # 整数
#     Mail     = models.EmailField(max_length=100)          # Email
#     Birthday = models.DateField()                         # 日付
#     Website  = models.URLField()                          # URL
#     FreeText = models.TextField()                         # フリーテキスト

#     # テキスト表示
#     def __str__(self):
#     	return self.name

class Sample(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


def db_select():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM persons')
        #cursor.execute('INSERT INTO sc_app_sample(title,text) values("インサート","する")')
        #cursor.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING,text STRING)')
        #cursor.execute('INSERT INTO persons(name,text) values("Sato","です")')
        #cursor.execute('INSERT INTO persons(name,text) values("Suzuki","ます")')
        #cursor.execute('INSERT INTO persons(name,text) values("Takahashi","であります")')
        row = cursor.fetchall()
        # print(row)
        cursor.close()
        return row