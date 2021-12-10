from konlpy.tag import Okt


# 형태소 분리
def splitByMorphs(text):
    okt = Okt()
    morph_list = okt.morphs(text, stem=True)  # 형태소로 분리, 원형
    # print("형태소 분리 결과:", morph_list)
    return morph_list
