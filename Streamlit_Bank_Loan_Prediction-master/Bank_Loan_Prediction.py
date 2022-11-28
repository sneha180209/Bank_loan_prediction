import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('./ML_Model11.pkl', 'rb'))

def run():
    img1 = Image.open('loan3.jpg')
    img1 = img1.resize((700,300))
    st.image(img1,use_column_width=False)

    st.title("Loan Prediction")

    ##For Account ID
    fn = st.text_input('Full Name')

    ##For Loan AMount
    loan_amt = st.number_input("Current Loan Amount",value=0)

    ## For Term
    term_display = ('Short Term','Long Term')
    term_options = list(range(len(term_display)))
    term = st.selectbox("Term",term_options, format_func=lambda x: term_display[x])

    ## For Credit Score
    cred_display = ('Between 0 to 250','Between 250 to 500','Between 500 to 750','Between 750 to 1000')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])

    ##For Annual Income
    ann_income = st.number_input("Annual Income",value=0)


    ##For Home Ownership
    dur_display = ['Home Mortgage','Rent','Own Home','HaveMortgage']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Home Ownership",dur_options, format_func=lambda x: dur_display[x])

    ##For Purpose
    pur_display = ['Home Improvements','Debt Consolidation','Buy House','Business Loan','other','major_purchase','Take a Trip',
    'Other','Buy a Car','small_business','Medical Bills','wedding','vacation','Educational Expenses','moving','renewable_energy']
    pur_options = range(len(pur_display))
    pur = st.selectbox("Purpose",pur_options, format_func=lambda x: pur_display[x])

    ##For Monthly Debt
    mon_debt= st.number_input("Monthly Debt",value=0)

    ##For Current Credit Balance
    lcredit_bal = st.number_input("Current Credit Balance",value=0)

    ##Bankruptcies
    # brp_display = ['0','1','2','3','4','5','6','7']
    # brp_options = range(len(brp_display))
    # brp=st.selectbox("Bankruptcies",brp_options, format_func=lambda x: brp_display[x])
    # new_title = '<p style="font-family:sans-serif; color:Red; font-size: 15px;">**Select number of times applicant is bankrupt</p>'
    # st.markdown(new_title, unsafe_allow_html=True)
    # st.markdown("")


    if st.button("Submit"):
        # duration = 0
        # if dur == 0:
        #     duration = 60
        # if dur == 1:
        #     duration = 180
        # if dur == 2:
        #     duration = 240
        # if dur == 3:
        #     duration = 360
        # if dur == 4:
        #     duration = 480
        features = [[loan_amt,term,cred,ann_income,dur,pur,mon_debt,lcredit_bal,0]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello!!" + fn + "|| " +' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello!!" + fn + "|| " +' || '
                'Congratulations!! you will get the loan from Bank'
            )

run()
