# beads-nested-number-notation

👇 Tree structure  

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

👇 Bad variable names  

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

👇 I suggest. PascalCase  

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

The O looks like zero.  
The o looks like point.  

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
