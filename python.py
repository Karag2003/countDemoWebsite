from flask import Flask, request, markup, render_template, flash, Markup
import os
import jason

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('random.html')
  
def get_state_options():
  #First step is to create a list of all states for each county in counties if the county's state is not in listOfState sadd the county's state to list of states
  type(states)
  stats_list = lists(states)
  #Second step is to create a string containing HTML code for the option in the select element 
  
  if __name__=="__main__":
    app.run(debug=False, port=54321)
