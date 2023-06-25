import pandas as pd
from bs4 import BeautifulSoup
def convert_html_to_table(html_file):
    # HTMLファイルから表を抽出
    with open(html_file, "r", encoding="utf-8") as f:
        html_data = f.read()
        soup = BeautifulSoup(html_data, "html.parser")
        table = soup.find("table")
    if not table:
        print("表が見つかりませんでした:", html_file)
        return
    # 表をDataFrameに変換
    df = pd.read_html(str(table))[0]
    # 出力ファイル名を生成
    base_name = html_file.replace(".html", "")
    text_output_file = base_name + ".txt"
    csv_output_file = base_name + ".csv"
    # DataFrameをテキストファイルに出力
    df.to_csv(text_output_file, sep="\t", index=False)
    # DataFrameをCSVファイルに出力
    df.to_csv(csv_output_file, index=False, encoding="utf-8-sig")
    # print("テキストファイルに出力しました:", text_output_file)
    # print("CSVファイルに出力しました:", csv_output_file)
def convert_html_files_to_text_and_csv(files_list_file):
    # ファイル名のリストをテキストファイルから読み込む
    with open(files_list_file, "r", encoding="utf-8") as f:
        files_list = f.read().splitlines()
    # 各ファイルを処理する
    for html_file in files_list:
        convert_html_to_table(html_file)
# ファイル名リストを指定してHTMLファイルを処理
if __name__ == "__main__":
    files_list_file = ".\\files_list.txt"
    convert_html_files_to_text_and_csv(files_list_file)