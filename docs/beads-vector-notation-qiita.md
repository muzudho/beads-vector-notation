一度に説明しても簡単だが、要点を分けて１つずつ説明する  

# 数珠玉表記の代表的な例

👇 以下のような表記があるとする  

```plaintext
128.0.0.1
```

👇 `.` を `o` に変換する  

```plaintext
128o0o0o1
```

これが 数珠玉表記 だ  

# もととなる符号化の考え方

以下のように対応する

| 演算優先順位 | 置換前 | 置換後 |
| -----------: | ------ | ------ |
|            1 | `;`    | `j`    |
|            2 | `:`    | `i`    |
|            3 | `(`    | `q`    |
|            3 | `)`    | `p`    |
|            4 | `,`    | `g`    |
|            5 | `*`    | `x`    |
|            5 | `/`    | `y`    |
|            6 | `+`    | `t`    |
|            6 | `-`    | `n`    |
|            7 | `.`    | `o`    |
|            8 | ` `    | `u`    |

（演算順）  

数珠玉表記では基本的に `o` だけ使う。 このPythonパッケージでは `o` をサポートする。  
拡張で `q`, `p`, `g` が必要になってくるケースがあるかもしれない  

## 備考

* 大文字，小文字は区別しない（Ignore case）

# 数珠玉表記 の格納構造

タプルを使う  

👇 以下のような数珠玉表記があるとする  

```plaintext
-21o-1o0o1o21
```

👇 大文字に揃える  

```plaintext
-21O-1O0O1O21
```

👇 `O` でスプリットする  

```plaintext
[-21, -1, 0, 1, 21]
```

👇 タプルに変換する  

```plaintext
(-21, -1, 0, 1, 21)
```

# 複数のベクトルを 数珠玉表記 に変換する手順

👇 複数のベクトルがあるとする  

```plaintext
[2 1] [4 3]
```

👇 各ベクトルの要素は `.` 区切りにする。間隔は詰める  

```plaintext
[2.1] [4.3]
```

* これにより，数珠玉表記では小数を扱えない  

👇 ベクトル間は `,` 区切りにする。間隔は詰める  

```plaintext
[2.1],[4.3]
```

👇 角かっこは、丸かっこへ置換する  

```plaintext
(2.1),(4.3)
```

👇 ここで、`.` より `,` は優先順位が高いことから、丸かっこは外せる。だから外す  

```plaintext
2.1,4.3
```

👇 以下の置換ルールを適用する  

* `,` は `g` へ  
* `.` は `o` へ

```plaintext
2o1g4o3
```

これが 数珠玉表記 だ  

## 備考

* 整数とベクトルの結合でも同様

# 関連する記事

## 辞書順記数法

👇 組み合わせて使える

📖 [辞書順記数法 Crieit版](https://crieit.net/posts/Dictionary-Ordinal-Number-Notation) - ブログ  
📖 [辞書順記数法 Qiita版](https://qiita.com/muzudho1/items/95852145eceddecd1503) - 固い記事  

## 数珠玉表記

📖 [数珠玉表記 Crieit版](https://crieit.net/posts/Beads-Nested-Number-Notation) - ブログ  
📖 `数珠玉表記 Qiita版` - この記事

## 電脳向量表記

👇 辞書順記数法と 数珠玉記数法を組み合わせたもの  

📖 [電脳向量表記 Crieit版 ブログ](https://crieit.net/posts/Cyber-Number) - ブログ  
📖 [電脳向量表記 Crieit版](https://crieit.net/posts/Cyber-Number-Notation) - 固い記事  

## Pythonコード

Example: 📖 [beads-vector-notation](https://github.com/muzudho/beads-vector-notation)  
