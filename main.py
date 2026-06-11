# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20115이상민
# 프로젝트 주제: 실험실 효소 반응 속도(ph/온도) 조건 판정기

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 아래 예시는 "활동 추천 프로그램"입니다.
# 자신의 주제에 맞게 data를 만드세요.
#
# 현재 열의 의미:
# 0번 열: 효소 이름
# 1번 열: 효소가 가장 잘 반응하는 최적 온도
# 2번 열: 효소가 가장 잘 반응하는 최적 ph
# ------------------------------------------------------------

enzyme_data = [
    ["아밀레이스", 37, 7],
    ["펩신", 37, 7],
    ["트립신", 40, 8],
    ["카탈레이스", 37, 7],
    ["라이페이스", 37, 8],
    ["펩티데이스", 37, 8],
    ["말테이스", 37, 7],
    ["DNA중합효소", 37, 7],
    ["타크중합효소", 72, 9]
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def fine_enyzme(data, name):
    for row in data:
        if row[0] == name:
            return row
    return None

def check_activity(optimal_temp, optimal_ph, current_temp, current_ph):
    print("------------------------------")
    print(" [실험 조건 생화학적 분석 결과] ")
    print("------------------------------")

    if current_temp == optimal_temp and current_ph == optimal_ph:
        print(" 결과: 최고 활성(100%) 상태입니다. ")
        print(" 가이드: 효소가 가장 활발하게 반응하므로 실험을 진행하기에 완벽한 조건입니다. ")

    elif current_temp >= optimal_temp + 15:
        print(" 결과: 활성 없음 / 효소 변성 (0%) 상태입니다! ")
        print(" 가이드: 온도가 너무 높아 효소 단백질의 구조가 파괴(변성)되었습니다. ")
   
    elif current_temp == optimal_temp or current_ph == optimal_ph:
        print(" 결과: 보통 활성 (50%) 상태입니다.")
        print(" 가이드: 온도나 pH 중 하나만 최적 조건입니다. 반응 속도가 조금 느릴 수 있습니다. ")
    
    else:
        print(" 결과: 낮은 활성 상태 (실험 불가) 입니다. ")
        print(" 가이드: 환경 조건이 효소와 전혀 맞지 않습니다. ")
       

def get_experimental_conditions():
    print("\n--- [현재 실험실 환경 입력] ---")
    
    current_temp = int(input(" 현재 실험실의 온도를 입력하세요(℃): "))
    current_ph = int(input(" 현재 실험실의 ph농도를 입력하세요: "))
    
    return current_temp, current_ph

print(" 실험실 효소 반응 속도 조건 판정 프로그램 ")

while True:
    user_enzyme = input(" 실험할 효소 이름을 입력하세요: ")
    selected_enzyme = find_enzyme(enzyme_data, user_enzyme)
    
    if selected_enzyme is None:
        print(" 입력하신 효소는 데이터에 없습니다. 다시 입력해 주세요.")
        continue  
    else:
        print(f" {user_enzyme}을(를) 찾았습니다.")
        break  


opt_t = selected_enzyme[1]
opt_p = selected_enzyme[2]
print(f" {user_enzyme}의 최적 조건 -> 온도: {opt_t}℃, pH: {opt_p}")

cur_t, cur_p = get_experimental_conditions()

check_activity(opt_t, opt_p, cur_t, cur_p)


# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------

enzyme_data = [
    ["아밀레이스", 37, 7],
    ["펩신", 37, 2],
    ["트립신", 40, 8],
    ["카탈레이스", 37, 7],
    ["라이페이스", 37, 8],
    ["펩티데이스", 37, 8],
    ["말테이스", 37, 7],
    ["DNA중합효소", 37, 7],
    ["타크중합효소", 72, 9]
]

def find_enzyme(data, name):

    for row in data:
        if row[0] == name:
            return row 
    return None  


def get_experimental_conditions():
    print("\n--- [현재 실험실 환경 입력] ---")
    
    current_temp = int(input(" 현재 실험실의 온도를 입력하세요(℃): "))
    current_ph = int(input(" 현재 실험실의 ph농도를 입력하세요: "))
    
    return current_temp, current_ph


def check_activity(optimal_temp, optimal_ph, current_temp, current_ph):
    print("------------------------------")
    print(" [실험 조건 생화학적 분석 결과] ")
    print("------------------------------")

    if current_temp == optimal_temp and current_ph == optimal_ph:
        print(" 결과: 최고 활성(100%) 상태입니다. ")
        print(" 가이드: 효소가 가장 활발하게 반응하므로 실험을 진행하기에 완벽한 조건입니다. ")

    elif current_temp >= optimal_temp + 15:
        print(" 결과: 활성 없음 / 효소 변성 (0%) 상태입니다! ")
        print(" 가이드: 온도가 너무 높아 효소 단백질의 구조가 파괴(변성)되었습니다. ")
   
    elif current_temp == optimal_temp or current_ph == optimal_ph:
        print(" 결과: 보통 활성 (50%) 상태입니다.")
        print(" 가이드: 온도나 pH 중 하나만 최적 조건입니다. 반응 속도가 조금 느릴 수 있습니다. ")
    
    else:
        print(" 결과: 낮은 활성 상태 (실험 불가) 입니다. ")
        print(" 가이드: 환경 조건이 효소와 전혀 맞지 않습니다. ")


print(" 실험실 효소 반응 속도 조건 판정 프로그램 ")


while True:
    user_enzyme = input(" 실험할 효소 이름을 입력하세요: ").strip()
    selected_enzyme = find_enzyme(enzyme_data, user_enzyme)
    
    if selected_enzyme is None:
        print(" 입력하신 효소는 데이터에 없습니다. 다시 입력해 주세요.")
        continue  
    else:
        print(f" {user_enzyme}을(를) 찾았습니다.")
        break  

opt_t = selected_enzyme[1]  
opt_p = selected_enzyme[2]  
print(f" {user_enzyme}의 최적 조건 -> 온도: {opt_t}℃, pH: {opt_p}")


cur_t, cur_p = get_experimental_conditions()

check_activity(opt_t, opt_p, cur_t, cur_p)