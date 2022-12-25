from sklearn.base import BaseEstimator, TransformerMixin
from underthesea import word_tokenize
import re
import pandas as pd


class Preprocesser(BaseEstimator, TransformerMixin):
  # def __init__(self, X=None, y=None) -> None:
  #   self.X = X
  #   self.y = y

  def fit(self, X, y=None):
    return self

  def remove_stop_words(self, X):
    with open('vietnamese-stopwords.txt') as f:
      stop_words = f.readlines()
      stop_words = list(set(m.replace(' ', '_').strip() for m in stop_words))
    for doc in X:
      arr = []
      try:
        for word in doc.split(' '):
          if word not in stop_words:
            arr.append(word)
      except:
        print(word)
      temp = " ".join(arr)
      X = X.replace(doc, temp)
    return X

  def remove_html(self, X):
    for i in X:
      try:
        X = X.replace(i, re.sub(r'<[^>]*>', '', i))
      except:
        pass
    return X
  uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
  unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"

  def loaddicchar(self):
      dic = {}
      char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
          '|')
      charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
          '|')
      for i in range(len(char1252)):
          dic[char1252[i]] = charutf8[i]
      return dic

  # Đưa toàn bộ dữ liệu qua hàm này để chuẩn hóa lại
  def convert_unicode(self, X):
    dic = self.loaddicchar()
    for i in X:
      X = X.replace(i, re.sub(
          r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
          lambda x: dic[x.group()], i))
    return X

  def tokenize(self, X):
    for i in X:
      X = X.replace(i, word_tokenize(i, format="text"))
    return X

  def lower_key(self, X):
    for i in X:
      X = X.replace(i, i.lower())
    return X

  def remove_noise_key(self, X):
    for i in X:
      # xóa các ký tự không cần thiết
      X = X.replace(i, re.sub(
          r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]', ' ', i))
      # xóa khoảng trắng thừa
      X = X.replace(i, re.sub(r'\s+', ' ', i).strip())
    return X

  def remove_digits(self, X):
    for i in X:
      try:
        X = X.replace(i, re.sub(r'\b\d+\b', "", i))
      except:
        pass
    return X

  def transform(self, X):
      X = pd.Series(X)
      X = self.remove_digits(X)
      # xóa html code
      X = self.remove_html(X)
      # chuẩn hóa unicode
      try:
        X = self.convert_unicode(X)
      except:
        print(Exception("unicode"))
        # tách từ
      try:
        X = self.tokenize(X)
      except:
        print(Exception("token"))
        # đưa về lower
      try:
        X = self.lower_key(X)
      except:
        print(Exception("Lowe"))
        # remove unneecessary key
      try:
        X = self.remove_noise_key(X)
      except:
        print(Exception("noise"))
        #remove stop word
      X = self.remove_stop_words(X)
      try:
        X = self.remove_noise_key(X)
      except:
        print(Exception("noise"))
      return X
