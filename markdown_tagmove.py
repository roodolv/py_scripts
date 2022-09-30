#!/usr/bin/env python3
import re
import os
from pathlib import Path
# import fire

def moveTag(targetFilePath):
    reTag = re.compile(r"^#{1}[a-zA-Z0-9-_\/#\s,]*?$")

    with open(targetFilePath, "r", encoding="utf-8") as fi:
        lines = fi.readlines()

    matchedNum = -1
    for i in range(len(lines)):
        matchedLine = reTag.findall(lines[i])
        if (len(matchedLine) != 0) & (matchedNum == -1):
            matchedNum = i

    # print("見つかったタグ行:", matchedLine[0], "\n")
    # print("見つかったタグ行位置:", matchedNum, "\n")

    # ローカル保存とクラウド保存で共通の操作
    targetSplitPath = os.path.splitext(targetFilePath)

    # ローカルディレクトリに保存する場合
    targetFileName = targetSplitPath[0].split("\\")[-1]
    localDirPath = "D:\\Download\\temp_dev\\"
    targetCombinedPath = localDirPath + targetFileName + ".new" + targetSplitPath[1]

    # 直接元のクラウドに保存する場合(非推奨)
    # targetCombinedPath = targetSplitPath[0] + ".new" + targetSplitPath[1]

    # 正規表現がマッチしていないならファイル名表示してmain()に戻る
    if len(matchedLine) == 0:
        print(targetFileName)
        return

    # 書き込み用テキストを再構成する
    targetText = []
    for j in range(len(lines)):
        if (j != matchedNum) & (j != matchedNum - 1):
            # 2行目(配列添え字1)に取得したタグ行と改行を挿入する
            if j == 1:
                targetText.append(matchedLine[0] + "\n")
            targetText.append(lines[j])

    for t in range(len(targetText)):
        # 0行目だけ書き込みモード
        if t == 0:
            with open(targetCombinedPath, "w", encoding="utf-8") as fw:
                fw.write(targetText[t])
        # 1行目以降は追記モード
        else:
            with open(targetCombinedPath, "a", encoding="utf-8") as fa:
                fa.write(targetText[t])


def main():
    notedir = Path(r"E:\Dropbox\Obsidian\main\default")
    listNote = []

    for note in notedir.glob("**/*"):
        if ".new" not in os.path.splitext(note)[0]:
            listNote.append(note)

    for l in listNote:
        # print(l)
        moveTag(l)


if __name__ == "__main__":
    main()

# fire.Fire(main)
# You should input an argument on your terminal.
# (e.g.) 'PYTHON_BINARY_PATH markdown_tagmove.py FUNC_NAME'
# And then this script will call the function 'FUNC_NAME'.
