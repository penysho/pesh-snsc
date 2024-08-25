# pesh-snsc

各SNSとの連携管理アプリケーションのプロジェクト、APIは[pesh-snsc-api](https://github.com/penysho/pesh-snsc-api)で別途管理する

## 使用技術一覧

<p style="display: inline">
 <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
 <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
 <img src="https://img.shields.io/badge/-Docker-1488C6.svg?logo=docker&style=for-the-badge">
 <img src="https://img.shields.io/badge/-TailwindCSS-000000.svg?logo=tailwindcss&style=for-the-badge">
</p>

## アーキテクチャ

* DjangoのMTVに、Service層とRepository層を追加した構成とする

<https://docs.djangoproject.com/en/5.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names>

### Service

* ビジネスロジックを実行する

### Repository

* データの永続化を実行する

### 言語

* Python(3.12.x)

### フレームワーク/ライブラリ

* Django(5.0.4)をコアとしてWebアプリケーションを構成する
* 一覧とバージョンは[requirements.txt](requirements.txt)を参照する

## 実行

本アプリケーションの実行方法を記載する

### 手順

* プロジェクト直下に`.env`を作成する、[環境変数一覧](#環境変数一覧)を参考にすること
* プロジェクトルートで`docker compose up`

### 環境変数一覧

| 変数名 | 説明 | デフォルト値 |
| - | - | - |
| DEBUG | djangoのデバッグ設定(真偽値) | |
| ALLOWED_HOSTS | アプリケーションを起動するサーバーのホスト名やIPのリスト(カンマ区切り) | |
| SECRET_KEY | djangoで使用する秘密鍵 | |
| DATABASE_URL | [django-environment](https://django-environ.readthedocs.io/en/latest/types.html#environ-env-db-url)で読み込み可能なDBのURL | |
