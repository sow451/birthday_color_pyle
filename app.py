import streamlit as st
import datetime
import webcolors



# Set minimum date
min_birth_date = datetime.date(1900, 1, 1)



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
    else:
            birthday_str = f"{day:02}{month:02}{year}"
    #st.write('Birthday string value:',birthday_str)
    birthday_int = int(birthday_str)
    #st.write('Birthday integer value:',birthday_int)

    # Apply modulo only if needed where int value is higher than 16777215
    if birthday_int > 16777215:
        birthday_int = birthday_int % 16777215
    else:
        birthday_int = birthday_int
        
    # Convert int to hex    
    birthday_hex = format(birthday_int, '06x')
    birthday_hex = birthday_hex.upper()
    
    #show the colour in a box, the name and the hex
        
    st.markdown(
    f"<div style='width:100%;height:100px;background-color:#{birthday_hex};border-radius:10px;'></div>",
    unsafe_allow_html=True
)
    st.markdown(
f"Your birthday colour is so cool! And for reference, your birthday hex code is **#{birthday_hex.upper()}**"
)

    
    
    # birthday_hex_name = str('#'+'birthday_hex')
    # #st.write('Birthday hex value: #',birthday_hex)
    
    # #get colour name from hex
    # color_name = webcolors.hex_to_name((birthday_hex_name))
    # st.write(f"{color_name}")
    # except ValueError:
    # st.write("This hex code does not have a defined name - go ahead and name it yourself.")

    