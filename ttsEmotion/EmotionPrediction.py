from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import keras
import transformers
from transformers import AutoTokenizer, TFBertModel
from transformers import BertConfig, BertModel

le = LabelEncoder()
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert_model = TFBertModel.from_pretrained("bert-base-uncased")
model = TFBertModel.from_pretrained('./sentimentModel/6_emotion_detector.h5')
def predictRes(sentence,model,max_text_len):
    #sentence = normalized_sentence(sentence)
    sentenceToken = tokenizer(text=sentence,
                   add_special_tokens=True,
                   padding="max_length",
                   truncation=False,
                   max_length=max_text_len,
                   return_tensors='tf',
                   verbose=1)
    tf_output = model.predict({'input_ids':sentenceToken['input_ids'], 'attention_mask': sentenceToken['attention_mask']})
    tf_result = tf.nn.softmax(tf_output,axis=1)
    labels = ['joy', 'fear', 'anger', 'sadness']
    #labels = ['sadness', 'joy', 'anger', 'fear', 'surprise', 'love']
    label = tf.argmax(tf_result,axis=1)
    label = label.numpy()
    return labels[label[0]]

predictRes("Last day one worker in the work shop had got injured", model, 40)