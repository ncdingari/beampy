# -*- coding: utf-8 -*-

# HipsterOrange Theme for beampy
# Main keys of the dict should be the name of the beampy modules or class
# Each modules default options need to be defined here!

# version: 0.1
# Author: H. chauvet & Olivier!



########################## THEME DICT ##########################################


THEME = {}

lead_color = 'blue'
standard_text_color = 'black'
shaded_text_color = 'gray'


THEME['document'] = {
    'format': 'html5', #could be svg // pdf // html5
    'width': 800,
    'height': 600
}

THEME['text'] = {
    'size':20,
    'font':'CMR',
    'color': standard_text_color,
    'align':'',
    'x':'center',
    'y':'auto',
    'width':None,
    'usetex':True,
    'va': ''
}

THEME['title'] = {
    'size': 28,
    'font': 'CMR',
    'color': lead_color,
    'x': {'shift':0.5, 'unit':'cm'},
    'y': {'shift':1.2, 'unit':'cm'},
    'reserved_y': '1.5cm',
    'align': '',
    'va': 'baseline'
}


THEME['maketitle'] = { # name should be 'titlepage' :-)
    'title_color':THEME['title']['color'],
    'author_size':THEME['text']['size'],
    'date_color':standard_text_color,
    'subtitle_color':shaded_text_color,
}


THEME['link'] = {
    'fill':THEME['title']['color']
}

THEME['itemize'] = {
    'x':'center',
    'y':'auto',
    'item_style':'bullet',
    'item_spacing':'+1cm',
    'item_indent':'0cm',
    'item_color':THEME['title']['color'],
    'text_color':THEME['text']['color'],
    'width':None
}

####################### Define a new maketitle layout ##########################

from beampy.commands import *

def theme_maketitle(titlein, author = [], affiliation = None, meeting = None, lead_author = None, date=None ):
    """
        Function to create the presentation title slide
    """
    
    #get_command_line(maketitle)
    #Check function arguments from THEME
    args = THEME['maketitle']

    try:
        author[lead_author] = r'\underline{' + str(author[lead_author]) + '}'
        
    except:
        pass
    
    author_string = ', '.join(author)

    if date in ('Today', 'today', 'now'):
        date = datetime.datetime.now().strftime("%d/%m/%Y")

    with group(y="center"):

        text(titlein, width=750, y=0, color=args['title_color'], size=args['title_size'], align='center')

        if author != [] :
            text( author_string, width=750, y="+1.5cm", color=args['author_color'], size=args['author_size'], align='center')

        if affiliation != None:
            text(affiliation, width=750, y="+1cm", color=args['subtitle_color'], size=args['subtitle_size'])
            
        if meeting != None:
            text( meeting, width=750, y="+1cm", color=args['subtitle_color'], size=args['subtitle_size'])

        if date != None:
            text(date, width=750, y="+1cm", color=args['date_color'], size=args['date_size'])

THEME['maketitle']['template'] = theme_maketitle
