#constellation.py
#python3 program use unicode print constellation

'''
这些星座英文分别是:
 Aries 白羊座（3月21日～4月20日）
 Taurus 金牛座（4月21～5月21日） 
 Taurus 金牛座（4月21～5月21日） 
 Gemini 双子座（5月22日～6月21日） 
 Cancer 巨蟹座（6月22日～7月22日）
  Leo 狮子座（7月23日～8月23日） 
  Virgo 处女座（8月24日～9月23日） 
  Libra 天秤座（9月24日～10月23日） 
  Scorpio 天蝎座（10月24日～11月22日） 
  Sagittarius 射手座（11月23日～12月21日） 
  Capricorn 摩羯座（12月22日～1月20日） 
  Aquarius 水瓶座（1月21日～2月19日） 
  Pisces 双鱼座（2月20日～3月20日）
'''

for i in range(12):
    print(chr(9800 + i), end="")

