# 데이터 전처리
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/mac/project-sec3/data/drwtNo.csv')

# 모델 훈련에 사용되는 특성은 당첨번호1~당첨번호6
cols = ['drwtNo1', 'drwtNo2', 'drwtNo3', 'drwtNo4', 'drwtNo5', 'drwtNo6']
# 예측값은 보너스 번호
target = 'bnusNo'

# train, test 분리
X_train = df[cols].iloc[0:900]
y_train = df[target].iloc[0:900]
X_test = df[cols].iloc[900:]
y_test = df[target].iloc[900:]

# 훈련 / 최적 파라미터 확인
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

pipe = make_pipeline(
    SimpleImputer(),
    RandomForestClassifier()
)

dists = {
    'randomforestclassifier__n_estimators': randint(50, 500),
    'randomforestclassifier__max_depth': [5, 10, 15, 20, None]
}

clf = RandomizedSearchCV(
    pipe,
    param_distributions=dists,
    n_iter=50, #비교 조합 수 = 40
    cv=3, # cross validation = 3회
    scoring='accuracy',
    verbose=1,
    n_jobs=-1,
    random_state=2
)

clf.fit(X_train, y_train)

print('best hyperparams', clf.best_params_)
print('accuracy of train', clf.best_score_)

# 베스트 하이퍼파라미터
model = clf.best_estimator_

# 검증 정확도 확인
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print('accuracy of test: ', accuracy_score(y_test, y_pred))

# 파일형태로 모델 저장
import joblib
joblib.dump(model, '/Users/mac/project-sec3/flask_app/model/model.pkl')