<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta charset= "utf-8">
    <title>SBI ORM</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" />


    <style>
        /* DEMO-SPECIFIC STYLES */
        .typewriter h1 {
            color: navy;
            font-family: monospace;
            overflow: hidden;
            /* Ensures the content is not revealed until the animation */
            border-right: .15em solid white;
            /* The typwriter cursor */
            white-space: nowrap;
            /* Keeps the content on a single line */
            margin: 0 auto;
            /* Gives that scrolling effect as the typing happens */
            letter-spacing: .15em;
            /* Adjust as needed */
            animation:
                typing 7.5s steps(30, end),
                blink-caret .5s step-end infinite;
        }

        /* The typing effect */
        @keyframes typing {
            from {
                width: 0
            }

            to {
                width: 100%
            }
        }

        /* The typewriter cursor effect */
        @keyframes blink-caret {

            from,
            to {
                border-color: transparent
            }

            50% {
                border-color: white
            }
        }



        .container1 {
            display: inline-block;
            cursor: pointer;
            float: right;

        }

        .bar1,
        .bar2,
        .bar3 {
            width: 35px;
            height: 5px;
            background-color: #333;
            margin: 6px 0;
            transition: 0.4s;

        }

        .change .bar1 {
            -webkit-transform: rotate(-45deg) translate(-9px, 6px);
            transform: rotate(-45deg) translate(-9px, 6px);
        }

        .change .bar2 {
            opacity: 0;
        }

        .change .bar3 {
            -webkit-transform: rotate(45deg) translate(-8px, -8px);
            transform: rotate(45deg) translate(-8px, -8px);
        }

    </style>




</head>



<body>


    <div class="container"><br>
    
        <h2 align="center"><img src="sbi.jpg" alt="j" width="250" height="80"><br><br>
            <div class="typewriter">
                <h1>Online Response Management.</h1>
            </div>
        </h2> <br /><!-- carol-rebeiro -->
    
        <div class="form-group">
            <div class="input-group">
                <span class="input-group-addon">Search</span>
                <input type="text" name="search_text" id="search_text" placeholder="Search by keywords" class="form-control" />
            </div>
        </div>
        <br />
        <div id="result"></div>
    </div>

</body>

</html>
