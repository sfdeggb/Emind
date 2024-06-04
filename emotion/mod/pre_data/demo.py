import pickle
import pandas as pd


#查看
def lo():
    # 指定.pkl文件的路径
    file_path = '乐.pkl'

    # 使用pickle的load函数读取文件
    with open(file_path, 'rb') as file:  # 注意这里的模式是'rb'，表示以二进制读取
        loaded_object = pickle.load(file)

    # 打印或使用加载的对象
    print(loaded_object)

#数处理
def du():
    df = pd.read_excel('test.xlsx')
    # 初始化情感集合
    happy_words = set()
    good_words = set()
    sad_words = set()
    anger_words = set()
    neutral_words = set()
    fear_words = set()

    # 提取对应情感分类的词语
    for index, row in df.iterrows():
        if row['情感分类'] == 'PA':
            happy_words.add(row['词语'])
        elif row['情感分类'] == 'PD':
            good_words.add(row['词语'])
        elif row['情感分类'] == 'NA':
            sad_words.add(row['词语'])
        elif row['情感分类'] == 'NB':
            anger_words.add(row['词语'])
        elif row['情感分类'] == 'NI':
            neutral_words.add(row['词语'])
        elif row['情感分类'] == 'NE':
            fear_words.add(row['词语'])

    # 保存集合为.pkl文件
    with open('乐.pkl', 'wb') as f:
        pickle.dump(happy_words, f)

    with open('好.pkl', 'wb') as f:
        pickle.dump(good_words, f)

    with open('哀.pkl', 'wb') as f:
        pickle.dump(sad_words, f)

    with open('怒.pkl', 'wb') as f:
        pickle.dump(anger_words, f)

    with open('俱.pkl', 'wb') as f:
        pickle.dump(neutral_words, f)

    with open('惊.pkl', 'wb') as f:
        pickle.dump(fear_words, f)


# pkl文件中的快乐情感词汇集合
def load_words(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# 自主添加
def append_to_pkl(file_name, words_set):
    try:
        with open(file_name, 'rb') as f:
            existing_words = pickle.load(f)
    except FileNotFoundError:
        existing_words = set()

    merged_words = existing_words.union(words_set)

    with open(file_name, 'wb') as f:
        pickle.dump(merged_words, f)


if __name__ == '__main__':
    # du()
    lo()


