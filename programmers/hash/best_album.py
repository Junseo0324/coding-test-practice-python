# 노래를 수록하는 기준은 다음과 같습니다.
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# genres = 노래 장르 , plays = 재생 횟수

from collections import defaultdict


def solution(genres, plays):
    genres_hash = {}
    genre_idx_song = defaultdict(list)
    print(genres_hash)
    answer = []

    for idx, genre in enumerate(genres):
        genres_hash[genre] = genres_hash.get(genre, 0) + plays[idx]
        genre_idx_song[genre].append((plays[idx], idx))

    sorted_genres = sorted(genres_hash.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_idx_song[genre], key=lambda x: (-x[0], x[1]))
        for song in sorted_songs[:2]:
            answer.append(song[1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
