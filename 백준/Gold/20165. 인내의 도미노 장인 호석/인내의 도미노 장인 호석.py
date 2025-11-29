import sys

# 표준 입력을 더 빠르게 받기 위한 설정
INPUT = sys.stdin.readline
# 방향 상수는 전역으로 명확하게 관리
DIRECTIONS = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

def solve():
    try:
        # 입력 처리
        N, M, R = map(int, INPUT().split())
        grid = [list(map(int, INPUT().split())) for _ in range(N)]
        
        # 상태 배열: 'S'(Standing), 'F'(Fallen)
        status = [['S'] * M for _ in range(N)]
        
        total_score = 0 # 공격수 총 점수

        for _ in range(R):
            # --- [공격수 턴] ---
            line = INPUT().split()
            atk_r, atk_c = int(line[0]) - 1, int(line[1]) - 1
            d_char = line[2]
            
            # FIX 1: 시작점이 이미 넘어져있으면 아무 일도 안 일어남 (Rule Check)
            if status[atk_r][atk_c] == 'S':
                # 첫 도미노 넘어뜨림
                status[atk_r][atk_c] = 'F'
                total_score += 1
                
                dr, dc = DIRECTIONS[d_char]
                residual_power = grid[atk_r][atk_c] - 1
                
                cur_r, cur_c = atk_r, atk_c

                while residual_power > 0:
                    new_r, new_c = cur_r + dr, cur_c + dc
                    
                    # FIX 2: 맵 범위를 벗어나면 즉시 종료 (Index Protection)
                    if not (0 <= new_r < N and 0 <= new_c < M):
                        break
                    
                    residual_power -= 1 # FIX 3: 이동했으므로 연료 1 소모
                    
                    if status[new_r][new_c] == 'S':
                        status[new_r][new_c] = 'F'
                        total_score += 1
                        # FIX 4: 새 도미노를 만나면 더 큰 힘으로 갱신 (Re-fueling)
                        # 이미 1을 뺐으므로 grid[new]-1 과 비교
                        residual_power = max(residual_power, grid[new_r][new_c] - 1)
                    
                    # 넘어진 도미노 위를 지나갈 땐 residual_power가 단순히 줄어든 상태로 유지됨
                    cur_r, cur_c = new_r, new_c

            # --- [수비수 턴] ---
            def_line = INPUT().split()
            def_r, def_c = int(def_line[0]) - 1, int(def_line[1]) - 1
            
            if status[def_r][def_c] == 'F':
                status[def_r][def_c] = 'S'

        # 결과 출력
        print(total_score)
        for row in status:
            print(*(row)) # 리스트 언패킹으로 깔끔하게 출력

    except Exception as e:
        # 디버깅용 (제출 시에는 주석 처리 가능)
        sys.stderr.write(f"Error: {e}\n")

if __name__ == "__main__":
    solve()