import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point

'''
    〇百名山のCSVファイルをシェープファイルに変換する
'''

def main():
    print("<<===========================>>")
    print("source file: meizan_csv-to-shp.py")

    conv_dict = {"山名": "name", "標高（m）": "elevation", "北緯": "latitude", "東経": "longitude", "よみがな": "yomi", "所在地": "prefecture", "地域名": "region", "備考": "remarks"}
    df_merge = pd.DataFrame()

    for number in [100, 200, 300]:
        # CSV読み込み
        ifile = f"./input/{number:03d}meizan02.csv"
        df = pd.read_csv(ifile, sep=",")
        print(f"ifile: {ifile}")

        # データを整える
        df = df.rename(columns=conv_dict)
        df = df.drop(columns=['yomi', 'prefecture', 'region', 'remarks'])
        df_merge = pd.concat([df_merge, df])


    # シェープファイル書き出し
    df_merge["count"] = np.zeros(len(df_merge), dtype=np.int32)
    geometry = [Point(xy) for xy in zip(df_merge["longitude"], df_merge["latitude"])]
    geo_df = gpd.GeoDataFrame(df_merge, geometry=geometry)
    geo_df = geo_df.drop(columns=['latitude', 'longitude'])
    geo_df["count"] = np.zeros(len(geo_df))
    print(geo_df)
    ofile = f"./output/meizan02.shp"
    geo_df.to_file(driver='ESRI Shapefile', filename=ofile)
    print(f"ofile: {ofile}")


if __name__ == "__main__":
    main()