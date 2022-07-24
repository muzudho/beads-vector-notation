![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　👇 プログラム設計書が 入れ子番号になってら……」  

```plaintext
1. Food

1.1. Fruits

1.1.1. Apple

1.1.2. Banana

2. Vehicle

2.1. Ship

2.2. Train

2.3. Car

2.3.1. Police car
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dcca56eb0f2.png)  
「　伝説の BASIC言語 の教えを知らないから 人は連番にする」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　今日の仕事を終え、続きは明日にするぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　次の日だぜ。　今日の業務を開始するぜ」  

```plaintext
1. House

1.1 Apart

1.2 Mansion

2. Food

2.1. Fruits

2.1.1. Apple

2.1.2. Banana

3. Vehicle

3.1. Ship

3.2. Train

3.3. Car

3.3.1. Police car
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　👆 振り番が変わってる……」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762dccbaa15edf.png)  
「　文書は　どんどん成長するのよ。　そのたびに **リナンバリング** するわよ！」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　よっしゃ　プログラム設計書の振り番と　プログラムのソースコードのファイル名の新旧対応表を作ったろ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dcca56eb0f2.png)  
「　そんな表を作る工数が無駄なのに……」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　👇 こういうクラス名を付けたいが、名前を数字で始めることはできないし、アンダースコアも コード規約的によろしくないぜ」  

```plaintext
1House
1_1Apart
1_2Mansion
2Food
2_1Fruit
2_1_1Apple
2_1_2Banana
3Vehicle
3_1Ship
3_2Train
3_3Car
3_3_1PoliceCar
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762dccbaa15edf.png)  
「　プログラムに連番を振るのは **アンチパターン** よ。  
**プログラムの意味** を洗い出せば、その部品に合った名前が自ずと付くのよ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　設計者は **政治的理由** で 意味を洗い出すことを止めてるんで」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dcca56eb0f2.png)  
「　政治的でない部分だけで　プログラムしようぜ？」  

```plaintext
O1House
O1_1Apart
O1_2Mansion
O2Food
O2_1Fruit
O2_1_1Apple
O2_1_2Banana
O3Vehicle
O3_1Ship
O3_2Train
O3_3Car
O3_3_1PoliceCar
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　👆 前ゼロに似てるという理由で 大文字の `O` を頭に付けたろ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dcca56eb0f2.png)  
「　経営幹部は ソースに興味ないしな」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762dccbaa15edf.png)  
「　ソースのモデラ―（管理者）がいないの　そもそもおかしいのよ」  

```plaintext
O1House
O1o1Apart
O1o2Mansion
O2Food
O2o1Fruit
O2o1o1Apple
O2o1o2Banana
O3Vehicle
O3o1Ship
O3o2Train
O3o3Car
O3o3o1PoliceCar
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　👆 アンダースコア `_` は、数字のゼロに似ている小文字の `o` に替えたろ。  
これで　章番号を　クラス名の頭に付ける道具立ては整ったぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dcca56eb0f2.png)  
「　驚き最大限の法則わらう」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　👇 lowerCamelCase としても使える。変数名にも使えそうだぜ」  

```plaintext
o1House
o1o1Apart
o1o2Mansion
o2Food
o2o1Fruit
o2o1o1Apple
o2o1o2Banana
o3Vehicle
o3o1Ship
o3o2Train
o3o3Car
o3o3o1PoliceCar
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dcca0f35df1.png)  
「　これを **数珠玉表記** （Beads Vector Notation） と名付けよ」  

# 関連する記事

## 辞書順記数法

組み合わせて使える  

📖 [辞書順記数法 Crieit版](https://crieit.net/posts/Dictionary-Ordinal-Number-Notation) - ブログ  
📖 [辞書順記数法 Qiita版](https://qiita.com/muzudho1/items/95852145eceddecd1503) - 固い記事  

## 数珠玉表記

📖 **数珠玉表記 Crieit版** - この記事
📖 [数珠玉表記 Qiita版](https://qiita.com/muzudho1/items/7aafcf17fc4bb8fe551b) - 固い記事

## 電脳向量表記

辞書順記数法と 数珠玉表記を組み合わせたもの  

📖 [電脳向量表記 Crieit版 ブログ](https://crieit.net/posts/Cyber-Number) - ブログ
📖 [電脳向量表記 Crieit版 固い記事](https://crieit.net/posts/Cyber-Number-Notation) - 固い記事  

## Pythonコード

Example: 📖 [beads-vector-notation](https://github.com/muzudho/beads-vector-notation)