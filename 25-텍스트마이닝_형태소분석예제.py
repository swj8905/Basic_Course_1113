from konlpy.tag import Okt

okt = Okt()
# result = okt.pos("이런 것도 되나욬ㅋㅋㅋㅋ")
result = okt.nouns("저는 코딩을 공부하고 있습니다.")
print(result)