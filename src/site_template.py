
HEAD = '''
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indo-French Seminar on 6G Wireless Networks</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .navbar-custom {
            background-color: #0056b3;
        }

        .navbar-custom a {
            color: white;
        }

        .header-logo img {
            max-height: 100px;
            margin-bottom: 20px;
        }

        .header-title {
            font-size: 1.8rem;
            font-weight: bold;
        }

        .header-subtitle {
            font-size: 1.2rem;
        }

        .header {
            padding: 20px;
            text-align: center;
        }

        .header-text {
            margin-top: 10px;
        }

        .nav-link {
            color: white;
            font-size: 1.1rem;
        }

        .nav-link:hover {
            color: #e2e6ea;
        }

        .section-title {
            font-size: 28px;
            color: #0056b3;
            margin-bottom: 10px;
        }

        .agenda, .speakers, .contact {
            background-color: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .full-width {
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
        }

        .date-location {
            background-color: #0056b3;
            padding: 20px;
            margin: 40px 0;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .date-location .section-title {
            font-size: 2rem;
            color: white;
            margin-bottom: 15px;
        }

        .date-location p {
            color: white;
            line-height: 1.6;
        }

        .date-location a {
            color: white;
            text-decoration: none;
        }
        .date-location a:hover {
            text-decoration: underline;
        }

        .agenda-calendar td {
            background-color: #004080;
            font-size: 1.1rem;
        }
 
        .agenda-calendar td:first-child {
            width: 20%;
            font-weight: bold;
        }

        .agenda-calendar td:last-child {
            width: 80%;
        }


        footer {
            text-align: center;
            padding: 20px;
            background-color: #004080;
            color: white;
        }

        html {
            scroll-behavior: smooth;
        }
    </style>
</head>
'''


HEAD_PROGRAM = '''
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indo-French Seminar on 6G Wireless Networks</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .navbar-custom {
            background-color: #0056b3;
        }

        .navbar-custom a {
            color: white;
        }

        .header-logo img {
            max-height: 100px;
            margin-bottom: 20px;
        }

        .header-title {
            font-size: 1.8rem;
            font-weight: bold;
        }

        .header-subtitle {
            font-size: 1.2rem;
        }

        .header {
            padding: 20px;
            text-align: center;
        }

        .header-text {
            margin-top: 10px;
        }

        .nav-link {
            color: white;
            font-size: 1.1rem;
        }

        .nav-link:hover {
            color: #e2e6ea;
        }

        .section-title {
            font-size: 28px;
            color: #f3f6f4;
            margin-bottom: 20px;
            text-align: center;

        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .section-title {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 40px;
        }

        .day-section {
            margin-bottom: 50px;
            background-color: #f0f4f8; /* Light background color for each section */
            padding: 20px;
            border-radius: 8px;
        }

        .day-title {
            font-size: 1.8rem;
            color: #0056b3;
            margin-bottom: 20px;
        }

        .agenda-calendar {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        .agenda-calendar th,
        .agenda-calendar td {
            border: 1px solid #ddd;
            padding: 15px;
            text-align: left;
            vertical-align: top;
        }

        .agenda-calendar th {
            background-color: #004080; /* Dark blue background for the table headers */
            color: white;
            font-weight: bold;
            text-align: center;
        }

        .agenda-calendar td {
            background-color: #004080;
            font-size: 1.1rem;
        }

        .agenda-calendar td:first-child {
            width: 20%;
            font-weight: bold;
        }

        .agenda-calendar td:last-child {
            width: 80%;
        }


        footer {
            text-align: center;
            padding: 20px;
            background-color: #004080;
            color: white;
        }

        html {
            scroll-behavior: smooth;
        }
    </style>
</head>
'''


BANNER = '''
   <!-- Header Section with 5 Logos (3 on the left, 2 on the right) -->
    <div class="container-fluid bg-light">
        <div class="row align-items-center header">
            <!-- Left Logos (3 logos) -->
            <div class="col-md-2 text-center header-logo">
                <div class="row">
                 <div class="col-10">
                        <img src="img/CEFPIRA.png" alt="CEFIPRA Logo" class="img-fluid mb-2">
                    </div>
                
                 <div class="col-6">
                        <img src="img/Ministry_of_Science_and_Technology_India.svg" alt="INIDA Ministry Logo" class="img-fluid mt-2">
                    </div>
                 <div class="col-6">
                        <img src="img/MDEA.jpg" alt="French Ministry Logo" class="img-fluid mb-2">
                    </div>
                   
                </div>
            </div>

            <!-- Title and Subtitle -->
            <div class="col-md-8 text-center header-text">
                <p class="header-title">Indo-French Seminar </p>
                
                <p class="header-title">6G Wireless Networks: Challenges and Opportunities</p>
                <p class="header-title"> October 9 - 10 - 11, 2024</p>
                
            </div>

            <!-- Right Logos (2 logos) -->
            <div class="col-md-2 text-center header-logo">
                <div class="row">
                   

                     <div class="col-6">
                        <img src="img/india2.png" alt="IIT (BHU) Varanasi logos " class="img-fluid mb-2">
                    </div>
                    <div class="col-6">
                        <img src="img/indianLogo.png" alt="IIT Guwahati  Logo" class="img-fluid mb-2">
                    </div>
<!--
                    <div class="col-12">
                        <img src="img/InriaLogo2.png" alt="Inria Logo" class="img-fluid mt-2">
                    </div>
                      <div class="col-12">
                        <img src="img/france-relance.png" alt="Funded by France Relance" class="img-fluid mt-2">
                    </div>
-->
                    <div class="col-6">
                        <img src="img/InriaLogo2.png" alt="Inria Logo" class="img-fluid mb-2">
                    </div>
                      <div class="col-6">
                        <img src="img/france-relance.png" alt="Funded by France Relance" class="img-fluid mb-2">
                    </div>




                </div>
            </div>
        </div>
    </div>
'''


NAVBAR = '''
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-custom sticky-top">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="Agenda.html">Agenda</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="Speaker.html">Speakers</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

'''

FOOTER = '''
      <footer class="text-center mt-5">
        <p>© 2024 organizers of the "6G Wireless Networks" seminar | Funded by CEFIPRA, France Relance and Inria</p>
<p>Contacts: <a href="mailto:cedric.adjih@inria.fr">Cedric Adjih (Inria)</a> and <a href="mailto:kuntaldeka@iitg.ac.in">Kuntal Deka (IIT Guwahati)</a></p>
    </footer>
'''



NAVBAR2 = '''
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-custom sticky-top">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="home.html">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#agenda">Agenda</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="Speaker.html">Speakers</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="Corrected_6G_Workshop_Program_Schedule_Linked.html">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
'''
