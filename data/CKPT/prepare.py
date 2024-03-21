from datasets import load_dataset

# 通过名称下载数据集
dataset = load_dataset("VatsaDev/ChatGpt-nano")

# 如果要指定版本，可以使用以下方式
# dataset = load_dataset("dataset_name", data_dir="path_to_data", download_mode="force_redownload")

# 使用数据集
print(dataset)
