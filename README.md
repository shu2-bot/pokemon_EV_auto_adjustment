# pokemon_EV_auto_adjustment

## 勉強したこと
### Django
- main.pyがインポートできなかった
  - pathを追加することで解決

- forms.Formもforms.ModelFormも速度に大差はない
  - DBに格納できるかどうか？

- forms.pyのcheckboxからPOSTで値を取得できない
  - choicefieldを使うことで解決

- 「python manage.py shell」でDBを操作できる
- python manage.py makemigrations アプリ名 で作成

### javascript
- jsでタブを閉じる関数が使えない
  - 動的に生成されたものでなく、ユーザーが自発的に開いたサイトは閉じられない

- js clonenodeから値を操作する方法は見つからなかった
  - 値の取得はできる

## メモ
smaple = Pokemon_status(pokemon_name="ピカチュウ", bs_h=35, bs_a=55, bs_b=40, bs_c=50, bs_d=50, bs_s=90, type1="electric", type2="None")

## 目標
- 短期的目標
  - ポケモンのデータベース作成
    - 新作に合わせたい
  - 攻撃・防御の実装
    - 条件を満たさない場合のエラー修正
  - 努力値の最適化
  - UIの確認
  - 比較ポケモンの追加機能
  - メールフォームの追加
  - 404以外のページの作成
  - XSS対策

- 長期的目標
  - 出力した調整を保存できるようにする？
    - そのためにはユーザー登録・ログインフォームが必要
  - 努力値調整をまとめるシステムとかもあり
    - メモ付きで、どのポケモンに立ち回れたかとか
