def main():
    userName=input("Enter your name:")
    userDescription=input("Describe yourself:")
    print(userName)
    print(userDescription)

    html_str = """<html>
    <head>
    </head>
    <body>
        <center>
            <h1>"""+userName+"""</h1>
        </center>
        <hr />"""+userDescription+"""
        <hr />
    </body>
</html>"""

    Html_file = open("filename.html", "w")
    Html_file.write(html_str)
    Html_file.close()


main()