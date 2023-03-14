import streamlit as st


def display_intro():
    st.title('NursingCalc: Your Medication Dosage Calculator using the Nursing Formula')
    st.write("""
Medication administration is a core competency for all nurses in every clinical setting. A key skill required to safely 
dispense drugs is the ability to perform accurate dosage calculations. New technologies such as bar code administration 
and smart infusion pumps have helped to reduce medication errors, however nurses cannot rely completely on these 
advances.

In the nursing formula (or “desired over have method”), the desired amount (dose) is the dose  prescribed and the amount 
on hand (available dose) or the amount you “have” is the available dose or concentration. The quantity is the form and amount in 
which the drug is supplied (i.e. tablet, capsule, liquid). To calculate the dose, take the desired amount and divide it 
by the amount on hand, then multiply it by the quantity, like this:
""")


def display_formula_image():
    col1, col2, col3 = st.columns([4, 8, 4])
    with col1:
        st.write("")
    with col2:
        st.image('the_nursing_formula.png', use_column_width='auto')
    with col3:
        st.write("")


def get_user_inputs():
    dose = st.number_input('D - desired amount (the prescribed dose (mg, g, mL, etc):')
    available_dose = st.number_input('H - amount to hand (the available dose or concentration):')
    quantity = st.number_input('Q - quantity (volume or quantity (tablets, capsules, liquid):')
    return dose, available_dose, quantity


def calculate_dose(dose, available_dose, quantity):
    if quantity != 0:
        amount_to_administer = dose / available_dose * quantity
    else:
        amount_to_administer = 0
    return amount_to_administer


def display_output(dose, available_dose, quantity, amount_to_administer):
    st.latex(f'{dose} / {available_dose} \\times {quantity} = {amount_to_administer}')
    col4, col5, col6 = st.columns([4, 8, 4])
    with col4:
        st.write("")
    with col5:
        st.subheader(f'Amount to Administer = {amount_to_administer}')
    with col6:
        st.write("")


def the_nursing_formula():
    ''' the ‘nursing formula': volume to administer  = dose required (what you want) * volume of solution (what you got)
     / solution strength (what is in it)’'''

    # Display introduction
    display_intro()

    # Display nursing formula image
    display_formula_image()

    # Get user inputs
    dose, available_dose, quantity = get_user_inputs()

    # Calculate dose
    amount_to_administer = calculate_dose(dose, available_dose, quantity)

    # Display output
    display_output(dose, available_dose, quantity, amount_to_administer)


if __name__ == '__main__':
    the_nursing_formula()
