import streamlit as st

import pandas as pd
import xgboost as xgb
import pickle

xyz = st.container(height = 300, border = True)
xyz.image(r"useit.jpg",caption = "Power Lifting",use_column_width=True, clamp=True,width = 100)
st.title("Power Lifting Prediction :man-lifting-weights:",anchor = False)
st.markdown("Check your ability")

playerId = st.number_input(label = "Enter your Id :",
                           help  = "If your new please register",
                           placeholder = "enter yout id",
                           value = 0)
Sex = st.radio(label = "Enter your sex",
               options = [1,0],
               captions = ["Male","Female"],
               horizontal = True,
               help = "Why are you gay...")
Age = st.number_input(label = "Enter your Age :",
                      help  = "Hey how old are you",
                      placeholder = "enter you age",
                      min_value = 7,
                      max_value = 83)
Equipment = st.radio(label = "Enter your Equipment ...",
                     options = [1,2,3,4],
                     captions = ["Raw", "Single-ply","Wrap","Multi-ply"],
                     horizontal = True,
                     help = "Choose the option")
BodyWeight = st.number_input(label = "Body Weight",
                             placeholder = "Enter your body weight",
                             min_value = 23.7,
                             help = "minimum weight is 23.7")
Squat = st.number_input(label = "Best Squat",
                        placeholder = "Enter the Best Squat",
                        help = "Enter the squat you have done")
BestBench = st.number_input(label = "Best Bench",
                            placeholder = "Enter the Best Bench",
                            help = "Enter the best bench value you have made")
input = {
        'playerId' : playerId,
        
        'Sex' : Sex,
        'Equipment' : Equipment,
        'Age' : Age,
        'BodyweightKg' : BodyWeight,
        'BestSquatKg' : Squat,
        'BestBenchKg' : BestBench
    }
data = pd.DataFrame(input, index = [0])
status = False
if playerId and Sex and BestBench and Squat and BodyWeight and Equipment and Age :
    status = st.button(label = "Submit")

if status:
    model = pickle.load(open(r'xg.model.pkl','rb'))
    output = model.predict(data)
    st.info(f"Estimated DeadLift for the Builder  {output}" )

