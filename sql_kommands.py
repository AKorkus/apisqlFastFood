# Kreate Table................................................................................................................
from json_handler import quot

def create_table(table_name, dikt, auto_id = True):
    """
    Por ejemplo:
    >>>create_projects_sql = create_table("projects", "nazwa text NOT NULL", "start_date text", "end_date text")
    CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    nazwa text NOT NULL,
    start_date text,
    end_date text
    """
    create_sql = f"""CREATE TABLE IF NOT EXISTS {table_name}(
    """
    if auto_id:
        create_sql += """id integer Primary KEY,
"""
    for item in dikt:
        create_sql += f"""{item} {dikt[item]},
"""
    create_sql = create_sql[:-2] + ");"
    return create_sql

# Insert Into................................................................................................................
def insert_into(table_name, data):
    '''
    Arguments:
    table_name (string) - name of the table in which you want to insert values.
    data (dictionary, json) - dictionary with the structure: {attribute (Day): value ("31-09-2021")}
    '''
    head = f'INSERT INTO {table_name}('
    body = f"VALUES("
    for attr in data:
        head += f"{attr}, "
        body += f"'{data[attr]}', "
    head = head[:-2] + ")"
    body = body[:-2] + ")"
    kommand = f"""{head}
    {body}"""
    return kommand


# Delete.......................................................................................................................
def delete(table_name, *args, column = "id", reverse = False):
    sql = f"Delete FROM {table_name}"
    if len(args) and len(column) > 0:
        arg_list = "("
        for arg in args:
            arg = quot(arg)
            arg_list += f"{arg}, "
        arg_list = arg_list[:-2] + ")"
        nothin = ""
        if reverse:
            nothin = "not "
        sql += f" where {column} {nothin}in {arg_list}"
    return sql


# UPDATE:.......................................................................................................................
def update(table_name, change_column, change_value, where_column, where_value):
    sql = f"""UPDATE {table_name}
    SET {change_column} = {quot(change_value)}
    WHERE {where_column} = {quot(where_value)}
    ;
    """
    return sql

def update_by_id(table_name, id, data):
    sql = f"""UPDATE {table_name}
    SET """
    for attr in data:
        sql += f"{attr} = {quot(data[attr])}, "
    sql = sql[:-2] + f"""
    WHERE id = {id}"""
    return sql


# Selekty......................................................................................................................

# Prosty Select:
def simple_select(table_name):
    query = f"Select * from {table_name};"
    return query

# Select bez grupowania:
def select_no_groups(table_name, select_what = ["*"], where = "", order = ""):
    query = f"Select "
    for column in select_what:
        query += f"{column}, "
    query = query[:-2] + f"""
    from {table_name}
    """
    if len(where) > 0:
        query += f"""where {where}
        """
    if len(order) > 0:
        query += f"order by {order}"
    query += ";"

    return query