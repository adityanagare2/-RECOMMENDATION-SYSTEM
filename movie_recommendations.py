from surprise import Dataset, SVD, Reader
from surprise.model_selection import cross_validate, train_test_split
from surprise import accuracy
import pandas as pd
import matplotlib.pyplot as plt

data = Dataset.load_builtin('ml-100k')
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

model = SVD()
model.fit(trainset)

predictions = model.test(testset)

rmse = accuracy.rmse(predictions)
mae = accuracy.mae(predictions)

print(f"\n✅ Evaluation Metrics:\nRMSE: {rmse:.4f}\nMAE: {mae:.4f}")

df_preds = pd.DataFrame(predictions, columns=['uid', 'iid', 'true_r', 'est', 'details'])

def get_top_n_recommendations(predictions, user_id, n=5):
    user_preds = [pred for pred in predictions if pred.uid == user_id]
    user_preds.sort(key=lambda x: x.est, reverse=True)
    top_n = user_preds[:n]
    
    print(f"\n🎬 Top {n} movie recommendations for User {user_id}:")
    for pred in top_n:
        print(f"Movie ID: {pred.iid} | Predicted Rating: {pred.est:.2f}")

get_top_n_recommendations(predictions, user_id='196')

plt.hist([pred.est for pred in predictions], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Predicted Ratings')
plt.xlabel('Predicted Rating')
plt.ylabel('Frequency')
plt.show()
