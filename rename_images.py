from PIL import Image
import os
import pandas as pd

# "file_name.csv"ファイルを読み込む
df = pd.read_csv("file_name.csv")

# imgフォルダのパスを取得する
img_dir = "./img"

# imgフォルダ内の全てのファイル名と更新日を取得する
file_info_list = [(f, os.path.getmtime(os.path.join(img_dir, f))) for f in os.listdir(img_dir)]

# 更新日が古い順にファイル名をソートする
sorted_file_info_list = sorted(file_info_list, key=lambda x: x[1])

# 画像を読み込んで名前を置換する
for i, (file_name, _) in enumerate(sorted_file_info_list):
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        image_path = os.path.join(img_dir, file_name)
        image = Image.open(image_path)

        # "name.csv"ファイルから名前を取得する
        name = df.iloc[i]["name"]

        # 画像の名前を置換する
        new_file_name = f"{name}.jpg" # 例えば、拡張子を.jpgに統一する場合
        new_image_path = os.path.join(img_dir, new_file_name)
        os.rename(image_path, new_image_path)
