### 问题描述：
***
给定字符串数组，转换成摩斯码后，返回不重复摩斯码个数
### 代码实现：
***
```python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_dic = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
               "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
               "o": "---", "p": ".--.","q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
               "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        morse_words = [] # 存放不重复摩斯码
        for word in words:
            templist = ""
            for i in range(len(word)):
                templist += morse_dic[word[i:i+1]]
            if templist not in morse_words:
                morse_words.append(templist)
        # print (str(morse_words))

        return len(morse_words)

        
```
### 总结：
***
1. 思路：以字典的形式存储字母与之对应的摩斯码，遍历列表，将字符串逐个翻译成与之对应的摩斯码字符串。