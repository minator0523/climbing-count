# ○○名山のCSVをSQLに変換

## 1. CSVファイルをまとめてシェープファイルに変換
```
$ cd ./csv-to-shp/
$ python meizan_csv-to-shp.py
```
* 変換前のファイル
  * `./input/100meizan02.csv`
  * `./input/200meizan02.csv`
  * `./input/300meizan02.csv`
* 変換後のファイル
  * .`/output/meizan02.shp`
  * `./output/meizan02.cpg`
  * `./output/meizan02.shx`
  * `./output/meizan02.dbf`

## 2. シェープファイルをSQLに変換
### 2.1 gdal用のコンテナを起動
```
$ cd ./shp-to-sql
$ docker compose up -d
```
### 2.2 コンテナのシェルに入る
```
$ docker exec -it gdal /bin/bash
```
### 2.3 gdalを使いシェープファイルからSQLに変換
```
root@gdal:/# ogr2ogr -f "PGDump" /output/meizan02.sql -nln meizan -lco GEOMETRY_NAME=geom /input/meizan02.shp
```
* 変換前のファイル：
  * `./input/meizan02.cpg`
  * `./input/meizan02.dbf`
  * `./input/meizan02.shp`
  * `./input/meizan02.shx`
* 変換後のファイル：
  * `./output/meizan02.sql`