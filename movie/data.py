#필요한 라이브러리 Import
import requests
import pandas as pd
import json
from models import *

def get_matches_data(api_key):
    uri = 'https://api.football-data.org/v4/matches' #정보를 받아오는 곳
    headers = { 'X-Auth-Token': api_key } #개인키

    # API 요청 보내기
    response = requests.get(uri, headers=headers) 
    # 받아온 데이터 중 필요한 정보 추출하여 리스트에 담기
    matches_data = []
    for match in response.json()['matches']:
        match_info = {
            '경기일시': match['utcDate'],
            '경기상태': match['status'],
            '1팀': match['homeTeam']['name'],
            '2팀': match['awayTeam']['name'],
            '1팀 득점': match['score']['fullTime']['home'] if match['score']['fullTime']['home'] is not None else None,
            '2팀 득점': match['score']['fullTime']['away'] if match['score']['fullTime']['away'] is not None else None,
            '승자': match['score']['winner'] if 'winner' in match['score'] else '미정',
            '1팀득점자': None,  # 해당 정보가 API에서 제공되지 않아서 None으로 설정
            '2팀득점자': None   # 해당 정보가 API에서 제공되지 않아서 None으로 설정
        }
        matches_data.append(match_info)

    # 데이터프레임 생성
    columns = ['경기일시', '경기상태', '1팀', '2팀', '1팀 득점', '2팀 득점', '승자', '1팀득점자', '2팀득점자']
    df = pd.DataFrame(matches_data, columns=columns)
    # 경기 일시를 기준으로 오름차순 정렬
    df['경기일시'] = pd.to_datetime(df['경기일시'])
    df = df.sort_values(by='경기일시').reset_index(drop=True)
    # 인덱스를 1부터 시작하도록 변경
    df.index = df.index + 1
    return df

def update_and_upload_data(df):
    for _, row in df.iterrows():
        question = Question(
        subject=f'{row['1팀']} vs {row['2팀']}',
        content=row['경기상태'],
        game_date=row['경기일시'],
        )
        question.save()

# 파이썬을 직접실행했을 때 실행됨
# if __name__ == "__main__":
api_key = ''
df = get_matches_data(api_key)
update_and_upload_data(df)