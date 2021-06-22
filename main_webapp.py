from pywebio.input import *
from pywebio.output import *

# testing pywebio
input("What's your name?")
select("Select food", ['Orange', 'Apple'])
checkbox("Are your okay?", options=["I'm okay."])
radio("What do you like to do?", options=['Eat', 'Sleep', 'Study'])

