# VRCamera

## これは何？
Raspberry Pi のカメラ映像を
[Google Cardboard](https://arvr.google.com/intl/ja_jp/cardboard/)
のようなアイテムで使用できる形式に変換するためのプログラム（予定）です。

## タスクリスト

- [X] カメラ映像を取得する
- [X] カメラ映像を複製し、横に連結する
- [ ] 処理後のカメラ映像をネットワーク経由で送信できるようにする
- [ ] 送信する映像に最適なエフェクトをかける
- [ ] 送信する映像の縦横比を任意に設定できるようにする
- [ ] Ubuntu20.04での動作確認を行う


## 将来的にやりたいこと

- こちらで処理した映像を[WebRTC Native Client Momo](https://github.com/shiguredo/momo)を使用して送信できるようにしたい
- ROSのNodeとして組み込みたい
- C++ で再実装したい


## 開発環境

|   |   |
|---|---|
|機種 |Raspberry Pi 4 Model B 4GB |
|OS |Raspbian Buster Lite |
|カメラモジュール |[Raspberry Pi Camera for 3B/2B/B+/A+/B/A](https://www.amazon.co.jp/gp/product/B01AUN1JUG/ref=ppx_yo_dt_b_asin_title_o09_s00) |