# 爬蟲相關庫

這個專案包含了一些用於網頁爬蟲的實用工具和類別。

## 主要功能

1. `Bug` 類別：用於設置和管理爬蟲請求。
2. 檔案下載：支援從網頁下載檔案。
3. Excel 輸出：可將爬取的數據輸出為 Excel 檔案。
4. 環境變數管理：安全地獲取環境變數。
5. 鏈接檢查：驗證 URL 的有效性。

## 安裝指南

1. 確保您的系統已安裝 Python 3.6 或更高版本。

2. 使用 pip 安裝套件：

```shell
pip install hsuBug
```

## 使用示例

### 基本爬蟲設置

```python
from hsuBug import Bug

# 創建 Bug 實例
url = "https://example.com"
bug = Bug(url)

# 設置請求頭
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 設置並獲取網頁內容
bug.setup(headers)

# 現在您可以使用 bug.soup 來解析 HTML 內容
```

### 下載檔案

```python
from hsuBug.functions import downloadFile

url = "https://example.com/file.pdf"
filename = "example.pdf"
downloaded_file = downloadFile(url, filename)
print(f"檔案下載至：{downloaded_file}")
```

### 輸出到 Excel

```python
from hsuBug.functions import downloadByExcel

data = {
    "名稱": ["項目1", "項目2", "項目3"],
    "價格": [100, 200, 300]
}

df = downloadByExcel(data)
if df is not None:
    print("數據已成功輸出到 Excel 檔案")
```

### 檢查鏈接有效性

```python
from hsuBug.functions import checkLink

url = "https://example.com"
if checkLink(url):
    print("鏈接有效")
else:
    print("鏈接無效")
```

## 單元測試

```shell
python -m unittest test_hsuBug.py
```

## 發布

```shell
python setup.py sdist
twine upload dist/*
```

## 未來功能

1. aiohttp 版本

## 許可證

[MIT](https://choosealicense.com/licenses/mit/)