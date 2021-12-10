import pandas as pd


def searchMatchingKeywords(morphs):
    data = pd.read_csv('./emoji-db', sep=',',
                       names=['Emoji', 'tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5', 'tag_6', 'tag_7', 'tag_8', 'tag_9', 'tag_10'])
    keywords = []
    emojis = []

    for word in morphs:
        search_result = data.index[(data['tag_1'] == word) |
                                   (data['tag_2'] == word) |
                                   (data['tag_3'] == word) |
                                   (data['tag_4'] == word) |
                                   (data['tag_5'] == word) |
                                   (data['tag_6'] == word) |
                                   (data['tag_7'] == word) |
                                   (data['tag_8'] == word) |
                                   (data['tag_9'] == word) |
                                   (data['tag_10'] == word)
                                   ].tolist()
        if search_result:
            # print("'{}' 키워드로 추천하는 이모지:".format(word))
            keywords.append(word)
            emojis.append([])

            for index in search_result:
                # print(data.loc[index, 'Emoji'])
                emojis[-1].append(data.loc[index, 'Emoji'])
            # print()

    return keywords, emojis


def dataToJSON(keywords, emojis):
    response = []

    for i in range(len(keywords)):
        emoji_list = []

        for j in range(len(emojis[i])):
            emoji = {"imageUrl": "", "rawText": emojis[i][j]}
            emoji_list.append(emoji)

        keyword = {"keyword": keywords[i], "emoji": emoji_list}
        response.append(keyword)

    return response
