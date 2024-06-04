import nltk.classify as cf
import nltk.classify.util as cu
import jieba
#from snownlp import SnowNLP
import jieba
import pickle
import pathlib
import re

class QEmo(object):
    def __init__(self):
        self.Haos = self.read_dict('好.pkl')
        self.Les = self.read_dict('乐.pkl')
        self.Ais = self.read_dict('哀.pkl')
        self.Nus = self.read_dict('怒.pkl')
        self.Jus = self.read_dict('惧.pkl')
        self.Wus = self.read_dict('恶.pkl')
        self.Jings = self.read_dict('惊.pkl')

    def read_dict(self, file):
        # 模型加载
        pathchain = ['mod',file]
        mood_dict_filepath = pathlib.Path(__file__).parent.joinpath(*pathchain)
        dict_f = open(mood_dict_filepath, 'rb')
        words = pickle.load(dict_f)
        return words
    def setiment(self,sentences):
        #适用于商品评论
        # 读取积极标签的评论
        pos_data = []
        with open('pos.txt', 'r+', encoding='utf-8') as pos:
            while True:
                words = pos.readline()
                if words:
                    positive = {}
                    words = jieba.cut(words)
                    for word in words:
                        positive[word] = True
                    pos_data.append((positive, 'POS'))
                else:
                    break
        ## 读取消极情绪的评论
        neg_data = []
        with open('neg.txt', 'r+', encoding='utf-8') as neg:
            while True:
                words = neg.readline()
                if words:
                    negative = {}
                    words = jieba.cut(words)
                    for word in words:
                        negative[word] = True
                    neg_data.append((negative, 'NEG'))
                else:
                    break
        pos_num, neg_num = int(len(pos_data) * 0.8), int(len(neg_data) * 0.8)
        train_data = pos_data[: pos_num] + neg_data[: neg_num]
        test_data = pos_data[pos_num:] + neg_data[neg_num:]
        model = cf.NaiveBayesClassifier.train(train_data)
        #模型验证
        ac = cu.accuracy(model, test_data)
        # print('准确率为：' + str(ac))
        tops = model.most_informative_features()
        # print('\n信息量较大的前10个特征为:')
        # for top in tops[: 10]:
        # print(top[0])
        for sentence in sentences:
            feature = {}
            words = jieba.cut(sentence)
            for word in words:
                feature[word] = True
            pcls = model.prob_classify(feature)
            sent = pcls.max()
            prob = pcls.prob(sent)
            print('\n', sentence, '的情绪面标签为', sent, '概率为', '%.2f%%' % round(prob * 100, 2))
            #s1 = SnowNLP(sentence)
            #print(sentence + '的积极情感概率为:', s1.sentiments)
    def emo(self, text):
        #通用 基于词典模型
        hao, le, ai, nu, ju, wu, jing =0, 0, 0, 0, 0, 0, 0
        words = jieba.lcut(text)
        for w in words:
            if w in self.Haos:
                hao += 1
            elif w in self.Les:
                le += 1
            elif w in self.Ais:
                ai += 1
            elif w in self.Nus:
                nu += 1
            elif w in self.Jus:
                ju += 1
            elif w in self.Wus:
                wu += 1
            elif w in self.Jings:
                jing += 1
            else:
                pass
        result = '开心='+str(hao),"高兴="+str(le), '哀怨='+str(ai),'生气厌恶='+str(nu+wu),'惊俱='+str(ju+jing)
        return result
    def get_emotion(self,result):
        my_tuple = result
        # Convert the tuple to a dictionary
        my_dict = dict(my_tuple.split('=') for my_tuple in my_tuple)
        # Find the maximum value
        max_value = max(my_dict.values())
        # Get the key of the maximum value
        for key, value in my_dict.items():
            if value == max_value:
                max_key = key
        # Print the maximum key
        return max_key

if __name__ == '__main__':
    import sys
    while True:
        user_input = input("请输入您想要测试的文本（输入'T'退出）：")
        if user_input.upper() == 'T':
            print("程序已退出。")
            sys.exit(0)
        else:
            emotion = QEmo()
            #商品为评论主题
            # sentences = [user_input]
            # emotion.setiment(sentences)
            test_text = user_input
            # 通用主题
            result = emotion.emo(test_text)
            print(type(result))
            print(result)
            print(emotion.get_emotion(result))
