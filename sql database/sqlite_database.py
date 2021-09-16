import os
import logging
import logging.handlers
import sqlite3
from sqlite3 import Error

# SQL TABLE
table_dict = {
    'create_users_table': """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            name TEXT NOT NULL,
            age INTEGER ,
            gender TEXT,
            nationality TEXT
            );""",
    'create_posts_table' : """
        CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
            );""",
    'create_comments_table' : """
        CREATE TABLE IF NOT EXISTS comments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            post_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
        );""",
    'create_likes_table' : """
        CREATE TABLE IF NOT EXISTS likes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            post_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
        )"""
      }

# data
data = {
    'create_users' : """
        INSERT INTO
            users (name, age, gender, nationality)
        VALUES
            ('James', 25, 'male', 'USA'),
            ('Leila', 32, 'female', 'France'),
            ('Brigitte', 35, 'female', 'England'),
            ('Mike', 40, 'male', 'Denmark'),
            ('Elizabeth', 21, 'female', 'Canada');
        """,
    'create_posts' : """
        INSERT INTO
            posts (title, description, user_id)
        VALUES
            ('Happy', 'I am feeling very happy today', 1),
            ('Hot Weather', 'The weather is very hot', 2),
            ('Help', 'I need some help with my work', 2),
            ('Great News', 'I am getting married', 1),
            ('Intersting', 'It was a fantastic game of tennis', 5),
            ('Party', 'Anyone up for late-night party today?', 3);
        """,
    'create_comments' : """
    INSERT INTO
        comments (text, user_id, post_id)
    VALUES 
        ('Count me in', 1, 6),
        ('What sort of help?', 2, 4),
        ('Congrats buddy', 2, 4),
        ('I was rooting for Nadal through', 4, 5),
        ('Help with your thesis?', 2, 3),
        ('Many Congratulations', 5, 4);
    """,
    'create_likes' : """
    INSERT INTO
        likes (user_id, post_id)
    VALUES 
        (1,6),
        (2,3),
        (1,5),
        (5,4),
        (2,4),
        (4,2),
        (3,6);
    """
}

#initilize_log
logger = logging.getLogger('sql_log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
logger.setLevel(logging.DEBUG)

# Stream_handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# sql log
master_handler = logging.FileHandler(filename='sql.log', mode='w')
master_handler.setFormatter(logging.DEBUG)
master_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(master_handler)


def create_connection(path):
    connection = None
    try:
        logger.debug(f'path: {path}')
        connection = sqlite3.connect(path)
        logger.info("Connection to SQLite DB successful")
    except Error as e:
        logger.error(f"The error '{e}' occured")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        logger.debug(f'SQL command: {query}')
        cursor.execute(query)
        connection.commit()
        logger.info("Query executed successfully")
    except Error as e:
        logger.error(f"{e} occured")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        logger.debug(f'SQL Command: {query}')
        cursor.execute(query)
        result = cursor.fetchall()
        logger.info('Done fetched')
        return result
    except Error as e:
        logger.error(f'{e} occurred')


def main():
    connection = create_connection('sm_app.sqlite')
    # Create Table
    execute_query(connection, table_dict['create_users_table'])
    execute_query(connection, table_dict['create_posts_table'])
    execute_query(connection, table_dict['create_comments_table'])
    execute_query(connection, table_dict['create_likes_table'])
    # Insert data
    execute_query(connection, data['create_users'])
    execute_query(connection, data['create_posts'])
    execute_query(connection, data['create_comments'])
    execute_query(connection, data['create_likes'])
    ## Fetch data
    # user
    select_users = 'SELECT * FROM users'
    users = execute_read_query(connection, select_users)
    for user in users:
        logger.info(f'{user}')
    # post
    select_posts = 'SELECT * FROM posts'
    posts = execute_read_query(connection, select_posts)
    for post in posts:
        logger.info(f'{post}')

    # JOIN
    select_users_posts = """
    SELECT
        users.id,
        users.name,
        posts.description
    FROM
        posts
        INNER JOIN users ON users.id = posts.user_id
    """
    users_posts = execute_read_query(connection, select_users_posts)
    for users_post in users_posts:
        logger.info(f'{users_post}')
    select_posts_comments_users ="""
    SELECT
        posts.description as post,
        comments.text as comment,
        users.name
    FROM
        posts
        INNER JOIN comments ON posts.id = comments.post_id
        INNER JOIN users ON users.id = comments.user_id
    """
    posts_comments_users = execute_read_query(connection, select_posts_comments_users)
    for posts_comments_user in posts_comments_users:
        logger.info(f'{posts_comments_user}')

    # WHERE
    select_post_likes = """
    SELECT
        description as Post,
        COUNT(likes.id) as Likes
    FROM
        likes,
        posts
    WHERE
        posts.id = likes.post_id
    GROUP BY
        likes.post_id
    """
    post_likes = execute_read_query(connection, select_post_likes)
    for post_like in post_likes:
        logger.info(f'{post_like}')

    # Update
    select_post_description = "SELECT description FROM posts WHERE id=2"
    post_description = execute_read_query(connection, select_post_description)
    for description in post_description:
        logger.info(f'{description}')
    update_post_description = """
    UPDATE
        posts
    SET
        description = "The weather has become pleasant now"
    WHERE
        id = 2
    """
    execute_query(connection, update_post_description)

    # DELETE
    delete_comment = "DELETE FROM comments WHERE id=5"
    execute_query(connection, delete_comment)

    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)


if __name__ == '__main__':
    main()