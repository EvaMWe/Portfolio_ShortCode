import mysql.connector as mc
import mysql

connection_params = {"host":"localhost", "user":"root", "passwd":"12345"}

def main(connection_params):
    qu = input("Do your want to create a new database? (Y/N)")

    if qu == "Y" or qu == "y":
        c,cnx,curr_name = create_newbase(database= None, **connection_params)

    elif qu == "N" or qu == "n":
        curr_name = input("Enter database you want to establish a connection to:")

        try:
            c, cnx = connect_to_base(database=curr_name, **connection_params)
            print(f"Verbindung zur Datenbank {curr_name} hergestellt!")
            return (cnx, c, curr_name)

        except mysql.connector.Error as err:
            print("Es ist ein Fehler aufgetreten\n", err)


def connect_to_base(database=None, **kwargs):
    '''this function performs the connection to the database'''

    if database:
        cnx = mc.connect(database=database, **kwargs)
    else:
        cnx = mc.connect(**kwargs)


    # Create the cursor object
    c = cnx.cursor()
    return c, cnx


def create_newbase(**kwargs):
    """this function will create a new data base: checks if a database exists if yes --> establish just connection if no --> create the database
    Args:
        db_name (string); name of the database
        host (string); host of the database
        user (string); user of the database
        passwd (string); password of the database
    Returns:
        None
        """
    # Create the connection to mysql Server
    c, cnx = connect_to_base(**kwargs)

    c = cnx.cursor()
    #check if data base is really new
    db_name = input("Geben Sie einen Namen für die Datenbank ein: ")
    sql = "SHOW DATABASES LIKE '%s'" % db_name
    c.execute(sql)
    result = c.fetchone()
    if result == None:
        try:
            c.execute(f"CREATE DATABASE {db_name}")
            print("Datenbank erstellt!")
            return (cnx,c)

        except mysql.connector.Error as err:
            print("Es ist ein Fehler aufgetreten\n", err)
    else:
        c, cnx = connect_to_base(database = db_name, **kwargs)
        print("Die Datenbank besteht bereits, eine Verbindung wurde erstellt")
        return (cnx, c, db_name)

    menue()


def execute_close_base(command, c, connection, commit=False, parameters=0):
    if parameters == 0:
        if commit == True:
            try:
                c.execute(command)
                connection.commit()

            except mc.errors.ProgrammingError:
                print("Es ist ein Fehler bei der Verbindung zur Datenbank aufgetreten!")

            finally:
                connection.close()

        else:
            try:
                c = connection.cursor()
                c.execute(command)
                ausgabe = c.fetchall()
                return ausgabe, c, connection,

            except mc.errors.ProgrammingError:
                print("Es ist ein Fehler bei der Verbindung zur Datenbank aufgetreten!")

            finally:
                connection.close()

    else:
        if commit == True:
            try:
                c.execute(command, parameters)
                connection.commit()

            except mc.errors.ProgrammingError:
                print("Es ist ein Fehler bei der Verbindung zur Datenbank aufgetreten!")

            finally:
                connection.close()

        else:
            try:
                c = connection.cursor()

            except mc.errors.ProgrammingError:
                print("Es ist ein Fehler bei der Verbindung zur Datenbank aufgetreten!")
                connection.close()

            c.execute(command, parameters)
            ausgabe = c.fetchall()
            print(ausgabe)
            return ausgabe
            connection.close()


def create_table():  #dynamisch machen
    c, connection = connect_to_base()
    table_name = input("Enter")
    sql = """CREATE TABLE IF NOT EXISTS warenkorb_ (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        article_nb VARCHAR(24) NOT NULL,
        netto_price DECIMAL(10,2)
    );"""

    execute_close_base(sql, c, connection)


def insert_products():
    '''this function is to insert products into database
    return None; call menue in the end
    '''
    product = input("Produkt-Name: ")
    nb = input("Artikelnummer: ")

    while True:
        try:
            price = float(input("Netto_Preis: "))
            break
        except ValueError as err:
            print("Pleaser enter the price as a number, text is not valid")
            print(err)

    params = (product, nb, price)
    c, connection = connect_to_base()

    sql = """INSERT INTO warenkorb_ (`product_name`, `article_nb`, `netto_price`) VALUES (%s, %s, %s)"""
    execute_close_base(sql, c, connection, commit=True, parameters=params)

    menue()


def select_products(*commands):
    c, connection = connect_to_base()
    if commands in locals():
        column = input("enter column you want to see, press q to quit, type \"allC\" for all columns: ")
    else:
        column = None
    col = []

    while True:

        if column == "q":
            break
        elif commands == "allC" or column == "allC":
            col = "*"
            break
        else:
            col.append(column)

    tabl_nam = input("Table Name: ")

    condition = input("Condition : ")

    sql = "SELECT " + ", ".join(col) + " FROM " + tabl_nam + " " + condition

    ausgabe = execute_close_base(sql, c, connection, commit=False, parameters=0)
    a, _, _ = ausgabe  #List of entries

    for entri in a:
        _, b, c, d = entri
        print(f"Product: {b}, Article Number: {c}, Price: {d}")


def delete_products():
    '''this is a function to delete an entry from the database
    it works together with the search function'''
    c, connection = connect_to_base()
    print("Please specify the product you want to delete:")

    ausgabe = search_products()


def search_products():
    '''user is supposed to enter the product name or the article number; the function will
    try if the input matches product name or the article number'''
    c, connection = connect_to_base()
    item = input("enter the product or article number you want to find ")
    params = (item, item)
    sql = """SELECT * FROM warenkorb_ WHERE product_name = %s OR article_nb = %s"""

    try:
        selection = execute_close_base(sql, c, connection, commit=False, parameters=params)
        return selection

    except mysql.connector.Error as err:
        print("There is neither a product nor an article-number matching your search!")
        menue()


def menue():
    print("select the process you want to execute")
    print("--------------------------------------")
    print(f"[1]     Create table")
    print(f"[2]     Insert Products")
    print(f"[3]     Select Product")
    print(f"[4]     Delete Product")
    print(f"[5]     Search Product")
    print(f"[6]     Update table")
    print(f"[7]     Alter table")


    option = int(input("Select an option: "))

    match option:
        case (1):
            create_table()
        case (2):
            insert_products()
        case (3):
            select_products()
        case (4):
            delete_products()
        case (5):
            search_products()

if __name__ == '__main__':
    main(connection_params)

