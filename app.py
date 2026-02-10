import streamlit as st
import datetime


# Set minimum date
min_birth_date = datetime.date(1900, 1, 1)
MAX_COLOR = 0xFFFFFF
MODULO_BASE = MAX_COLOR + 1


def hex_division_steps(n: int):
    steps = []
    while True:
        q, r = divmod(n, 16)
        steps.append((n, q, r))
        if q == 0:
            break
        n = q
    return steps


st.title('What''s Your Birthday Color? 🎂🎂🎂')

st.markdown(
    """ 
    How it works: Enter your date of birth, and find your own unique birthday color! Behind the scenes, your date is turned into a hex code - a six digit code that computers use to represent colors (Eg: #FF0987 represents bright pink). 

    """
)

your_birthday = st.date_input("When's your birthday", min_value=min_birth_date)
st.write("Your birthday is:", your_birthday.strftime("%d %B %Y"))

if st.button("Get My Birthday Color",type="primary"):

    # Review dateinput and see if month is single or double digit. If former, do nothing. If latter, convert it into a modulo w 16777216 
    # Convert date into string
    day = your_birthday.day
    month = your_birthday.month
    year = your_birthday.year

    # Use DDmYYYY or DDMMYYYY based on month and convert the birthday string val to int
    if month < 10:
            birthday_str = f"{day:02}{month}{year}"
            format_pattern = "DDmYYYY"
    else:
            birthday_str = f"{day:02}{month:02}{year}"
            format_pattern = "DDMMYYYY"
    #st.write('Birthday string value:',birthday_str)
    birthday_int_raw = int(birthday_str)
    #st.write('Birthday integer value:',birthday_int)

    # Apply modulo only if needed where int value is higher than MAX_COLOR
    if birthday_int_raw > MAX_COLOR:
        birthday_int = birthday_int_raw % MODULO_BASE
        wrapped = True
    else:
        birthday_int = birthday_int_raw
        wrapped = False
        
    # Convert int to hex    
    birthday_hex = format(birthday_int, '06x')
    birthday_hex = birthday_hex.upper()
    
    #show the colour in a box, the name and the hex
        
    st.markdown(
    f"<div style='width:100%;height:100px;background-color:#{birthday_hex};border-radius:10px;'></div>",
    unsafe_allow_html=True
)
    st.markdown("### Here's your birthday colour!")

    st.markdown(
        f"Hex code: **#{birthday_hex.upper()}**"
    )

    remainder_str = f"{birthday_int:,}"
    wrap_sentence = (
        "That did not fit within the upper limit of 16,777,215, so we first ran a modulo "
        "operation (divide your number by 16,777,216 and used that remainder "
        f"{remainder_str} as the starting point). Then, we ran the math on that number "
        "and delivered a hex (see how we did it below)."
        if wrapped else
        "That fits within the upper limit of 16,777,215, so we ran the math and delivered "
        "a hex (see how we did it below)."
    )
    st.markdown("**How unique is it?**")
    st.markdown(
        "There are about 16.7 million possible 6-digit hex colors, so your birthday "
        "usually lands on a unique color. But if the number gets too large, we use "
        "modulo to wrap it back into the valid range, which can cause collisions."
    )
    st.markdown(
        f"For your date **{your_birthday.strftime('%d-%m-%Y')}**, we used **{format_pattern}** "
        f"and got **{birthday_str}**. {wrap_sentence}"
    )

    with st.expander("Show me the math: how a number becomes hex"):
        steps = hex_division_steps(birthday_int)
        step_lines_md = "\n".join(
            f"- {n:,} ÷ 16 = {q:,} remainder {format(r, 'X')}"
            for n, q, r in steps
        )
        st.markdown(f"**Date entered:** {your_birthday.strftime('%d-%m-%Y')}")
        st.markdown(f"**Number used:** {birthday_int:,}")
        st.markdown(
            "To convert a number to hex, we keep dividing by 16 and record the remainder. "
            "Read the remainders from bottom to top to get the hex digits."
        )
        st.markdown(step_lines_md)
        st.markdown(
            f"Read bottom to top: **{birthday_hex.upper()}**, so the hex code is "
            f"**#{birthday_hex.upper()}**."
        )

    
#name the color
# import webcolors

    # birthday_hex_name = str('#'+'birthday_hex')
    # #st.write('Birthday hex value: #',birthday_hex)
    
    # #get colour name from hex
    # color_name = webcolors.hex_to_name((birthday_hex_name))
    # st.write(f"{color_name}")
    # except ValueError:
    # st.write("This hex code does not have a defined name - go ahead and name it yourself.")

    
