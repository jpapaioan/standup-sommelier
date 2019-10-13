from flask import render_template, request, redirect
from application_folder import flask_instance, com_methods
import os
import pandas as pd

@flask_instance.route('/', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        df = com_methods.retrieve_df()
        rating = int(request.form['rating'])
        joke_style = int(request.form['joke_style'])

        if rating == 1:
            rating_label = 'PG'
        elif rating == 2:
            rating_label = 'PG-13'
        else:
            rating_label = 'R'

        if joke_style == 0:
            form_label = 'short-form'
        else:
            form_label = 'long-form'

        comics = com_methods.comic_search(df, rating, joke_style)
        comic_url_list = com_methods.comic_url(comics)
        
        template_dict = {
            'rating_key' : rating_label,
            'joke_form' : form_label,
            'comic1': comics[0],
            'comic2': comics[1],
            'comic3': comics[2],
            'vid_link1': comic_url_list[0],
            'vid_link2': comic_url_list[1],
            'vid_link3': comic_url_list[2]
            }
        return render_template('test_results.html', **template_dict)    
    return render_template('test.html')