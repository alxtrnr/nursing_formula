import streamlit as st

def the_nursing_formula():
    ''' the ‘nursing formula': volume to administer  = dose required (what you want) * volume of solution (what you got)
     / solution strength (what is in it)’'''

    # inputs block
    medication = st.text_input('Name of medication:')
    dose_required = st.number_input('Amount prescribed (mg):')
    vol_solution = st.number_input('Volume of solution (ml):')
    dose_available = st.number_input('Solution strength (mg/ml?):')

    # the nursing formula calculation
    if dose_available != 0:
        vol_to_administer = dose_required * vol_solution / dose_available
    else:
        vol_to_administer = 0

    # confirmation of inputs
    st.write(f'{medication} {dose_required}mg is prescribed. You have {medication} {dose_available}mg/{vol_solution}ml.')

    # output block
    st.subheader('THE NURSING FORMULA')
    form = f'{dose_required}mg (what you want) x {vol_solution}ml (what you got) / {dose_available}mg (what\'s in it)'
    st.write(form)

    st.write(f'Volume to administer = {vol_to_administer}ml')


if __name__ == '__main__':
    the_nursing_formula()
