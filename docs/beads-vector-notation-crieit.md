👇 入れ子番号を見かけることはある  

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

入れ子番号を加味して変数名を付けたいときに悩むことがある。  
👇 このような変数名はイケてない  

```plaintext
1Food
1_1Fruit
1_1_1Apple
1_1_2Banana
2Vehicle
2_1Ship
2_2Train
2_3Car
2_3_1PoliceCar
```

数字から始まる変数名を付けられないことはよくあるし、  
入れ子番号をアンダースコアでつなぐと　スネークケースのとき区切りが多くなったり、  
そもそも　パスカルケース　と決められていれば　アンダースコアが使えない  

あなたは `0` と `O` が視認しづらいとか、 `.` と `o` は点の大きさがだいぶ違うとか、  
**美的違和感** や　いくつもの不完全さを許容して この悩みを解決するか、それとも このまま  
悩み続けるか 好きな方を選ぶことができる  

👇 PascalCase  

```plaintext
O1Food
O1o1Fruit
O1o1o1Apple
O1o1o2Banana
O2Vehicle
O2o1Ship
O2o2Train
O2o3Car
O2o3o1PoliceCar
```

👇 lowerCamelCase  

```plaintext
o1Food
o1o1Fruit
o1o1o1Apple
o1o1o2Banana
o2Vehicle
o2o1Ship
o2o2Train
o2o3Car
o2o3o1PoliceCar
```

👇 snake_case

```plaintext
o1_food
o1o1_fruit
o1o1o1_apple
o1o1o2_banana
o2_vehicle
o2o1_ship
o2o2_train
o2o3_car
o2o3o1_police_car
```

👇 kebab-case

```plaintext
o1-food
o1o1-fruit
o1o1o1-apple
o1o1o2-banana
o2-vehicle
o2o1-ship
o2o2-train
o2o3-car
o2o3o1-police-car
```

Example: 📖 [beads-nested-number-notation](https://github.com/muzudho/beads-nested-number-notation)  

# 関連する記事

📖 [辞書順記数法](https://crieit.net/posts/Dictionary-Ordinal-Number-Notation) - 組み合わせて使える  
📖 [電脳記数法](https://crieit.net/posts/Cyber-Number-Notation) - 辞書順記数法と 数珠玉記数法を組み合わせたもの