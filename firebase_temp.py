import firebase_admin
from firebase_admin import credentials, db


# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate(
    './emoji-recommendation-firebase-adminsdk-9td56-544cedf58d.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://emoji-recommendation-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

dir = db.reference()
dir.update({'자동차': ['기아', '현대', '벤츠']})

dir = db.reference('이동수단/기차')
dir.update({'1번': 'KTX'})
dir.update({'2번': '무궁화'})
