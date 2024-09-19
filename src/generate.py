# C.A. - Inria - 2022
# Simple site generator

from pathlib import Path
import os
import glob
from site_template import *


TEMPLATE_DIR = "template"


#template_file_list = glob.glob(TEMPLATE_DIR + "/*.template")

file_list = [
    ("index.html", "Home"),
    #("speaker.html", "Research Program"),    
    ("program.html", "Program"),
    ("speaker.html", "Speakers"),
    #("registration.html", "Registration")
]


NAVBAR_HEADER = '''
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-custom sticky-top">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto">
'''

NAVBAR_FOOTER = '''                    
                </ul>
            </div>
        </div>
    </nav>

'''


external_url_list = [
    ("https://6g-workshop.sciencesconf.org/registration", "Registration"),
    ]

for (file_name, page_name) in file_list:
    template_file_name = f"template/{file_name}.template"
    with open(template_file_name) as f:
        data = f.read()
    output_file_name = file_name

    navbar = NAVBAR_HEADER
    for other_file_name, other_page_name in file_list + external_url_list:
        #if other_file_name == file_name:
        #navbar += f'''<li><a class="current" href="{other_file_name}">{other_page_name}</a></li>''' + "\n"
        #else:
        #navbar += f'''<li><a href="{other_file_name}">{other_page_name}</a></li>''' + "\n"
        navbar += f'''
                    <li class="nav-item">
                        <a class="nav-link" href="{other_file_name}">{other_page_name}</a>
                    </li>
''' 
    navbar += NAVBAR_FOOTER

    output = data
    if file_name != "program.html":
        output = output.replace("<@HEAD@>", HEAD)
    else:
        output = output.replace("<@HEAD@>", HEAD_PROGRAM)        
    output = output.replace("<@BANNER@>", BANNER)
    output = output.replace("<@NAVBAR@>", navbar)
    output = output.replace("<@FOOTER@>", FOOTER)
    
    assert output_file_name != template_file_name    
    with open(output_file_name, "w") as f:
        f.write(output)
    print(f"+ generated '{output_file_name}'")

