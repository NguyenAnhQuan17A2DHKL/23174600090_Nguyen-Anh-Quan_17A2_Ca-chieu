import random
import csv

def simulate_monty_hall(num_simulations):
    #Danh sách cánh cửa:
    doors = [1, 2, 3]
    #Lưu trữ kết quả:
    results = {'stay_win': 0, 'switch_win': 0}

    for _ in range(num_simulations):
        #Chọn vị trí của xe hơi:
        car_position = random.choice(doors)
        #Người chơi chọn một cánh cửa:
        player_choice = random.choice(doors)
        #Hiển thị cánh cửa không có giải thưởng:
        remaining_doors = [door for door in doors if door != player_choice and door != car_position]
        revealed_door = random.choice(remaining_doors)
        #Cho người chơi cơ hội đổi lựa chọn:
        new_choice = [door for door in doors if door != player_choice and door != revealed_door][0]
        #Xác định kết quả:
        if new_choice == car_position:
            results['switch_win'] += 1
        elif player_choice == car_position:
            results['stay_win'] += 1

    #Tính xác suất thắng:
    total_simulations = num_simulations
    stay_win_probability = results['stay_win'] / total_simulations
    switch_win_probability = results['switch_win'] / total_simulations

    #Lưu kết quả vào file CSV:
    with open('monty_hall_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Initial Choice', 'Final Choice', 'Result', 'Stay Win Probability', 'Switch Win Probability']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_simulations):
            writer.writerow({
                'Initial Choice': player_choice,
                'Final Choice': new_choice,
                'Result': 'Win' if new_choice == car_position else 'Lose',
                'Stay Win Probability': stay_win_probability,
                'Switch Win Probability': switch_win_probability
            })

    print(f"Xác suất thắng khi giữ nguyên lựa chọn: {stay_win_probability:.4f}")
    print(f"Xác suất thắng khi đổi lựa chọn: {switch_win_probability:.4f}")

#Thực hiện mô phỏng 200 lần:
simulate_monty_hall(num_simulations=200)
