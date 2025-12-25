import pandas as pd
import os

file_path = r"C:\Users\Hp\OneDrive\Desktop\PythonProgramming\AI Project\Crop_recommendation.csv"

if not os.path.exists(file_path):
    print("Dataset not found.", file_path)
    exit()

data = pd.read_csv(file_path)
print(" Dataset loaded successfully")


crop_knowledge_base = {}

for crop in data['label'].unique():
    crop_data = data[data['label'] == crop]
    crop_knowledge_base[crop.capitalize()] = {
        "N": crop_data['N'].mean(),
        "P": crop_data['P'].mean(),
        "K": crop_data['K'].mean(),
        "temperature": crop_data['temperature'].mean(),
        "humidity": crop_data['humidity'].mean(),
        "ph": crop_data['ph'].mean(),
        "rainfall": crop_data['rainfall'].mean()
    }


def calculate_distance(user, crop):
    return (
        abs(user["N"] - crop["N"]) * 1.0 +
        abs(user["P"] - crop["P"]) * 1.0 +
        abs(user["K"] - crop["K"]) * 1.0 +
        abs(user["temperature"] - crop["temperature"]) * 2.0 +
        abs(user["humidity"] - crop["humidity"]) * 0.5 +
        abs(user["ph"] - crop["ph"]) * 10 +
        abs(user["rainfall"] - crop["rainfall"]) * 0.3
    )


def dfs(crop_list, user_input, index, depth, max_depth, best):
    if depth > max_depth or index >= len(crop_list):
        return best

    crop_name, crop_data = crop_list[index]
    distance = calculate_distance(user_input, crop_data)

    if distance < best[1]:
        best = (crop_name, distance)

    return dfs(crop_list, user_input, index + 1, depth + 1, max_depth, best)


def iddfs(crops, user_input, max_depth):
    crop_list = list(crops.items())
    best_result = (None, float("inf"))

    for depth in range(1, max_depth + 1):
        best_result = dfs(
            crop_list,
            user_input,
            index=0,
            depth=0,
            max_depth=depth,
            best=best_result
        )

    return best_result[0]


def AI_crop_recommendation_IDDFS(N, P, K, temperature, humidity, ph, rainfall):
    user_input = {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    crop = iddfs(crop_knowledge_base, user_input, max_depth=10)

    if crop:
        return f" Recommended Crop: {crop}"
    else:
        return "No suitable crop found for given conditions"


if __name__ == "__main__":
    print("\nAI Crop Recommendation System using IDDFS\n")
    
    try:
        N = float(input("Enter Nitrogen (N) value: "))
        P = float(input("Enter Phosphorus (P) value: "))
        K = float(input("Enter Potassium (K) value: "))
        temperature = float(input("Enter Temperature (°C): "))
        humidity = float(input("Enter Humidity (%): "))
        ph = float(input("Enter pH value: "))
        rainfall = float(input("Enter Rainfall (mm): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        exit()

    recommendation = AI_crop_recommendation_IDDFS(N, P, K, temperature, humidity, ph, rainfall)
    print("\n" + recommendation)
