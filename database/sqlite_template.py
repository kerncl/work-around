import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s [%(levelname)s]: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
# logging.addLevelName(logging.DEBUG)

TABLE = {
    'projects': '''
    CREATE TABLE IF NOT EXISTS projects(
        id integer PRIMARY KEY ,
        name text NOT NULL ,
        begin_date text,
        end_date text
        );''',
    'tasks': '''
    CREATE TABLE IF NOT EXISTS tasks(
        id integer primary key ,
        name text NOT NULL ,
        priority integer,
        status_id integer NOT NULL ,
        project_id integer NOT NULL ,
        begin_date text NOT NULL ,
        end_date text,
        FOREIGN KEY (project_id) REFERENCES projects (id)
        );'''
}


def create_connection(db_file):
    """
    Create a database connection to a SQLite database

    Args:
        db_file (file): database file path

    Returns:
        Connection object or None
    """
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')  # create database in RAM
        conn = sqlite3.connect(db_file)
        logging.info(sqlite3.version)
        logging.debug('Succefully created db')
    except Error as e:
        logging.error(e)
    # finally:
    #     if conn:
    #         conn.close()
    return conn


def create_execute(conn, sql):
    """
    Create a table from create_table_sql statement
    Args:
        conn (obj): Connection object
        sql (): SQL query command

    Returns:
        None
    """
    try:
        logging.debug(f'SQL Command: {sql}')
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        logging.info('Succefully executed')
    except Error as e:
        logging.error(e)

def create_read_execute(conn, sql):
    """
    Read data from table
    Args:
        conn (object): Connection Object
        sql (): SQL Command

    Returns:
        table data
    """
    cur = conn.cursor()
    result = None
    try:
        logging.debug(f'SQL Command: {sql}')
        cur.execute(sql)
        result = cur.fetchall()
        logging.info('Succefully fetched')
        return result
    except Error as e:
        logging.error(e)


def create_table(db_file):
    """
    Create a database connection to a SQLite database

    Args:
        db_file (file): database file path

    Returns:
        Connection object or None
    """
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')  # create database in RAM
        conn = sqlite3.connect(db_file)
        logging.info(sqlite3.version)
        logging.debug('Succefully created db')
    except Error as e:
        logging.error(e)
    finally:
        if conn:
            conn.close()
    return conn


def insert_into(conn, table, args, data):
    """
    Insert data into TABLE
    Args:
        conn (obj): Connection object
        table (str): table name
        args (list/tuple): list of table field
        data (list/tuple): list of data field

    Returns:
        None
    """
    sql = f'''INSERT INTO {table} ({','.join(args)}) VALUES ({','.join(data)})'''
    cur = conn.cursor()
    try:
        logging.debug(f'SQL Command: {sql}')
        cur.execute(sql)
        cur.commit()
        logging.debug('Succefully Executed')
    except Error as e:
        logging.error(e)


def create_project(conn, project):
    """
    Create a new project into the projects table
    Args:
        conn (obj): Connection object
        project ():

    Returns:
        project id
    """
    sql = ''' INSERT INTO projects(name, begin_date, end_date) 
                VALUES (?,?,?)'''
    logging.debug(f'SQL Command: {sql}')
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    logging.info('Successfully create project')
    return cur.lastrowid


def create_task(conn, task):
    """
    Insert data into tasks table
    Args:
        conn (obj): Connection object
        task (tuple): tuple field data

    Returns:
        last id number
    """
    sql = """INSERT INTO tasks (name, priority, status_id, project_id, begin_date, end_date)
                VALUES (?,?,?,?,?,?);"""
    logging.debug(f'SQL Command: {sql}')
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    logging.info('Successfully create task')
    return cur.lastrowid


def update_task(conn, task):
    """
    Update data in task table
    Args:
        conn (obj): Connection object
        task (tuple): field datas

    Returns:
        None
    """
    sql = """UPDATE tasks
                SET priority= ?,
                    begin_date = ?,
                    end_date = ?
                WHERE id = ?"""
    logging.debug(f'SQL Command: {sql}')
    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()
    logging.info('Succefully Executed')


def delete_task(conn, id):
    """
    Delete data based on id given
    Args:
        conn (obj): Connection Object
        id (int): ID number of data

    Returns:
        None
    """
    sql = '''DELETE FROM tasks WHERE id=?'''
    logging.debug(f'SQL Command: {sql}')
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    logging.info(f'Succefully deleted id:{id}')


def delete_all_task(conn):
    """
    Delete tasks table
    Args:
        conn (obj): Connection Object

    Returns:
        None
    """
    sql = '''DELETE FROM tasks'''
    logging.debug(f'SQL Command {sql}')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def select_all_task(conn):
    """
    Query all rows in the tasks table
    Args:
        conn (obj): Connection Obj

    Returns:
        None
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()

    for row in rows:
        logging.info(row)

def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    Args:
        conn (obj): Connection Obj
        priority ():

    Returns:
        None
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()

    for row in rows:
        logging.info(row)


if __name__ == '__main__':
    conn = create_connection(r'sql_template.db')
    if conn:
        with conn:
            # Create table
            create_execute(conn, TABLE['projects'])
            create_execute(conn, TABLE['tasks'])

            # Insert data into project
            project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
            project_id = create_project(conn, project)

            # Insert data into tasks
            task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
            task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
            create_task(conn, task_1)
            create_task(conn, task_2)

            # udpate on task data
            update_task(conn, (2, '2015-01-04', '2015-01-06', 2))

            # Delete data on tasks table
            delete_task(conn, 2)

            # Query data from tasks
            select_task_by_priority(conn, 1)
            select_all_task(conn)
    else:
        logging.error('Error! cannot create the database connection')



