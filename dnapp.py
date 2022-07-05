import streamlit as st
st.set_page_config(layout="wide") 

def clean(num):
    if num == 1:
        st.session_state.firstpair= []
        st.session_state.firsttype= []
    if num == 2:
        st.session_state.secondpair= []
        st.session_state.secondtype= []  
    return

def dna():
    # init
    if 'firstpair' not in st.session_state:
        st.session_state.firstpair= []
    if 'firsttype' not in st.session_state:
        st.session_state.firsttype= []
    if 'secondpair' not in st.session_state:
        st.session_state.secondpair= []
    if 'secondtype' not in st.session_state:
        st.session_state.secondtype= []
    # end of init

    col1, col2  = st.columns([2, 2])

    form = col1.form(key='my_form')
    pairs = form.text_input("Input First pairs")
    type = form.text_input("Input First pairs type")
    clear = form.checkbox("Clear")
    submit_button = form.form_submit_button(label='Submit')
    if submit_button and pairs and type:
        st.session_state.firstpair.append(pairs)
        st.session_state.firsttype.append(type)
    if clear:
        clean()
    col2.title("First Pairs")
    col2.code(st.session_state.firstpair)
    col2.title("Type of First Pairs")
    col2.warning(st.session_state.firsttype)

    form2 = col1.form(key='my_form_2')
    pairs = form2.text_input("Input Second pairs")
    type2 = form2.text_input("Input Second pairs type")
    clear = form2.checkbox("Clear")
    submit_button_2 = form2.form_submit_button(label='Submit')
    if submit_button_2:
        st.session_state.secondpair.append(pairs)
        st.session_state.secondtype.append(type2)
    if clear:
        clean(2)
    col2.title("Second Pairs")
    col2.code(st.session_state.secondpair)
    col2.title("Type of Second Pairs")
    col2.warning(st.session_state.secondtype)
    
    form3 = col1.form(key='my_form_3')

    target =form3.text_input("Please enter targer: ")
    submit_button_3 = form3.form_submit_button(label='Submit')
    
    if submit_button_3 and target:
        tmp = ""
        for i in range(len( st.session_state.firstpair)):
        # print(split(firstpair[i]))
            tmp+=st.session_state.firstpair[i]
        for i in range(len( st.session_state.secondpair)):
        # print(split(firstpair[i]))
            tmp+=st.session_state.secondpair[i]

        # print(tmp)
        col2.text("Combined String")
        col2.success(tmp)

        import itertools
        result = list(itertools.combinations(tmp, 2))
        hit = 0

        # print("Target pair: " + str( tuple(target)+"\n"))
        target = tuple(target)
        for i in range(len(result)):
            if result[i]==target:
                hit +=1

        percentage =  hit/len(result)


        col1.title("% of "+str(target)+": "+str(percentage))
        col2.title("All combinations")
        col2.code(result)
        # option = col2.multiselect(
        #  'Select your markers',
        #  ('M', 'L', 'S'))
        

    return


page_names_to_funcs = {
    "DNA Combination": dna
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()