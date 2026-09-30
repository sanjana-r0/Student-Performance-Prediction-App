from sklearn.linear_model import LogisticRegression

x=[
    [2,40],
    [3,55],
    [3,56],
    [4,65],
    [5,85],
    [6,90]
]
y=[0, 0, 0, 1, 1, 1]
model = LogisticRegression()
model.fit(x,y)

predictions = model.predict([[4, 70], [2, 45]])
print(predictions)
